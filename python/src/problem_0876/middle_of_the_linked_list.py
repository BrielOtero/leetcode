from utils.linked_lists import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        """
        time: O(n)
        space: O(1) extra space
        approach: fast and slow pointers
        """

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next  # type: ignore

        return slow
