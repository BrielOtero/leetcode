class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        time: O(n)
        space: O(1)
        approach: two pointers
        """

        def alpha_num(c: str) -> bool:
            return (
                ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            )

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not alpha_num(s[left]):
                left += 1
            while right > left and not alpha_num(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
