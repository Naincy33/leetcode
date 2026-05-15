class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows= len(grid)
        cols= len(grid[0])
        count =0

        for i in range(rows-2):
            for j in range(cols-2):

                if grid[i+1][j+1]!= 5:
                    continue
                if self.isMagic(grid, i,j):
                    count +=1

        return count

    def isMagic(self, g, i,j):
            nums = set()

            for r in range(i, i+3):
                for c in range(j, j+3):
                    if g[r][c] < 1 or g[r][c] > 9 or g[r][c] in nums:
                        return False
                    nums.add(g[r][c])

            return (
                g[i][j] + g[i][j+1] + g[i][j+2] == 15 and
                g[i+1][j] + g[i+1][j+1] + g[i+1][j+2] == 15 and
                g[i+2][j] + g[i+2][j+1] + g[i+2][j+2] == 15 and

                g[i][j] + g[i+1][j] + g[i+2][j] == 15 and
                g[i][j+1] + g[i+1][j+1] + g[i+2][j+1] == 15 and
                g[i][j+2] + g[i+1][j+2] + g[i+2][j+2] == 15 and

                g[i][j] + g[i+1][j+1] + g[i+2][j+2] == 15 and
                g[i][j+2] + g[i+1][j+1] + g[i+2][j] == 15
            )
obj = Solution()
print(obj.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[3,7,6,1]]))