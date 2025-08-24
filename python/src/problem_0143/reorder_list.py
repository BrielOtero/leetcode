from utils.linked_lists import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        """
        1. First we need have get a pointer in the middle of linked list using two pointers
        2. Then reverse the second part of the linked list
        3. Iterate over the first and second part and mix the nodes
        """

        """
        time: O(n)
        space: O(1)
        approach: two pointers
        """

        slow, fast = head, head.next  # type: ignore

        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

        second = slow.next  # type: ignore
        prev = slow.next = None  # type: ignore

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp_1, tmp_2 = first.next, second.next  # type: ignore
            first.next = second  # type: ignore
            second.next = tmp_1
            first, second = tmp_1, tmp_2
