import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0003.longest_substring_without_repeating_characters import Solution

def test_lengthOfLongestSubstring() -> None:
    """Test lengthOfLongestSubstring function."""
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
