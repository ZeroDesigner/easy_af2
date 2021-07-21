# 准备好迎接蛋白设计的时代了吗？--AlphaFold2的几种使用方式



## 前言：

AF2已经出了一段时间，上次看了看RoseTTAFold，这次我们试试AlphaFold2.

## 方式

### 1 躺平

简称白嫖Geogle，直接使用colab进行使用，当然你得会科学上网

Colab提供了一张GPU V100 以供挥霍

直接点击进入 此网站 https://colab.research.google.com/drive/1PePaHHp1J-L1rufW4_r7v7VpZjYVUbTH

熟悉Jupyter的应该都知道怎么操作，不知道的百度下

另外下面这种操作方式，不使用MSA信息，适用于蛋白质从头设计，

第一步：colab提供了一张GPU或者TPU以供调用，选择GPU就好

![image-20210721001713671](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/image-20210721001713671.png)

第二步：

点击方格左侧的▶️使其运行，或者直接shift+ctrl

![image-20210721001842649](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/image-20210721001842649.png)

注意：

在这个地方，将query_sequence改为你自己的序列

![image-20210721001936104](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/image-20210721001936104.png)

第三步：

predict_structure 在预测结构，而下方的excute则是运行时间，案例这个跑了大约2min左右，约68个氨基酸

初始会慢一些，后续基本在20s左右

![image-20210721002204764](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/image-20210721002204764.png)

第四步查看结构，以及下载

![image-20210721002455565](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/image-20210721002455565.png)

在左方的none中点击并下载

![image-20210721003805474](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/image-20210721003805474.png)



### 2 本地版



第一步直接git clone

`git clone https://github.com/deepmind/alphafold.git`

第二步 使用conda创造环境

```bash
conda env create -f alphafold.yaml
conda activate alphafold
```

第三步下载

alphafold 提供了一个自动化下载脚本

```bash
cd scripts
nohup sh download_all_data.sh ./ &
```

这一步时间很长,直接nohup挂到后台

所用空间

```bash
$DOWNLOAD_DIR/                             # Total: ~ 2.2 TB (download: 428 GB)
    bfd/                                   # ~ 1.8 TB (download: 271.6 GB)
        # 6 files.
    mgnify/                                # ~ 64 GB (download: 32.9 GB)
        mgy_clusters.fa
    params/                                # ~ 3.5 GB (download: 3.5 GB)
        # 5 CASP14 models,
        # 5 pTM models,
        # LICENSE,
        # = 11 files.
    pdb70/                                 # ~ 56 GB (download: 19.5 GB)
        # 9 files.
    pdb_mmcif/                             # ~ 206 GB (download: 46 GB)
        mmcif_files/
            # About 180,000 .cif files.
        obsolete.dat
    uniclust30/                            # ~ 87 GB (download: 24.9 GB)
        uniclust30_2018_08/
            # 13 files.
    uniref90/                              # ~ 59 GB (download: 29.7 GB)
        uniref90.fasta
```

第四步 运行alphafold

```bash
bash run_alphafold.sh -d ./scripts -o ./output/ -m model_1 -f ./example/query.fasta -t 2020-05-14
```

### 推荐配置：

1. GPU：一张A100 显卡  5w-7w（目前还没有在这么强大的显卡上跑过），
2. 存储空间：50T ，5k-1w左右
3. CPU： [Intel® Xeon® Gold 6338 Processor (48M Cache, 2.00 GHz)](https://www.intel.cn/content/www/cn/zh/products/sku/212285/intel-xeon-gold-6338-processor-48m-cache-2-00-ghz/specifications.html) 32 cores  8k左右

价格都差不多，当然你还需要人力来配置，人工费用另算。或者直接买超算的GPU核时。

## 参考：

1. AlphaFold2:https://github.com/deepmind/alphafold
2. Colab上的AF2：https://github.com/sokrypton/ColabFold
3. 非docker下的AF2:https://github.com/deepmind/alphafold/issues/24
4. 硬盘价格：https://www.jd.com/jiage/67036b20876f0c79715.html
5. A100 价格：https://www.smzdm.com/p/36608092/
6. CPU价格：https://www.intel.cn/content/www/cn/zh/products/details/processors/xeon/scalable/gold.html#:~:text=%E7%AC%AC%E4%B8%89%E4%BB%A3%E8%8B%B1%E7%89%B9%E5%B0%94%C2%AE%20%E8%87%B3%E5%BC%BA%C2%AE%20%E5%8F%AF%E6%89%A9%E5%B1%95%E5%A4%84%E7%90%86%E5%99%A8%E5%8C%85%E6%8B%AC%E8%8B%B1%E7%89%B9%E5%B0%94%C2%AE%20SGX%EF%BC%8C%E5%8F%AF%E5%AE%9E%E6%97%B6%E4%BF%9D%E6%8A%A4%E8%BE%B9%E7%BC%98%E3%80%81%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%E5%92%8C%E5%A4%9A%E7%A7%9F%E6%88%B7%E5%85%AC%E5%85%B1%E4%BA%91%E4%B8%AD%E7%9A%84%E6%95%B0%E6%8D%AE%E5%92%8C%E5%BA%94%E7%94%A8%E4%BB%A3%E7%A0%81%EF%BC%8C%E6%94%AF%E6%8C%81%E8%BF%90%E7%94%A8%E5%85%B1%E4%BA%AB%E6%95%B0%E6%8D%AE%E6%9D%A5%E5%8A%A0%E5%BC%BA%E5%8D%8F%E4%BD%9C%EF%BC%88%E4%BE%8B%E5%A6%82%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%AD%E7%9A%84%E8%81%94%E5%90%88%E5%AD%A6%E4%B9%A0%EF%BC%89%EF%BC%8C%E5%90%8C%E6%97%B6%E4%B8%8D%E6%8D%9F%E5%AE%B3%E9%9A%90%E7%A7%81%E3%80%82,%E8%8B%B1%E7%89%B9%E5%B0%94%C2%AE%20Speed%20Select%20%E6%8A%80%E6%9C%AF%EF%BC%88%E8%8B%B1%E7%89%B9%E5%B0%94%C2%AE%20SST%EF%BC%89%E9%9B%86%E5%90%88%E4%BA%86%E5%8F%AF%E9%85%8D%E7%BD%AE%E7%9A%84%E5%A4%84%E7%90%86%E5%99%A8%E7%89%B9%E6%80%A7%EF%BC%8C%E4%BB%8E%E8%80%8C%E4%BC%98%E5%8C%96%E5%A4%84%E7%90%86%E8%B5%84%E6%BA%90%E4%BB%A5%E6%8F%90%E9%AB%98%E5%B7%A5%E4%BD%9C%E8%B4%9F%E8%BD%BD%E6%80%A7%E8%83%BD%E5%B9%B6%E6%8F%90%E9%AB%98%E5%88%A9%E7%94%A8%E7%8E%87%EF%BC%8C%E8%BF%98%E5%8F%AF%E5%B8%AE%E5%8A%A9%E4%BC%98%E5%8C%96%E6%80%BB%E6%8B%A5%E6%9C%89%E6%88%90%E6%9C%AC%E3%80%82





 
