import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0700.search_in_a_binary_search_tree import Solution
from utils.trees import create_tree_node, serialize_tree


def test_searchBST() -> None:
    """Test searchBST function."""
    solution = Solution()
    test_1_tree_node = create_tree_node([4, 2, 7, 1, 3])
    test_1_result = solution.searchBST(test_1_tree_node, 2)
    test_1_expected: list = [2, 1, 3]

    assert serialize_tree(test_1_result) == test_1_expected

    test_2_tree_node = create_tree_node([4, 2, 7, 1, 3])
    test_2_result = solution.searchBST(test_2_tree_node, 5)
    test_2_expected: list = []

    assert serialize_tree(test_2_result) == test_2_expected
