import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0287.find_the_duplicate_number import Solution


def test_findDuplicate() -> None:
    """Test findDuplicate function."""
    solution = Solution()
    assert solution.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert solution.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert solution.findDuplicate([3, 3, 3, 3, 3]) == 3
