from utils.linked_lists import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        time: O(n)
        space: O(1)
        approach: two pointers with dummy
        """

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next  # type: ignore
            n -= 1

        while right:
            left = left.next  # type: ignore
            right = right.next

        left.next = left.next.next  # type: ignore
        return dummy.next
