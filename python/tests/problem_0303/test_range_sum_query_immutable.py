import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0303.range_sum_query_immutable import NumArray


def test_sumRange() -> None:
    """Test sumRange function."""
    # ["NumArray", "sumRange", "sumRange", "sumRange"]
    # [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    # [null, 1, -1, -3]
    solution = NumArray([-2, 0, 3, -5, 2, -1])
    assert solution.sumRange(0, 2) == 1
    assert solution.sumRange(2, 5) == -1
    assert solution.sumRange(0, 5) == -3
