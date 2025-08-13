import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0209.minimum_size_subarray_sum import Solution


def test_minSubArrayLen() -> None:
    """Test minSubArrayLen function."""
    solution = Solution()
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
