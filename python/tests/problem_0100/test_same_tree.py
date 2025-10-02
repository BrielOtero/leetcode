import sys
from pathlib import Path


# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0100.same_tree import Solution
from utils.trees import create_tree_node


def test_isSameTree() -> None:
    """Test isSameTree function."""
    solution = Solution()

    # Test 1
    # Input: p = [1,2,3], q = [1,2,3]
    # Output: true
    assert solution.isSameTree(create_tree_node([1, 2, 3]), create_tree_node([1, 2, 3]))

    # Test 2
    # Input: p = [1,2], q = [1,null,2]
    # Output: false
    assert not solution.isSameTree(
        create_tree_node([1, 2]), create_tree_node([1, None, 2])
    )

    # Test 3
    # Input: p = [1,2,1], q = [1,1,2]
    # Output: false
    assert not solution.isSameTree(
        create_tree_node([1, 2, 1]), create_tree_node([1, 1, 2])
    )
