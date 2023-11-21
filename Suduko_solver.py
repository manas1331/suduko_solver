def is_valid(board, row, col, num):
    # Check if the number is not present in the same row, column, or 3x3 grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True
# Tells about the empty locations
def find_empty_location(board, empty_loc):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                empty_loc[0], empty_loc[1] = row, col
                return True
    return False

def solve_sudoku(board):
    empty_loc = [0, 0]
    # If it is not empty it returns true
    if not find_empty_location(board, empty_loc):
        return True  # All cells are filled, puzzle solved
    
    row, col = empty_loc
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True  # If this number leads to a solution
                
            board[row][col] = 0  # If not a solution, backtrack
            
    return False

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

# Get input from the user to initialize the Sudoku puzzle
sudoku_board = []
print("Enter the Sudoku puzzle (0 for empty cells, row by row) by providing space between the numbers:")
for i in range(9):
    row = list(map(int, input().split()))
    sudoku_board.append(row)

if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print_sudoku(sudoku_board)
else:
    print("No solution exists.")
