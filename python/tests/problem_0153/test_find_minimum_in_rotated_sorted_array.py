import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0153.find_minimum_in_rotated_sorted_array import Solution


def test_findMin() -> None:
    """Test findMin function."""
    solution = Solution()
    assert solution.findMin([3, 4, 5, 1, 2]) == 1
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([11, 13, 15, 17]) == 11
