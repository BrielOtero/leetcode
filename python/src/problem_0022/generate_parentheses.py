class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        time: O(4^n/Sqrt(n))
        space: O(n)
        approach: dfs, stack
        """

        stack: list[str] = []
        res: list[str] = []

        def dfs(opened: int, closed: int) -> None:
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                dfs(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                dfs(opened, closed + 1)
                stack.pop()

        dfs(0, 0)

        return res
