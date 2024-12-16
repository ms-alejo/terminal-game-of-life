# Conway's Game of Life - Terminal Implementation

This is a Python implementation of Conway's Game of Life, designed to run in a terminal. Conway's Game of Life is a cellular automaton devised by mathematician John Horton Conway. It is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input from the user.

## Features

- **Terminal-based animation**: The game runs entirely in the terminal, refreshing the grid to show each generation.

## Rules of the Game
The grid consists of cells that can be in one of two states:
- **Alive** (`■`)
- **Dead** (` `)

Each cell interacts with its eight neighbors. The rules for cell evolution are:
1. **Underpopulation**: A live cell with fewer than two live neighbors dies.
2. **Overpopulation**: A live cell with more than three live neighbors dies.
3. **Survival**: A live cell with two or three live neighbors survives.
4. **Reproduction**: A dead cell with exactly three live neighbors becomes a live cell.

## License
This project is licensed under the MIT License. See `LICENSE` for more information.

## Acknowledgments
- John Horton Conway for inventing the Game of Life.
