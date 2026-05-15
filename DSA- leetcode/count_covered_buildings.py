class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        count = 0
        rows = {}
        cols = {}
        for building in buildings:
            r, c = building
            if r not in rows:
                rows[r] = [c, c]
            else:
                rows[r][0] = min(rows[r][0], c)
                rows[r][1] = max(rows[r][1], c)
            if c not in cols:
                cols[c] = [r, r]
            else:
                cols[c][0] = min(cols[c][0], r)
                cols[c][1] = max(cols[c][1], r)
        # print(rows)
        # print(cols)
        for building in buildings:
            x, y = building
            row, col = rows[x], cols[y]
            if row[0] < y < row[1] and col[0] < x < col[1]:
                count += 1
        
        return count
    
obj=Solution()
print(obj.countCoveredBuildings(4, [[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[2,0],[2,2]]))  # 4


'''
anytime we see a building we know that any other building
w the same x/y is covered in some direction
need quick lookup for both rows and columns -> maybe hashmap?
can lookup info in binary search method in array or we only store lowest, highest
and we can tell if this value is in between them then its covered


idea: rows {row_id : [lowest_col, highest_col]}
      cols {col_id : [lowest_row, highest_row]}
build this in O(b)

then loop through b again and for each [x,y]
to look for left right: we do rows[x][0] < x < rowx[x][1]
up down similar 

this is done in O(b)
keep track of count, increment

0 x x x
0 x x x
x 0 x 0
0 0 0 0
'''