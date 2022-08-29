import States
import numpy as np

temp_state = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]]
new_state = temp_state
# print(state, new_state)

neighbours = [0, 0, 0, 0]
# Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
# print((range(0, state_width(state))), (range(0, state_height(state))))
for i in range(0, States.state_height(new_state)):  # range(0, state_width(state))
    for j in range(0, States.state_width(new_state)):  # range(0, state_height(state))

        if States.checka(i):
            neighbours[0] = temp_state[i - 1][j]
            print(i-1, j)
        else:
            print('pass')


        if States.checkb(j):
            neighbours[3] = temp_state[i][j - 1]
            print(i, j-1)
        else:
            print('pass')


        if States.checkc(i, 3):
            neighbours[2] = temp_state[i + 1][j]
            print(i + 1, j)
        else:
            print('pass')


        if States.checkd(j, 3):
            neighbours[1] = temp_state[i][j + 1]
            print(i, j+1)
        else:
            print('pass')


        neighbour_match = np.sum(neighbours, dtype=np.int32)
        print(neighbours)

        if neighbour_match == 0:
            new_state[i][j] = 0
        elif neighbour_match == 1:
            new_state[i][j] = 0
        elif neighbour_match == 2:
            if temp_state[i][j] == 0:
                new_state[i][j] = 0
        elif neighbour_match == 3:
            new_state[i][j] = 1
        elif neighbour_match == 4:
            new_state[i][j] = 0
        else:
            print("Unexpected value: " + neighbour_match)
print(temp_state)
