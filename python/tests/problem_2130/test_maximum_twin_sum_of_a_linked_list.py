import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_2130.maximum_twin_sum_of_a_linked_list import Solution
from utils.linked_lists import create_singly_linked_list


def test_pairSum() -> None:
    """Test pairSum function."""
    solution = Solution()

    test_1_input = create_singly_linked_list([5, 4, 2, 1])
    assert solution.pairSum(test_1_input) == 6

    test_2_input = create_singly_linked_list([4, 2, 2, 3])
    assert solution.pairSum(test_2_input) == 7

    test_3_input = create_singly_linked_list([1, 100000])
    assert solution.pairSum(test_3_input) == 100001
