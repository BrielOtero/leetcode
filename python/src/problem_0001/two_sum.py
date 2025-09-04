class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        time: O(n)
        space: O(n) extra space
        approach: hash map
        """
        mp: dict[int, int] = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in mp:
                return [mp[diff], i]

            mp[nums[i]] = i

        return [0, 0]  # There are always a solution, it's not needed
