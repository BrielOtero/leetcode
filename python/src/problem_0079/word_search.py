class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        time: O(m * 4^n)
        space: O(n)
        approach: backtracking
        """
        rows, cols = len(board), len(board[0])
        path: set[tuple[int, int]] = set()

        def dfs(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True

            if (
                min(row, col) < 0
                or row >= rows
                or col >= cols
                or word[index] != board[row][col]
                or (row, col) in path
            ):
                return False

            path.add((row, col))

            res = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )
            path.remove((row, col))
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
