from utils.linked_lists import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        """
        time: O(n)
        space: O(1) extra space
        approach: fast and slow pointers
        """

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next  # type: ignore
            if fast == slow:
                return True

        return False
