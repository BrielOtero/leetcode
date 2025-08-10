import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0700.search_in_a_binary_search_tree import Solution, TreeNode


def same_tree(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    return a.val == b.val and same_tree(a.left, b.left) and same_tree(a.right, b.right)


def test___init__() -> None:
    """Test __init__ function."""
    solution = Solution()
    head = TreeNode(4)
    head.left = TreeNode(2)
    head.right = TreeNode(7)
    head.left.left = TreeNode(1)
    head.left.right = TreeNode(3)

    res = TreeNode(2, TreeNode(1), TreeNode(3))

    assert same_tree(solution.searchBST(head, 2), res)
