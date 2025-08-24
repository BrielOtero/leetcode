class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        time: O(n)
        space: O(1)
        approach: kadane's algorithm
        """
        max_sum, curr_sum = nums[0], 0

        for n in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += n
            max_sum = max(max_sum, curr_sum)

        return max_sum
