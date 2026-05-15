class Solution:
    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        if self.isValid(board, i, j, str(num)):
                            board[i][j] = str(num)

                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False  # No number fits here
        return True  # Puzzle solved

    def isValid(self, board, row, col, num):
        # Check row & column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Check 3x3 subgrid
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False

        return True
board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

obj = Solution()
obj.solveSudoku(board)

for row in board:
    print(row)
