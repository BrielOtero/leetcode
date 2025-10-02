import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0424.longest_repeating_character_replacement import Solution


def test_characterReplacement() -> None:
    """Test characterReplacement function."""
    solution = Solution()
    assert solution.characterReplacement("ABAB", 2) == 4
