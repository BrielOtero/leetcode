class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        time: O(n)
        space: O(1) extra memory
        approach: two pointers
        """

        # width x height = area

        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return res
