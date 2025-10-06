import sys
from pathlib import Path

from utils.trees import create_tree_node

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0235.lowest_common_ancestor_of_a_binary_search_tree import Solution


def test_lowestCommonAncestor() -> None:
    """Test lowestCommonAncestor function."""
    solution = Solution()

    # Test 1
    root = create_tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = create_tree_node([2])
    q = create_tree_node([8])
    assert root and p and q
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 6, f"Expected 6, got {result.val}"

    # Test 2
    root = create_tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = create_tree_node([2])
    q = create_tree_node([4])
    assert root and p and q
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 2, f"Expected 2, got {result.val}"

    # Test 3
    root = create_tree_node([2, 1])
    p = create_tree_node([2])
    q = create_tree_node([1])
    assert root and p and q
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 2, f"Expected 2, got {result.val}"
