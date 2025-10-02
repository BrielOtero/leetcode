import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0079.word_search import Solution

def test_exist() -> None:
    """Test exist function."""
    solution = Solution()
    assert solution.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
    assert solution.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
    )
    assert not solution.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
