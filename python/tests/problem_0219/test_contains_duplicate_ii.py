import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0219.contains_duplicate_ii import Solution


def test_containsNearbyDuplicate() -> None:
    """Test containsNearbyDuplicate function."""
    solution = Solution()
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
