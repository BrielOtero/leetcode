import sys
from pathlib import Path

from utils.trees import create_tree_node

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0098.validate_binary_search_tree import Solution


def test_isValidBST() -> None:
    """Test isValidBST function."""
    solution = Solution()

    assert solution.isValidBST(create_tree_node([2, 1, 3]))
    assert not solution.isValidBST(create_tree_node([5, 1, 4, None, None, 3, 6]))
