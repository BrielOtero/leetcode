import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0053.maximum_subarray import Solution


def test_maxSubArray() -> None:
    """Test maxSubArray function."""
    solution = Solution()
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
