class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        time: O(n)
        space: O(n)
        approach: hash set
        """
        nums_set = set(nums)
        max_len = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                curr_len = 0
                while (n + curr_len) in nums_set:
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len
