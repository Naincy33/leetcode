class BruteForceMatrixZeroSetter:

    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Mark rows and columns using temporary markers '#'
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # Mark row
                    for col in range(cols):
                        if matrix[i][col] != 0:
                            matrix[i][col] = '#'
                    # Mark column
                    for row in range(rows):
                        if matrix[row][j] != 0:
                            matrix[row][j] = '#'

        # Step 2: Replace markers with 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]

obj = BruteForceMatrixZeroSetter()
obj.setZeroes(matrix)

print(matrix)
