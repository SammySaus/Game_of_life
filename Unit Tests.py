import numpy as np
import States

#temp_state = np.array([[0, 0, 1], [0, 1, 1], [0, 0, 0]])
temp_state = [[0, 0, 1], [0, 1, 1], [0, 0, 0]]
# print(temp_state)
# print(temp_state[0][2])
# next_state = States.next_board_state(temp_state)
# print(next_state)
States.simple_iteration(temp_state)