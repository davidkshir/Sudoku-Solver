puzzle = input("Enter puzzle string: ")

class SudokuEngine:
    """Class for Sudoku solving engine."""
    def __init__(self, puzzle_str: str, row_size: int = 9, col_size: int = 9, box_size: int = 3):
        self.puzzle_str = puzzle_str
        self.row_size = row_size
        self.col_size = col_size
        self.box_size = box_size
        self.board = []

        # convert puzzle string into 2D list called board
        for i in range(0, self.row_size * self.col_size, self.col_size):
            row = [int(char) for char in puzzle_str[i:i + self.col_size]]
            self.board.append(row)

    def solve_by_row(self, row):
        """Finds possible values for given coordinates based on the values in the row."""
        possible_row_val = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # removes any value already in row from possible values
        for num in self.board[row]:
            if num in possible_row_val:
                possible_row_val.remove(num)

        return possible_row_val

    def solve_by_col(self, col):
        """Finds possible values for given coordinates based on the values in the column."""
        possible_col_val = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # removes any value already in column from possible values
        for i in range(0, self.row_size):
            num = self.board[i][col]
            if num in possible_col_val:
                possible_col_val.remove(num)

        return possible_col_val

    def find_box(self, row, col):
        """Finds the bounds of the box of the given coordinates."""
        start_row = (row // self.box_size) * self.box_size
        start_col = (col // self.box_size) * self.box_size

        end_row = start_row + self.box_size
        end_col = start_col + self.box_size

        return start_row, start_col, end_row, end_col

    def solve_by_box(self, row, col):
        """Finds possible values for given coordinates based on the values in the box"""
        possible_box_val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        start_row, start_col, end_row, end_col = self.find_box(row, col)

        # removes any value already in box from possible values
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                if self.board[i][j] in possible_box_val:
                    possible_box_val.remove(self.board[i][j])

        return possible_box_val


    def solve(self):
        """Solves Sudoku puzzle using solve_by_row, solve_by_col, & solve_by_box methods."""

        # iterates all 3 solving methods over entire board
        while True:
            min_possible_val = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            min_row = 0
            min_col = 0
            zero_count = 0
            changed = False

            for i in range(self.row_size):
                for j in range(self.col_size):

                    # if the current index's isn't 0 skip it because it's already solved
                    if self.board[i][j] != 0:
                        continue

                    # if there is only 1 possible value the current index could be set it equal to that value
                    temp_possible_val = set(self.solve_by_row(i)) & set(self.solve_by_col(j)) & set(self.solve_by_box(i,j))
                    if len(temp_possible_val) == 0:
                        return False
                    if len(temp_possible_val) == 1:
                        self.board[i][j] = temp_possible_val.pop()
                        changed = True

                    zero_count += 1 # if neither condition happened current value must still be 0

                    if len(temp_possible_val) != 1 and len(temp_possible_val) < len(min_possible_val):
                        min_possible_val = temp_possible_val
                        min_row = i
                        min_col = j


            if zero_count == 0: # if no zeros then puzzle is solved
                return True

            if not changed: # if no changes are made backtracking is necessary to solve puzzle
                saved_board = [row[:] for row in self.board]

                # tries a random possible value for the index that had the least amount
                # if it doesn't work it restores the board and tries another, if it does
                # work it returns to solving the board like normal
                for value in min_possible_val:
                    self.board = saved_board
                    self.board[min_row][min_col] = value
                    if self.solve():
                        return True

                return False # returns false if guess didn't work so it can try a different value

    def print_board(self):
        """Prints the board of the Sudoku puzzle"""
        for row in self.board:
            print(row)


def main():
    engine = SudokuEngine(puzzle)
    engine.solve()
    engine.print_board()

if __name__ == "__main__":
    main()







