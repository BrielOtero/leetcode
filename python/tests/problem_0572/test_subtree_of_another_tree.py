import sys
from pathlib import Path

from utils.trees import create_tree_node

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0572.subtree_of_another_tree import Solution


def test_isSubtree() -> None:
    """Test isSubtree function."""
    solution = Solution()
    assert solution.isSubtree(
        create_tree_node([3, 4, 5, 1, 2]), create_tree_node([4, 1, 2])
    )
    assert not solution.isSubtree(
        create_tree_node([3, 4, 5, 1, 2, None, None, None, None, 0]),
        create_tree_node([4, 1, 2]),
    )
