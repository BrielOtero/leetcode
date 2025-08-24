class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        """
        time: O(n)
        space: O(1)
        approach: kadane's algorithm sliding window
        """

        left, right, res, prev = 0, 1, 1, ""

        while right < len(arr):
            if arr[right - 1] > arr[right] and prev != ">":
                res = max(res, right - left + 1)
                right += 1
                prev = ">"
            elif arr[right - 1] < arr[right] and prev != "<":
                res = max(res, right - left + 1)
                right += 1
                prev = "<"
            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
                prev = ""

        return res
