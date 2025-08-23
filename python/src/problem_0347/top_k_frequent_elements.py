"""
[347] Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:


        1 <= nums.length <= 105
        -104 <= nums[i] <= 104
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.



Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Difficulty: Medium
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        time: O(n)
        space: (n) extra memory
        approach: bucket sort
        """

        count: dict[int, int] = {}
        freq: list[list[int]] = [[] for i in range(len(nums) + 1)]
        res: list[int] = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key, cnt in count.items():
            freq[cnt].append(key)

        for i in reversed(range(len(freq))):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res  # Is not necessary
