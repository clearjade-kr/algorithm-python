from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        cur_profit = 0

        for val in prices:
            if cur_min > val:
                cur_min = val
            elif val - cur_min > cur_profit:
                cur_profit = val - cur_min

        return cur_profit


if __name__ == "__main__":
    sol = Solution()
    prices = []
    sol.maxProfit(prices)
