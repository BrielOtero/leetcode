import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0647.palindromic_substrings import Solution


def test_countSubstrings() -> None:
    """Test countSubstrings function."""
    solution = Solution()
    assert solution.countSubstrings("abc") == 3
    assert solution.countSubstrings("aaa") == 6
