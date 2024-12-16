"""
1. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
"""

import random

# constants
DEAD = 0
ALIVE = 1

# variables
# board_state = [][]  # holds board state

# for testing
width = 5
height = 5


# returns a board state specified with width and height and all cells are DEAD
def dead_state(width, height):
    return [
        [DEAD for _ in range(width)] for _ in range(height)
    ]  # underscores are placeholders


print("dead state: ", dead_state(width, height))


# makes a board state that randomly initialize cells from DEAD or Alive
def random_state(width, height):
    # initialize board size
    state = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            if random.random() >= 0.75:
                cell_state = DEAD
            else:
                cell_state = ALIVE
            state[x][y] = cell_state

    return state


print("random state: ", random_state(width, height))
