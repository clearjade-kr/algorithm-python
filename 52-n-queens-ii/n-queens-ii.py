class Solution:
    def totalNQueens(self, n: int) -> int:

        res = 0
        board = [[0] * n for _ in range(n)]

        def dfs(cur_row, cnt_queens):
            nonlocal res
            if cnt_queens == n:
                res += 1
                return

            if cur_row >= n:
                return

            for x in range(cur_row, n):
                for y in range(n):
                    if board[x][y] > 0:
                        continue

                    check_board(x, y, 1)
                    dfs(x + 1, cnt_queens + 1)
                    check_board(x, y, -1)

        def check_board(x, y, val):
            board[x][y] += val
            n = len(board) - 1
            for i in range(x + 1, n + 1):
                board[i][y] += val

            right_min = min(n-x, n-y)
            for i in range(right_min):
                board[x + 1 + i][y + 1 + i] += val

            left_min = min(n-x, y)
            for i in range(left_min):
                board[x + 1 + i][y - 1 - i] += val

        dfs(0, 0)
        return res
