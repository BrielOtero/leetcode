"""
[560] Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2


Constraints:


	1 <= nums.length <= 2 * 104
	-1000 <= nums[i] <= 1000
	-107 <= k <= 107

Difficulty: Medium
"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        time: O(n)
        space: O(n)
        approach: prefix sums
        """
        res = 0
        prefix = 0
        freq = {0: 1}

        for n in nums:
            prefix += n

            if prefix - k in freq:
                res += freq[prefix - k]

            freq[prefix] = freq.get(prefix, 0) + 1

        return res
