class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        flag_check = [[False for _ in range(m)] for _ in range(n)]

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return False

            if flag_check[x][y]:
                return True
            flag_check[x][y] = True
            if board[x][y] == 'X' or board[x][y] == 'T':
                return True
            flag_island = True
            if board[x][y] == 'O':
                board[x][y] = 'T'
                flag_island = dfs(x - 1, y) and flag_island
                flag_island = dfs(x + 1, y) and flag_island
                flag_island = dfs(x, y - 1) and flag_island
                flag_island = dfs(x, y + 1) and flag_island
            return flag_island

        def flip(x, y, chr='X'):
            if x < 0 or x >= n or y < 0 or y >= m:
                return
            if board[x][y] == 'T':
                board[x][y] = chr
                flip(x - 1, y, chr)
                flip(x + 1, y, chr)
                flip(x, y - 1, chr)
                flip(x, y + 1, chr)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    if dfs(i, j):
                        flip(i, j)
                    else:
                        flip(i, j, 'O')
