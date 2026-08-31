class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        import math
        list_dp = [[0, -math.inf] for _ in range(k)]

        for price in prices:
            for i in range(k):
                list_dp[i][1] = max(list_dp[i][1], list_dp[i - 1][0] - price if i > 0 else -price)
                list_dp[i][0] = max(list_dp[i][0], list_dp[i][1] + price)

        return list_dp[-1][0] if k > 0 else 0
