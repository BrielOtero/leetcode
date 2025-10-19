import sys
from pathlib import Path

from utils.trees import create_tree_node, serialize_tree

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0297.serialize_and_deserialize_binary_tree import Codec


def test_codec() -> None:
    """Test codec class."""
    codec = Codec()
    test_1_serialize: list[int | None] = [1, 2, 3, None, None, 4, 5]
    test_1_node = create_tree_node(test_1_serialize)
    assert (
        serialize_tree(codec.deserialize(codec.serialize(test_1_node)))
        == test_1_serialize
    )

    test_2_serialize: list[int | None] = []
    test_2_node = create_tree_node(test_2_serialize)
    assert (
        serialize_tree(codec.deserialize(codec.serialize(test_2_node)))
        == test_2_serialize
    )
