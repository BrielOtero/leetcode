class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        time: O(n^2)
        space: O(1)
        approach: two pointers
        """

        res = 0

        for center in range(len(s)):
            res += self.expandAroundCenter(s, center, center)
            res += self.expandAroundCenter(s, center, center + 1)

        return res

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1

        return res
