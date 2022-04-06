import sys
import os
sys.path.append(os.getcwd())
import pytest

from middlewared.plugins.pool_.dataset_recordsize import generate_recordsize_choices, MAPPING

EXPECTED_RESULT = {}
for raw_val, human_readable in MAPPING.items():
    if human_readable == '512B':
        EXPECTED_RESULT[raw_val] = set((human_readable,))
    elif human_readable == '1K':
        EXPECTED_RESULT[raw_val] = set(('512B', human_readable))
    elif human_readable == '2K':
        EXPECTED_RESULT[raw_val] = set(('512B', '1K', human_readable))
    elif human_readable == '4K':
        EXPECTED_RESULT[raw_val] = set(('512B', '1K', '2K', human_readable))
    elif human_readable == '8K':
        EXPECTED_RESULT[raw_val] = set(('512B', '1K', '2K', '4K', human_readable))
    elif human_readable == '16K':
        EXPECTED_RESULT[raw_val] = set(('512B', '1K', '2K', '4K', '8K', human_readable))
    elif human_readable == '32K':
        EXPECTED_RESULT[raw_val] = set(('512B', '1K', '2K', '4K', '8K', '16K', human_readable))
    elif human_readable == '64K':
        EXPECTED_RESULT[raw_val] = set(('512B', '1K', '2K', '4K', '8K', '16K', '32K', human_readable))
    elif human_readable == '128K':
        EXPECTED_RESULT[raw_val] = set(('512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', human_readable))
    elif human_readable == '256K':
        EXPECTED_RESULT[raw_val] = set(('512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', human_readable))
    elif human_readable == '512K':
        EXPECTED_RESULT[raw_val] = set((
            '512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', human_readable
        ))
    elif human_readable == '1M':
        EXPECTED_RESULT[raw_val] = set((
            '512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K', human_readable
        ))
    elif human_readable == '2M':
        EXPECTED_RESULT[raw_val] = set((
            '512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K',
            '1M', human_readable
        ))
    elif human_readable == '4M':
        EXPECTED_RESULT[raw_val] = set((
            '512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K',
            '1M', '2M', human_readable
        ))
    elif human_readable == '8M':
        EXPECTED_RESULT[raw_val] = set((
            '512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K',
            '1M', '2M', '4M', human_readable
        ))
    elif human_readable == '16M':
        EXPECTED_RESULT[raw_val] = set((
            '512B', '1K', '2K', '4K', '8K', '16K', '32K', '64K', '128K', '256K', '512K',
            '1M', '2M', '4M', '8M', human_readable
        ))


@pytest.mark.parametrize('recordsize', list(MAPPING.keys()))
def test_generate_choices_for_recordsize(recordsize):
    # set the max recordsize first
    with open('/sys/module/zfs/parameters/zfs_max_recordsize', 'w') as f:
        f.write(recordsize)

    assert set(generate_recordsize_choices()) == EXPECTED_RESULT[recordsize]
