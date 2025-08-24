from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        time: O(n^2)
        space: O(n^2)
        approach: hash set
        """

        cols: dict[int, set] = defaultdict(set)
        rows: dict[int, set] = defaultdict(set)
        squares: dict[tuple, set] = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(c // 3, r // 3)]
                ):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(c // 3, r // 3)].add(board[r][c])

        return True
