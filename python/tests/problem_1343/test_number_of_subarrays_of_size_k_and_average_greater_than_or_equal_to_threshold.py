import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_1343.number_of_subarrays_of_size_k_and_average_greater_than_or_equal_to_threshold import (
    Solution,
)


def test_numOfSubarrays() -> None:
    """Test numOfSubarrays function."""
    solution = Solution()
    assert solution.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3
