class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        time: O(n^2)
        space: O(1)
        approach: two pointers
        """

        start, max_length = 0, 0

        def expand_around_center(left: int, right: int) -> None:
            nonlocal start, max_length

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    start = left
                    max_length = current_length

                left -= 1
                right += 1

        for center in range(len(s)):
            # odd length palindrome
            expand_around_center(center, center)
            # even length palindrome
            expand_around_center(center, center + 1)

        return s[start : start + max_length]
