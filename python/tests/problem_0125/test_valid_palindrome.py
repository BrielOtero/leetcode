import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0125.valid_palindrome import Solution


def test_isPalindrome() -> None:
    """Test isPalindrome function."""
    solution = Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama")
