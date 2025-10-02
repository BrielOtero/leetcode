import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0033.search_in_rotated_sorted_array import Solution

def test_search() -> None:
    """Test search function."""
    solution = Solution()

    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert solution.search([1], 0) == -1
