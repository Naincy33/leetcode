""""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0."""

class MatrixZeroSetter:

    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
        
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Check if first row contains zero
        firstRowZero = any(matrix[0][j] == 0 for j in range(cols))

        # Step 2: Check if first column contains zero
        firstColZero = any(matrix[i][0] == 0 for i in range(rows))

        # Step 3: Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 4: Zero out rows
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        # Step 5: Zero out columns
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0

        # Step 6: Zero first row if needed
        if firstRowZero:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 7: Zero first column if needed
        if firstColZero:
            for i in range(rows):
                matrix[i][0] = 0
matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]

obj = MatrixZeroSetter()   # object banaya
obj.setZeroes(matrix)      # method call ki

print(matrix)
