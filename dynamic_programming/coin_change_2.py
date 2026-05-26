class Solution:
    def change(self, amount, coins):
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
# Time complexity: O(amount * n) where n is the number of coins, due to the nested loops
# Space complexity: O(amount) due to the dp array
solution = Solution()
amount = 5
coins = [1, 2, 5]
print(solution.change(amount, coins))   