class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]

        queue = [(0, 0)]
        dp[0][0] = grid[0][0]

        while queue:
            x, y = queue.pop(0)

            for i, j in [(x + 1, y), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and dp[i][j] > dp[x][y] + grid[i][j]:
                    dp[i][j] = dp[x][y] + grid[i][j]
                    queue.append((i, j))

        return dp[-1][-1]