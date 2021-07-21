# Copyright 2021 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for run_alphafold."""

import os

from absl.testing import absltest
from absl.testing import parameterized
import mock
import numpy as np

import run_alphafold
# Internal import (7716).


class RunAlphafoldTest(parameterized.TestCase):

  def test_end_to_end(self):

    data_pipeline_mock = mock.Mock()
    model_runner_mock = mock.Mock()
    amber_relaxer_mock = mock.Mock()

    data_pipeline_mock.process.return_value = {}
    model_runner_mock.process_features.return_value = {
        'aatype': np.zeros((12, 10), dtype=np.int32),
        'residue_index': np.tile(np.arange(10, dtype=np.int32)[None], (12, 1)),
    }
    model_runner_mock.predict.return_value = {
        'structure_module': {
            'final_atom_positions': np.zeros((10, 37, 3)),
            'final_atom_mask': np.ones((10, 37)),
        },
        'predicted_lddt': {
            'logits': np.ones((10, 50)),
        },
        'plddt': np.zeros(10),
        'ptm': np.array(0.),
        'aligned_confidence_probs': np.zeros((10, 10, 50)),
        'predicted_aligned_error': np.zeros((10, 10)),
        'max_predicted_aligned_error': np.array(0.),
    }
    amber_relaxer_mock.process.return_value = ('RELAXED', None, None)

    fasta_path = os.path.join(absltest.get_default_test_tmpdir(),
                              'target.fasta')
    with open(fasta_path, 'wt') as f:
      f.write('>A\nAAAAAAAAAAAAA')
    fasta_name = 'test'

    out_dir = absltest.get_default_test_tmpdir()

    run_alphafold.predict_structure(
        fasta_path=fasta_path,
        fasta_name=fasta_name,
        output_dir_base=out_dir,
        data_pipeline=data_pipeline_mock,
        model_runners={'model1': model_runner_mock},
        amber_relaxer=amber_relaxer_mock,
        benchmark=False,
        random_seed=0)


if __name__ == '__main__':
  absltest.main()
