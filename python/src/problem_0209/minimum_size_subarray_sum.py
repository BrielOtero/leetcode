class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        time: O(n)
        space: O(1)
        approach: sliding window variable size
        """

        length = float("inf")
        curr_sum = 0
        left = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                length = min(length, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if length == float("inf") else int(length)
