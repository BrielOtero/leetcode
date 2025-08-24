class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """
        time: O(n)
        space: O(1)
        approach: prefix sums
        """
        total = 0
        left_sum = 0

        for n in nums:
            total += n

        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
