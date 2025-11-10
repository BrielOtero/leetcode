class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        time: O(n * s) where n is length of coins and s given amount
        space: O(s)
        approach: dynamic programming top-down
        """
        memo: dict[int, float] = {}

        def dfs(amount: int) -> float:
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = float("inf")

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res

        min_coins = dfs(amount)

        return -1 if min_coins == float("inf") else int(min_coins)
