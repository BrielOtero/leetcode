import sys
from pathlib import Path

# Add src to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

import pytest
from utils.linked_lists import create_singly_linked_list, create_cyclic_linked_list, singly_linked_list_to_list, ListNode


def test_create_singly_linked_list() -> None:
    """Test create_singly_linked_list function."""
    # Test basic list
    head = create_singly_linked_list([1, 2, 3])
    assert head is not None
    assert head.val == 1
    assert head.next is not None
    assert head.next.val == 2
    assert head.next.next is not None
    assert head.next.next.val == 3
    assert head.next.next.next is None

    # Test single element list
    head = create_singly_linked_list([1])
    assert head is not None
    assert head.val == 1
    assert head.next is None

    # Test empty list
    head = create_singly_linked_list([])
    assert head is None


def test_create_cyclic_linked_list() -> None:
    """Test create_cyclic_linked_list function."""
    # Test basic cyclic list with pos = 1
    head = create_cyclic_linked_list([3, 2, 0, -4], 1)
    assert head is not None
    assert head.val == 3
    assert head.next is not None
    assert head.next.val == 2
    assert head.next.next is not None
    assert head.next.next.val == 0
    assert head.next.next.next is not None
    assert head.next.next.next.val == -4
    # Check that the cycle is created (tail points to node at index 1)
    assert head.next.next.next.next is head.next

    # Test cyclic list with pos = 0
    head = create_cyclic_linked_list([1, 2], 0)
    assert head is not None
    assert head.val == 1
    assert head.next is not None
    assert head.next.val == 2
    # Check that the cycle is created (tail points to head)
    assert head.next.next is head

    # Test single element list with cycle (pos = 0)
    head = create_cyclic_linked_list([1], 0)
    assert head is not None
    assert head.val == 1
    # Check that the cycle is created (node points to itself)
    assert head.next is head

    # Test empty list
    head = create_cyclic_linked_list([], 0)
    assert head is None


def test_singly_linked_list_to_list() -> None:
    """Test singly_linked_list_to_list function."""
    # Test basic list
    head = create_singly_linked_list([1, 2, 3])
    result = singly_linked_list_to_list(head)
    assert result == [1, 2, 3]

    # Test single element list
    head = create_singly_linked_list([1])
    result = singly_linked_list_to_list(head)
    assert result == [1]

    # Test empty list
    result = singly_linked_list_to_list(None)
    assert result == []


def test_linked_list_conversion_roundtrip() -> None:
    """Test that converting from list to linked list and back gives the same list."""
    # Test with various lists
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3, 4, 5],
        [-1, -2, -3],
        [0, 0, 0],
        [1, -1, 2, -2, 3, -3]
    ]

    for test_list in test_cases:
        head = create_singly_linked_list(test_list)
        result = singly_linked_list_to_list(head)
        assert result == test_list
