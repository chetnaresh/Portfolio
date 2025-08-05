def is_valid_sudoku(board):
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            if board[i][j] != '.' and board[i][j] in row:
                return False
            row.add(board[i][j])

            if board[j][i] != '.' and board[j][i] in col:
                return False
            col.add(board[j][i])

            r = 3 * (i // 3) + j // 3
            c = 3 * (i % 3) + j % 3
            if board[r][c] != '.' and board[r][c] in box:
                return False
            box.add(board[r][c])
    return True
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(is_valid_sudoku(board))

