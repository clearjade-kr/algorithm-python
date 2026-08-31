class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import math

        # sellTwo: the maximum profit after selling the second stock
        sellTwo = 0
        # holdTwo: the maximum profit after holding the second stock
        holdTwo = -math.inf
        # sellOne: the maximum profit after selling the first stock
        sellOne = 0
        # holdOne: the maximum profit after holding the first stock
        holdOne = -math.inf

        # Iterate through the prices
        # The order of the following four lines is important
        for price in prices:
            sellTwo = max(sellTwo, holdTwo + price)
            holdTwo = max(holdTwo, sellOne - price)
            sellOne = max(sellOne, holdOne + price)
            holdOne = max(holdOne, -price)

        return sellTwo
