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
    return len(state[0])
