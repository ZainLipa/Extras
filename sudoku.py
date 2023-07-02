# Program of the Day: Sudoku Solver (Backtracking Algorithm)

def solve_sudoku(board):
    if not find_empty_cell(board):
        return True

    row, col = find_empty_cell(board)

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, row, col, num):
    return (
        not used_in_row(board, row, num) and
        not used_in_col(board, col, num) and
        not used_in_box(board, row - row % 3, col - col % 3, num)
    )

def used_in_row(board, row, num):
    for col in range(9):
        if board[row][col] == num:
            return True
    return False

def used_in_col(board, col, num):
    for row in range(9):
        if board[row][col] == num:
            return True
    return False

def used_in_box(board, start_row, start_col, num):
    for row in range(3):
        for col in range(3):
            if board[row + start_row][col + start_col] == num:
                return True
    return False

# Example usage
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Sudoku solved successfully!")
    for row in board:
        print(row)
else:
    print("No solution exists for the given Sudoku!")

