import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0055.jump_game import Solution


def test_canJump() -> None:
    """Test canJump function."""
    solution = Solution()
    assert solution.canJump([2, 3, 1, 1, 4])
    assert not solution.canJump([2, 2, 1, 0, 4])
