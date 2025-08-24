from utils.linked_lists import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        """
        time: O(n)
        space: O(1) extra space
        approach: fast and slow pointers
        """
        if not head or not head.next:
            return None

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next  # type: ignore

            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        slow = head
        while slow != fast:
            slow = slow.next  # type: ignore
            fast = fast.next  # type: ignore

        return slow
