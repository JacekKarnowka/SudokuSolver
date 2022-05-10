sudoku_to_solve = [[5,3,0,0,7,0,0,0,0],
                  [6,0,0,1,9,5,0,0,0],
                  [0,9,8,0,0,0,0,6,0],
                  [8,0,0,0,6,0,0,0,3],
                  [4,0,0,8,0,3,0,0,1],
                  [7,0,0,0,2,0,0,0,6],
                  [0,6,0,0,0,0,2,8,0],
                  [0,0,0,4,1,9,0,0,5],
                  [0,0,0,0,8,0,0,7,9]]

def check_sudoku(board, digit, row, col):

    def check_rows(board, digit, row):
        return False if digit in board[row] else True
    
    def check_columns(board, digit, col):

        return False if digit in [i[col] for i in board] else True

    def check_segment(board, digit, row, col):
        i = row - row % 3
        j = col - col % 3
        nums = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]        
        return False if digit in nums else True
       
    if (check_rows(board, digit, row) and check_columns(board, digit, col) and check_segment(board, digit, row, col)):
        return True
    else:
        return False 

def solver(board):
    
    for row in range(0, 9): # iterating over rows
        for col in range (0, 9): # iterating over columns
            
            if (board[row][col] == 0): # checking if board[row][column] is 0 
                for digit in range(1, 10): # loop over possible values from 1 to 9

                    if(check_sudoku(board, digit, row, col) == True): # check if value "digit" from loop above is correct
                        board[row][col] = digit # if value "digit" is correct, try to put value in board[row][col]
                        
                        if (solver(board) == True):
                            return True
                        else:
                            board[row][col] = 0

                return False
        
    return True

print("Sudoku board before solving: \n {}".format(sudoku_to_solve))

solved = solver(sudoku_to_solve)

print("Sudoku board after solving: \n {}".format(sudoku_to_solve))
