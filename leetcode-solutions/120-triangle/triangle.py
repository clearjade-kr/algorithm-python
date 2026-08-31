class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []

        for i in range(len(triangle)):
            dp.append([0] * len(triangle[i]))

        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, len(triangle[i]) - 1):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
            dp[i][-1] = dp[i - 1][-1] + triangle[i][-1]
        
        return min(dp[-1])
