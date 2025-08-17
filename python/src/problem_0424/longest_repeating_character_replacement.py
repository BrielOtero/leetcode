"""
[424] Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


Example 1:


Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.


Example 2:


Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:


	1 <= s.length <= 105
	s consists of only uppercase English letters.
	0 <= k <= s.length

Difficulty: Medium
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        time: O(n)
        memory: O(m), m is total number of unique characters in the string
        approach: sliding window
        """
        left, max_f, res = 0, 0, 0
        count: dict[str, int] = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])

            while (r - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, r - left + 1)

        return res
