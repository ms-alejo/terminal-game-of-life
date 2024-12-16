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

# for testing
# width = 5
# height = 5


# returns a board state specified with width and height and all cells are DEAD
def dead_state(width, height):
    return [
        [DEAD for _ in range(width)] for _ in range(height)
    ]  # underscores are placeholders


# print("dead state: ", dead_state(width, height))


# makes a board state that randomly initialize cells from DEAD or Alive
def random_state(width, height):
    # initialize board size
    state = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            if random.random() >= 0.5:
                cell_state = DEAD
            else:
                cell_state = ALIVE
            state[x][y] = cell_state

    return state


# print("random state: ", random_state(width, height))


# format the board state and print it to the terminal
def render(board_state):
    width = len(board_state)
    height = len(board_state[0])

    symbols = {DEAD: " ", ALIVE: "\u2588"}

    lines = []
    for y in range(0, height):
        line = ""
        for x in range(0, width):
            line += symbols[board_state[x][y]] * 2
        lines.append(line)
    print("\n".join(lines))


# sample_dead = dead_state(30, 30)
# render(sample_dead)
sample_random = random_state(30, 30)
render(sample_random)
