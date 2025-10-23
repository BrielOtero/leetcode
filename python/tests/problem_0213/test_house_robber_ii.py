import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0213.house_robber_ii import Solution


def test_rob() -> None:
    """Test rob function."""
    solution = Solution()
    assert solution.rob([2, 3, 2]) == 3
    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([1, 2, 3]) == 3
