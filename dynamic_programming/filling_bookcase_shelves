class Solution:
    def minHeightShelves(self, books, shelfWidth):

        n = len(books)

        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for i in range(1, n + 1):

            width = 0
            height = 0

            for j in range(i, 0, -1):

                width += books[j - 1][0]

                if width > shelfWidth:
                    break

                height = max(height, books[j - 1][1])

                dp[i] = min(dp[i], dp[j - 1] + height)

        return dp[n]
# Time complexity: O(n^2) where n is the number of books, due to the nested loops
# Space complexity: O(n) due to the dp array
solution = Solution()
books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1]]
shelfWidth = 4
print(solution.minHeightShelves(books, shelfWidth)) 