class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        list_coins = [float('inf')] * (amount + 1)
        list_coins[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                list_coins[i] = min(list_coins[i], list_coins[i - coin] + 1)
        
        return list_coins[amount] if list_coins[amount] != float('inf') else -1
