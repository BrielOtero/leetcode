class Solution:
    def trap(self, height: list[int]) -> int:
        """
        time: O(n)
        space: O(1) extra memory
        approach: two pointers
        """

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        res = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                res += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res += max_right - height[right]

        return res
