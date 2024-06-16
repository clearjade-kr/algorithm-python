from typing import List


# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         n = len(board)
#         m = len(board[0])
#         flag_check = [[False for _ in range(m)] for _ in range(n)]
#
#         def dfs(x, y):
#             if x < 0 or x >= n or y < 0 or y >= m:
#                 return False
#
#             if flag_check[x][y]:
#                 return True
#             flag_check[x][y] = True
#             if board[x][y] == 'X' or board[x][y] == 'T':
#                 return True
#             flag_island = True
#             if board[x][y] == 'O':
#                 board[x][y] = 'T'
#                 flag_island = dfs(x - 1, y) and flag_island
#                 flag_island = dfs(x + 1, y) and flag_island
#                 flag_island = dfs(x, y - 1) and flag_island
#                 flag_island = dfs(x, y + 1) and flag_island
#             return flag_island
#
#         def flip(x, y, chr='X'):
#             if x < 0 or x >= n or y < 0 or y >= m:
#                 return
#             if board[x][y] == 'T':
#                 board[x][y] = chr
#                 flip(x - 1, y, chr)
#                 flip(x + 1, y, chr)
#                 flip(x, y - 1, chr)
#                 flip(x, y + 1, chr)
#
#         for i in range(n):
#             for j in range(m):
#                 if board[i][j] == 'O':
#                     if dfs(i, j):
#                         flip(i, j)
#                     else:
#                         flip(i, j, 'O')


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i, j):
            if 0 <= i < r and 0 <= j < c and board[i][j] == 'O' and not v[i][j]:
                v[i][j] = 1
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        r = len(board)
        c = len(board[0])
        v = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):
            if not v[i][0]:
                dfs(i, 0)
        for i in range(1, c):
            if not v[r - 1][i]:
                dfs(r - 1, i)
        for i in range(r - 2, -1, -1):
            if not v[i][c - 1]:
                dfs(i, c - 1)
        for i in range(c - 2, 0, -1):
            if not v[0][i]:
                dfs(0, i)
        # print(v)
        for i in range(r):
            for j in range(c):
                if v[i][j]:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


if __name__ == "__main__":
    sol = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    sol.solve(board)
    print(board)
