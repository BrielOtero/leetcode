import sys
from pathlib import Path


# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0143.reorder_list import Solution
from utils.linked_lists import create_singly_linked_list, singly_linked_list_to_list


def test___init__() -> None:
    """Test __init__ function."""
    solution = Solution()

    test_1_expected = [1, 4, 2, 3]
    test_1_input = create_singly_linked_list([1, 2, 3, 4])
    solution.reorderList(test_1_input)
    assert singly_linked_list_to_list(test_1_input) == test_1_expected

    test_2_input = create_singly_linked_list([1, 2, 3, 4, 5])
    test_2_expected = [1, 5, 2, 4, 3]
    solution.reorderList(test_2_input)
    assert singly_linked_list_to_list(test_2_input) == test_2_expected
