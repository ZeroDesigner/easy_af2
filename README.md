# 准备好迎接蛋白设计的时代了吗？--AlphaFold2的两种使用方式



## 前言：

AF2已经出了一段时间，上次试了试RoseTTAFold，这次我们试试AlphaFold2。

![03d40565b55d43818f9968ac555cec2b](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/03d40565b55d43818f9968ac555cec2b.png)

## 方式

### 1 躺平式

简称白嫖Geogle，直接使用colab进行使用，当然你得会科学上网（别看了，我这里不教）

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

![image-20210721002204764](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/image-20210721002204764.png)

第四步查看结构，以及下载

![image-20210721002455565](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/image-20210721002455565.png)

在左方的none中点击并下载

![image-20210721003805474](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/image-20210721003805474.png)



### 2 本地版



第一步直接git clone

```bash
git clone git@github.com:ZeroDesigner/easy_af2.git
```

第二步 使用conda创造环境

```bash
conda env create -f easy_af2.yaml
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
3. CPU： [Intel® Xeon® Gold 6338 Processor (48M Cache, 2.00 GHz)](https://www.intel.cn/content/www/cn/zh/products/sku/212285/intel-xeon-gold-6338-processor-48m-cache-2-00-ghz/specifications.html) 32 cores  2w左右

价格都差不多，当然你还需要人力来配置，人工费用另算。或者直接买超算的GPU核时。

### 后记

还有很多不同的玩法

具体参看：

1. https://github.com/sokrypton/ColabFold
2. https://github.com/deepmind/alphafold/issues/24

## 参考：

1. AlphaFold2:https://github.com/deepmind/alphafold
2. Colab上的AF2：https://github.com/sokrypton/ColabFold
3. 非docker下的AF2:https://github.com/deepmind/alphafold/issues/24
4. 硬盘价格：https://www.jd.com/jiage/67036b20876f0c79715.html
5. A100 价格：https://www.smzdm.com/p/36608092/



 

