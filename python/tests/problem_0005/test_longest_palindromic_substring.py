import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0005.longest_palindromic_substring import Solution


def test_longestPalindrome() -> None:
    """Test longestPalindrome function."""
    solution = Solution()
    assert solution.longestPalindrome("babad") == "bab"
    assert solution.longestPalindrome("cbbd") == "bb"
