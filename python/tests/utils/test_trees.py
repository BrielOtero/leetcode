import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from utils.trees import create_tree_node, serialize_tree


def test_serialize_tree() -> None:
    """Test serialize_tree function."""
    # Test basic tree
    tree = create_tree_node([4, 2, 7, 1, 3])
    result = serialize_tree(tree)
    assert result == [4, 2, 7, 1, 3]

    # Test tree with None values
    tree = create_tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    result = serialize_tree(tree)
    assert result == [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]

    # Test empty tree
    result = serialize_tree(None)
    assert result == []

    # Test single node
    tree = create_tree_node([1])
    result = serialize_tree(tree)
    assert result == [1]
