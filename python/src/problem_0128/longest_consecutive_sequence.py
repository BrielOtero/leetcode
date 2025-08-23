"""
[128] Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:


Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Example 2:


Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Example 3:


Input: nums = [1,0,1,2]
Output: 3



Constraints:


        0 <= nums.length <= 105
        -109 <= nums[i] <= 109

Difficulty: Medium
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        time: O(n)
        memory: O(n)
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
