# Sudoku Solver

A Python Sudoku solver that uses constraint-based candidate elimination and recursive backtracking to solve standard 9×9 Sudoku puzzles. The program can also automatically enter the completed solution into a Sudoku interface using PyAutoGUI.

## Features

- Validates Sudoku input
- Constraint-based solving
- Recursive backtracking
- Fewest-candidates heuristic for backtracking
- Automatic solution entry using PyAutoGUI

## How It Works

The solver first determines the possible values for each empty cell by checking its row, column, and 3×3 box. Cells with only one possible value are filled automatically.

If no cells can be solved directly, the solver selects the cell with the fewest possible values and attempts each candidate using recursive backtracking. If a candidate leads to an invalid state, the board is restored, and the next candidate is attempted.

Once a solution is found, PyAutoGUI can automatically enter the completed board into a Sudoku interface.

## Usage

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python main.py
```

The program expects an 81-digit puzzle string, starting from the top-left cell and proceeding row by row. Use `0` to represent empty cells.

For example:

```text
530070000600195000...
```

This repository does **not** include functionality for automatically extracting a puzzle from an image or website.

## Automatic Input

After entering the puzzle, focus the top-left cell of the target Sudoku interface before automatic entry begins.

By default, the program waits 3 seconds before entering the solution. This delay can be changed by modifying the `time.sleep()` call in `main.py`.

The automatic input assumes the target interface supports number entry and navigation using the arrow keys.

## Future Improvements

- Automatic puzzle extraction
