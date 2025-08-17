import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0876.middle_of_the_linked_list import Solution
from utils.linked_lists import create_singly_linked_list, singly_linked_list_to_list


def test_middle_node() -> None:
    """Test middleNode function."""
    solution = Solution()

    # Test case 1: [1,2,3,4,5] => [3,4,5]
    test_1_input = create_singly_linked_list([1, 2, 3, 4, 5])
    test_1_expected = [3, 4, 5]
    result_1 = solution.middleNode(test_1_input)
    assert singly_linked_list_to_list(result_1) == test_1_expected

    # Test case 2: [1,2,3,4,5,6] => [4,5,6]
    test_2_input = create_singly_linked_list([1, 2, 3, 4, 5, 6])
    test_2_expected = [4, 5, 6]
    result_2 = solution.middleNode(test_2_input)
    assert singly_linked_list_to_list(result_2) == test_2_expected
