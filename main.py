from engine import SudokuEngine
import time
import pyautogui

puzzle = input("Puzzle: ")
engine = SudokuEngine(puzzle)
engine.solve()
answer = engine.board
rows = len(answer)
cols = len(answer[0])

time.sleep(2)

for row in range(rows):
    for col in range(cols):
        pyautogui.press(str(answer[row][col]))

        if col < cols - 1:
            pyautogui.press('right')

    if row < rows - 1:
        for cell in range(cols - 1):
            pyautogui.press('left')

        pyautogui.press('down')
