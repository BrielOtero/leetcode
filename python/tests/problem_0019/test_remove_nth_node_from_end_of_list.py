import sys
from pathlib import Path


# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0019.remove_nth_node_from_end_of_list import Solution
from utils.linked_lists import create_singly_linked_list, singly_linked_list_to_list


def test_removeNthFromEnd() -> None:
    """Test removeNthFromEnd function."""
    solution = Solution()
    test_1_input = create_singly_linked_list([1, 2, 3, 4, 5])
    text_1_expected: list[int] = [1, 2, 3, 5]
    test_1_output = solution.removeNthFromEnd(test_1_input, 2)
    assert text_1_expected == singly_linked_list_to_list(test_1_output)

    test_2_input = create_singly_linked_list([1])
    text_2_expected: list[int] = []
    test_2_output = solution.removeNthFromEnd(test_2_input, 1)
    assert text_2_expected == singly_linked_list_to_list(test_2_output)

    test_3_input = create_singly_linked_list([1, 2])
    text_3_expected: list[int] = [1]
    test_3_output = solution.removeNthFromEnd(test_3_input, 1)
    assert text_3_expected == singly_linked_list_to_list(test_3_output)
