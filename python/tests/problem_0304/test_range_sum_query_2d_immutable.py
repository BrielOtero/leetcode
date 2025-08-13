import sys
from pathlib import Path
from typing import List

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0304.range_sum_query_2d_immutable import NumMatrix


def test___init__() -> None:
    """Test __init__ function."""
    solution = NumMatrix(
        [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
    )
    assert solution.sumRegion(2, 1, 4, 3) == 8
    assert solution.sumRegion(1, 1, 2, 2) == 11
    assert solution.sumRegion(1, 2, 2, 4) == 12
