import sys
from pathlib import Path


# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from problem_0142.linked_list_cycle_ii import Solution
from utils.linked_lists import create_cyclic_linked_list


def test_detectCycle() -> None:
    """Test detectCycle function."""
    solution = Solution()

    # Test case 1: Cycle begins at node with value 2
    test_1_input = create_cyclic_linked_list([3, 2, 0, -4], 1)
    test_1_output = solution.detectCycle(test_1_input)
    assert test_1_output is not None
    assert test_1_output.val == 2

    # Test case 2: Cycle begins at node with value 1
    test_2_input = create_cyclic_linked_list([1, 2], 0)
    test_2_output = solution.detectCycle(test_2_input)
    assert test_2_output is not None
    assert test_2_output.val == 1

    # Test case 3: No cycle
    test_3_input = create_cyclic_linked_list([1], -1)
    test_3_output = solution.detectCycle(test_3_input)
    assert test_3_output is None
