class Solution:
    def kClosest(self, points, k):

        points.sort(key=lambda p: p[0]**2 + p[1]**2)

        return points[:k]
# Time complexity: O(n log n) where n is the number of points, due to the sorting step
# Space complexity: O(1) if we ignore the space used for sorting, otherwise O       (n) due to the space used for sorting
solution = Solution()
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 1
print(solution.kClosest(points, k)) 