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
