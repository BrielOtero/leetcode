import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0080.remove_duplicates_from_sorted_array_ii import Solution


def test_removeDuplicates() -> None:
    """Test removeDuplicates function."""
    solution = Solution()
    assert solution.removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
