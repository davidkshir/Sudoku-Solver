puzzle = '020040800003001050801706349005009102210008064000060500560913400042600010107000603'
answer = '926345871473891256851726349685479132219538764734162598568913427342687915197254683'

class SudokuEngine:
    """Sudoku puzzle solving engine class."""
    def __init__(self, puzzle_str: str):
        self.puzzle_str = puzzle_str
        self.answer = answer
        self.board = []

        # convert puzzle string into matrix called board
        for i in range(0, 81, 9):
            row = [int(char) for char in puzzle_str[i:i+9]]
            self.board.append(row)

    def solve_col(self, col_index: int):
        pass

    def solve_row(self, row_index: int):
        pass

    def solve_box(self, box_index: int):
        pass

    def solve(self):
        pass



puzzle = SudokuEngine(puzzle)
print(puzzle.board)










