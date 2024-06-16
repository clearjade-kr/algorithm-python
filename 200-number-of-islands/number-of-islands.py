class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt_islands = 0
        n = len(grid)
        m = len(grid[0])
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == '0':
                return
            
            grid[x][y] = '0'
            for i in range(4):
                dfs(x + dx[i], y + dy[i])
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt_islands += 1
                    dfs(i, j)
                    
        return cnt_islands