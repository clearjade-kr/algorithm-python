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
        v = [[0 for i in range(c)] for j in range(r)]

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