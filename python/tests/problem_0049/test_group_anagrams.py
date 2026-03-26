import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0049.group_anagrams import Solution


def test_groupAnagrams() -> None:
    """Test groupAnagrams function."""
    solution = Solution()

    # Test multiple anagrams
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

    # Sort each group internally
    result = [sorted(group) for group in result]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    expected = [sorted(group) for group in expected]

    # Sort groups themselves
    result.sort()
    expected.sort()
    assert result == expected

    # Test empty string
    result = solution.groupAnagrams([""])
    expected = [[""]]
    assert result == expected

    # Test single-character string
    result = solution.groupAnagrams(["a"])
    expected = [["a"]]
    assert result == expected
