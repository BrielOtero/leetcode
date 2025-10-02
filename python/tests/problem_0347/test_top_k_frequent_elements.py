import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0347.top_k_frequent_elements import Solution


def test_topKFrequent() -> None:
    """Test topKFrequent function."""
    solution = Solution()
    assert solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
