class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        dp = [0] + flowerbed + [0]

        for i in range(1, len(dp) - 1):
            if dp[i - 1] == dp[i] == dp[i + 1] == 0:
                dp[i] = 1
                n -= 1
                
        return n <= 0
