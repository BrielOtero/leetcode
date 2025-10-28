import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0091.decode_ways import Solution


def test_numDecodings() -> None:
    """Test numDecodings function."""
    solution = Solution()
    assert solution.numDecodings("12") == 2
    assert solution.numDecodings("226") == 3
    assert solution.numDecodings("06") == 0
