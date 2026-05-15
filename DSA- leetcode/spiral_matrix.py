"""matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]   output =[1,2,3,6,9,8,7,4,5]
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # 1) left → right (top row)
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2) top → bottom (right column)
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3) right → left (bottom row)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4) bottom → top (left column)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
# Driver code
matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
]

obj = Solution()
print(obj.spiralOrder(matrix))
