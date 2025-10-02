import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0560.subarray_sum_equals_k import Solution


def test_subarraySum() -> None:
    """Test subarraySum function."""
    solution = Solution()
    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2
