import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from problem_0141.linked_list_cycle import Solution
from utils.linked_lists import create_singly_linked_list, create_cyclic_linked_list


def test_has_cycle() -> None:
    """Test hasCycle function with various inputs."""
    solution = Solution()

    # Test case 1: List with cycle [3,2,0,-4], pos = 1
    test_1_input = create_cyclic_linked_list([3, 2, 0, -4], 1)
    assert solution.hasCycle(test_1_input)

    # Test case 2: List with cycle [1,2], pos = 0
    test_2_input = create_cyclic_linked_list([1, 2], 0)
    assert solution.hasCycle(test_2_input)

    # Test case 3: List without cycle [1], pos = -1
    test_3_input = create_singly_linked_list([1])
    assert not solution.hasCycle(test_3_input)

    # Additional test: Empty list
    assert not solution.hasCycle(None)

    # Additional test: Two node list without cycle
    test_4_input = create_singly_linked_list([1, 2])
    assert not solution.hasCycle(test_4_input)
