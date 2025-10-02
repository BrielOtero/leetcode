import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0978.longest_turbulent_subarray import Solution


def test_maxTurbulenceSize() -> None:
    """Test maxTurbulenceSize function."""
    solution = Solution()
    assert solution.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5
