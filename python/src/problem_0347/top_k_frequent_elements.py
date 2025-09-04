class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        time: O(n)
        space: (n)
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
