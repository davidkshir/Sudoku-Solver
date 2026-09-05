from solver import SudokuSolver
import time
import pyautogui

def main():
    puzzle = input("Puzzle: ") # Expects puzzle starting from top left corner
    solver = SudokuSolver(puzzle)
    if not solver.solve():
        raise ValueError("No solution found.")
    solver.print_board()
    answer = solver.board
    rows = len(answer)
    cols = len(answer[0])

    time.sleep(3)

    for row in range(rows):
        for col in range(cols):
            pyautogui.press(str(answer[row][col]))

            if col < cols - 1:
                pyautogui.press('right')

        if row < rows - 1:
            for _ in range(cols - 1):
                pyautogui.press('left')

            pyautogui.press('down')

if __name__ == '__main__':
    main()

