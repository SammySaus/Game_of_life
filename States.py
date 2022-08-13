import random


def dead_state(width, height):
    temp_list = [[0] * width] * height

    return temp_list


def random_state(width, height):
    state = dead_state(width, height)

    for i in range(len(state)):
        for j in range(len(state[i])):

            random_number = random.random()
            if random_number <= 0.5:
                    cell_state = 1
            else:
                    cell_state = 0
            state[i][j]=cell_state
    return state


