import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0724.find_pivot_index import Solution


def test_pivotIndex() -> None:
    """Test pivotIndex function."""
    solution = Solution()
    assert solution.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert solution.pivotIndex([1, 2, 3]) == -1
    assert solution.pivotIndex([2, 1, -1]) == 0
