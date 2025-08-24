class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        time: O(n)
        space: O(1)
        approach: fast and slow pointers, floyd tortoise and hare
        """
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break

        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
