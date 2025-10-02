import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0015.three_3sum import Solution


def test_threeSum() -> None:
    """Test threeSum function."""
    solution = Solution()
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert solution.threeSum([0, 1, 1]) == []
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]
