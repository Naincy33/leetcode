class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)

        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])
# Time complexity: O(n) where n is the length of the cost list
# Space complexity: O(n) for the dp array used to store the minimum cost at each step
solution = Solution()
cost = [10, 15, 20]
print(solution.minCostClimbingStairs(cost))