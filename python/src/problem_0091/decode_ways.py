class Solution:
    def numDecodings(self, s: str) -> int:
        """
        time: O(n)
        space: O(1)
        approach: dynamic programming
        """

        # - single: ways to decode starting at next position (i+1)
        # - double: ways to decode starting two positions ahead (i+2)
        single, double = 1, 0

        for i in reversed(range(len(s))):
            current = 0

            if s[i] != "0":
                current = single

                if i + 1 < len(s) and (
                    s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")
                ):
                    current += double

            double = single
            single = current

        return single
