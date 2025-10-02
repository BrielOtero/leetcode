import sys
from pathlib import Path

from utils.trees import create_tree_node

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0104.maximum_depth_of_binary_tree import Solution


def test_maxDepth() -> None:
    """Test maxDepth function."""
    solution = Solution()
    test_1_input = create_tree_node([3, 9, 20, None, None, 15, 7])
    assert solution.maxDepth(test_1_input) == 3

    solution = Solution()
    test_2_input = create_tree_node([1, None, 2])
    assert solution.maxDepth(test_2_input) == 2
