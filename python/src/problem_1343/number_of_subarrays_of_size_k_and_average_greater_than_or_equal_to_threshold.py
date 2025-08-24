class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        """
        time: O(n)
        space: O(1)
        approach: sliding window
        """

        curr_sum = 0
        threshold *= k
        res = 0

        for right in range(len(arr)):
            curr_sum += arr[right]

            if right >= k - 1:
                res += curr_sum >= threshold
                curr_sum -= arr[right - k + 1]

        return res
