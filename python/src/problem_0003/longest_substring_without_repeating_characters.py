class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        time: O(n)
        space: O(m), where m is unique elements
        approach: sliding window
        """

        left, length = 0, 0
        mp: dict[str, int] = {}

        for r in range(len(s)):
            if s[r] in mp:
                left = max(left, mp[s[r]] + 1)

            mp[s[r]] = r
            length = max(length, r - left + 1)

        return length
