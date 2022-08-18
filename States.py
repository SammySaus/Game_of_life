import random
import numpy as np


def dead_state(width, height):
    return np.zeros((width, height))


def random_state(width, height):
    state = np.random.random((height, width))
    for i in range(0, state_width(state)):
        for j in range(0, state_width(state)):

            random_number = random.random()
            if state[i][j] <= 0.5:  # experiment with this value to increase or decrease life/death states
                cell_state = 1
            else:
                cell_state = 0
            state[i][j] = cell_state

    return state


def state_width(state):
    """Get the width of a state.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    The width of the input state
    """

    # print(len(state))
    return len(state)


def state_height(state):
    """Get the height of a state.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    The height of the input state
    """
    # print(len(state[0]))
    return len(state[0])


def next_board_state(state):
    new_state = state
    # print(state, new_state)

    neighbours = [0, 0, 0, 0]
    # Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    # print((range(0, state_width(state))), (range(0, state_height(state))))
    for i in range(0, state_width(state)):  # range(0, state_width(state))
        for j in range(0, state_height(state)):  # range(0, state_height(state))
            print(state, new_state)
            if i - 1 > -1:
                neighbours[0] = state[i - 1][j]
            # print(state)
            # print("if i-1 j", i-1, j, state[i-1][j])
            else:
                neighbours[0] = 0
            if j - 1 > -1:
                neighbours[3] = state[i][j - 1]
                # print("if i j-1")

            else:
                neighbours[3] = 0

            try:
                neighbours[1] = state[i + 1][j]
                # print("if i+1 j")

            except:
                neighbours[1] = 0
            else:
                neighbours[1] = state[i + 1][j]

            try:
                neighbours[2] = state[i][j + 1]
                # print("if i j+1")

            except:
                neighbours[2] = 0
            else:
                neighbours[2] = state[i][j + 1]

            neighbour_match = np.sum(neighbours, dtype=np.int32)

            # print(i, j, neighbour_match, neighbours, state[i][j], state[i][j])
            match neighbour_match:
                case 0:
                    new_state[i][j] = 0
                case 1:
                    new_state[i][j] = 0
                case 2:
                    if state[i][j] == 0:
                        new_state[i][j] = 0

                case 3:  # if there are 3 neighbours
                    new_state[i][j] = 1
                case 4:
                    new_state[i][j] = 0
                case other:
                    print("Unexpected value: ")
                    print(neighbour_match)
    return new_state

    # Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    # Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    # Any dead cell with exactly 3 live neighbors becomes alive, by reproduction


def simple_iteration(state):
    for i in enumerate(state):
        for j in range(len(i)):
            element = state[i][j]
            print(element)
