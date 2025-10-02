import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0022.generate_parentheses import Solution


def test_generateParenthesis() -> None:
    """Test generateParenthesis function."""
    solution = Solution()
    assert solution.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
    assert solution.generateParenthesis(1) == ["()"]
