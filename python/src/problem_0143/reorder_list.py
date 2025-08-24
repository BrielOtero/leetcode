"""
[143] Reorder List

You are given the head of a singly linked-list. The list can be represented as:


L0 &rarr; L1 &rarr; &hellip; &rarr; Ln - 1 &rarr; Ln


Reorder the list to be on the following form:


L0 &rarr; Ln &rarr; L1 &rarr; Ln - 1 &rarr; L2 &rarr; Ln - 2 &rarr; &hellip;


You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]


Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]



Constraints:


        The number of nodes in the list is in the range [1, 5 * 104].
        1 <= Node.val <= 1000

Difficulty: Medium
"""

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
