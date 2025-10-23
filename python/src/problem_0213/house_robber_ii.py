class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        time: O(n)
        space: O(1)
        approach: dynamic programming
        """

        return max(
            self.helper([nums[0]]),
            self.helper(nums[1:]),
            self.helper(nums[:-1]),
        )

    def helper(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
