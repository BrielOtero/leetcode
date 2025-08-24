class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        time: O(n)
        space: O(1) extra, O(n) for the output array
        approach: prefix sums
        """
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]

        return res
