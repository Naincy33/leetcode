

class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def get_candidates(r, c):
            b = (r // 3) * 3 + (c // 3)
            return {str(x) for x in range(1, 10)} - rows[r] - cols[c] - boxes[b]

        def backtrack():
            if not empties:
                return True

            empties.sort(key=lambda x: len(get_candidates(x[0], x[1])))
            r, c = empties.pop(0)
            b = (r // 3) * 3 + (c // 3)

            for num in get_candidates(r, c):
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                if backtrack():
                    return True

                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)

            empties.insert(0, (r, c))
            return False

        backtrack()


def printBoard(board):
    for row in board:
        print(" ".join(row))


if __name__ == "__main__":
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

    solver = Solution()
    solver.solveSudoku(board)

    print("\nSolved Sudoku:\n")
    printBoard(board)
