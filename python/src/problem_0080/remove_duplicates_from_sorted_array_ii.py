class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        time: O(n)
        space: O(1) extra memory
        approach: two pointers
        """

        left, right = 0, 0

        while right < len(nums):
            count = 1

            while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                right += 1
                count += 1

            for _ in range(min(2, count)):
                nums[left] = nums[right]
                left += 1

            right += 1

        return left
