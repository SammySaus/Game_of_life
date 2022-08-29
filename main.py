import States
import Views

width = 3
height = 3

# print(States.random_state(width, height))
start_state = [[0, 0, 1],
              [0, 1, 1],
              [0, 0, 0]]
conway = States.Cells()
States.Cells.renderCells(conway, width, height, start_state)
States.Cells.nextstate(conway, width, height)


