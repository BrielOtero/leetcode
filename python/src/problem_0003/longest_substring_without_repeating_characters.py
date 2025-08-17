"""
[3] Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.


Example 1:


Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:


Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:


Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



Constraints:


        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces.

Difficulty: Medium
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        time: O(n)
        memory: O(m), where m is unique elements
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
