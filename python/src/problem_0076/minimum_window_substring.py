class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        time: O(n^2)
        space: O(n)
        approach: sliding window, hash map
        """

        if t == "":
            return ""

        cnt_mp: dict[str, int] = {}
        window: dict[str, int] = {}

        for letter in t:
            cnt_mp[letter] = 1 + cnt_mp.get(letter, 0)

        have, need = 0, len(cnt_mp)
        res, res_len = [-1, -1], float("infinity")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in cnt_mp and window[c] == cnt_mp[c]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in cnt_mp and window[s[left]] < cnt_mp[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left : right + 1] if res_len != float("infinity") else ""
