import sys
from pathlib import Path


# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0226.invert_binary_tree import Solution
from utils.trees import TreeNode, create_tree_node, serialize_tree


def test_invertTree() -> None:
    """Test invertTree function."""
    solution = Solution()
    test_1_input = create_tree_node([4, 2, 7, 1, 3, 6, 9])
    test_1_expected = [4, 7, 2, 9, 6, 3, 1]
    test_1_output = solution.invertTree(test_1_input)
    assert serialize_tree(test_1_output) == test_1_expected

    test_2_input = create_tree_node([2, 1, 3])
    test_2_expected = [2, 3, 1]
    test_2_output = solution.invertTree(test_2_input)
    assert serialize_tree(test_2_output) == test_2_expected

    test_3_input = None
    test_3_expected: list[TreeNode] = []
    test_3_output = solution.invertTree(test_3_input)
    assert serialize_tree(test_3_output) == test_3_expected
