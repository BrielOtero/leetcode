from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


def create_singly_linked_list(values: list[int]) -> ListNode | None:
    """Create a singly linked list from a list of values.

    Args:
        values: A list of integers to convert to a linked list.

    Returns:
        The head node of the created linked list, or None if the input list is empty.

    Example:
        >>> head = create_singly_linked_list([1, 2, 3])
        >>> singly_linked_list_to_list(head)
        [1, 2, 3]
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def create_cyclic_linked_list(values: list[int], pos: int) -> ListNode | None:
    """Create a cyclic linked list from a list of values.

    Args:
        values: A list of integers to convert to a linked list.
        pos: The index of the node that tail's next pointer connects to.
             If pos is -1, there is no cycle.

    Returns:
        The head node of the created linked list, or None if the input list is empty.
    """
    if not values:
        return None

    nodes = []
    head = ListNode(values[0])
    nodes.append(head)
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)

    # Create cycle if pos is valid
    if pos >= 0 and pos < len(nodes):
        current.next = nodes[pos]

    return head


def singly_linked_list_to_list(head: ListNode | None) -> list[int]:
    """Convert a singly linked list to a list of values.

    Args:
        head: The head node of the linked list to convert.

    Returns:
        A list of integers containing the values from the linked list nodes
        in the same order as they appear in the list.

    Example:
        >>> # Assuming we have a linked list representing [1, 2, 3]
        >>> values = singly_linked_list_to_list(head)
        >>> values
        [1, 2, 3]
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
