import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0167.two_sum_ii_input_array_is_sorted import Solution


def test_twoSum() -> None:
    """Test twoSum function."""
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
