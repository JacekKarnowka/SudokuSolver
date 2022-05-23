from Sudoku_Solver import sudoku_board

board_1 = sudoku_board("./Sudoku_to_solve.txt")

if board_1.solver():
    print("Sudoku solved!")
    board_1.print_board()
else:
    print("Sudoku unsolvable")