import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_1991.find_the_middle_index_in_array import Solution


def test_findMiddleIndex() -> None:
    """Test findMiddleIndex function."""
    solution = Solution()
    assert solution.findMiddleIndex([2, 3, -1, 8, 4]) == 3
    assert solution.findMiddleIndex([1, -1, 4]) == 2
    assert solution.findMiddleIndex([2, 5]) == -1
