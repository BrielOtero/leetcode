import sys
from pathlib import Path

from utils.trees import create_tree_node

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0124.binary_tree_maximum_path_sum import Solution


def test_maxPathSum() -> None:
    """Test maxPathSum function."""
    solution = Solution()
    assert solution.maxPathSum(create_tree_node([1, 2, 3])) == 6
    assert solution.maxPathSum(create_tree_node([-10, 9, 20, None, None, 15, 7])) == 42
