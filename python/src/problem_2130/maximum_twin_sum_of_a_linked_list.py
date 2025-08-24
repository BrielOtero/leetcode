from utils.linked_lists import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        """
        time: O(n)
        space: O(1) extra space
        approach: fast and slow pointers
        """
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next  # type: ignore
            slow.next = prev  # type: ignore
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, (slow.val + prev.val))  # type: ignore
            slow = slow.next
            prev = prev.next  # type: ignore

        return res
