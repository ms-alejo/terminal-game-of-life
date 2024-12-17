import random
import time

# constants
DEAD = 0
ALIVE = 1


# returns a board state specified with width and height and all cells are DEAD
def dead_state(width, height):
    # underscores are placeholders
    return [[DEAD for _ in range(height)] for _ in range(width)]


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
# # sample_random = random_state(30, 30)
# render(sample_random)

"""
Rules:
1. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
"""


def next_cell_value(coordinates, state):
    width = len(state)
    height = len(state[0])
    x = coordinates[0]
    y = coordinates[1]
    neighbors = 0

    # count neighbors
    for i in range((x - 1), (x + 1) + 1):
        if i < 0 or i >= width:
            continue  # stay inbounds

        for j in range((y - 1), (y + 1) + 1):
            if j < 0 or j >= height:
                continue

            if i == x and j == y:
                continue  # don't count itself

            if state[i][j] == ALIVE:
                neighbors += 1

    # determine next cell state
    if state[x][y] == ALIVE:
        if neighbors <= 1:
            return DEAD
        elif neighbors > 3:
            return DEAD
        else:
            return ALIVE
    else:
        if neighbors == 3:
            return ALIVE
        else:
            return DEAD


def next_board_state(initial_board_state):
    width = len(initial_board_state)
    height = len(initial_board_state[0])

    # initialize new state to avoid overwriting old values while processing
    new_state = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            new_state[x][y] = next_cell_value((x, y), initial_board_state)

    return new_state


def run(state):
    next_state = state

    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.03)


if __name__ == "__main__":
    initial_state = random_state(100, 200)
    run(initial_state)
