class Solution:
    def minCosts(self, cost):
        ans = []

        mini = float('inf')

        for x in cost:
            mini = min(mini, x)
            ans.append(mini)

        return ans
# Time complexity: O(n) where n is the length of the cost list
# Space complexity: O(n) for the ans list       
solution = Solution()
cost = [5, 3, 2, 4, 1]
print(solution.minCosts(cost))
