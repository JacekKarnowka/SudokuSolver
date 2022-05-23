class sudoku_board:
    def __init__(self, file_name):
        # Load sudoku board from "Sudoku_to_solve.txt" file
        try:
            with open(file_name) as f:
                lines = f.readlines()

        except FileNotFoundError:
            raise Exception("File not found!")
        
        try:
            
            rows = [i.split("\n")[0] for i in lines]

            sudoku = [[int(j) for j in i.split(",")] for i in rows]

            for check_rows in rows:
                if len(check_rows) != 17:
                    raise Exception("Wrong lenght of data")

            if len(sudoku) != 9:
                raise Exception("Wrong lenght of data!")
                
            

            self.board = sudoku


        except Exception as err:
            print("Error: {}".format(err))
            return None

    # Print board function
    def print_board(self):
        for row in self.board:
            print("{}".format(row))

    def check_sudoku(self, digit, row, col):

        if (
            self.check_rows(digit, row)
            and self.check_columns(digit, col)
            and self.check_segment(digit, row, col)
        ):
            return True
        else:
            return False

    def check_rows(self, digit, row):
        return False if digit in self.board[row] else True

    def check_columns(self, digit, col):
        return False if digit in [i[col] for i in self.board] else True

    def check_segment(self, digit, row, col):
        i = row - row % 3
        j = col - col % 3
        nums = (
            self.board[i][j : j + 3]
            + self.board[i + 1][j : j + 3]
            + self.board[i + 2][j : j + 3]
        )

        return False if digit in nums else True

    # Backtracking algorithm solver
    def solver(self):

        for row in range(0, 9):  # iterating over rows
            for col in range(0, 9):  # iterating over columns

                if self.board[row][col] == 0:  # checking if board[row][column] is 0
                    for digit in range(1, 10):  # loop over possible values from 1 to 9

                        if (
                            self.check_sudoku(digit, row, col) == True
                        ):  # check if value "digit" from loop above is correct

                            self.board[row][
                                col
                            ] = digit  # if value "digit" is correct, try to put value in board[row][col]

                            if self.solver() == True:  # backtrack for another field
                                return True
                            else:
                                self.board[row][
                                    col
                                ] = 0  # if solution is wrong, back to previous empty field

                    return False

        return True



