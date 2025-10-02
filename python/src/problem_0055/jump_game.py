class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        time: O(n)
        space: O(1)
        approach: greedy
        """

        goal = len(nums) - 1

        for i in reversed(range(len(nums))):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
