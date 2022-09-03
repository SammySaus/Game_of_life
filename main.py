import States
import tkinter
import Views

width = 10
height = 10

# print(States.random_state(width, height))
start_state = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
width = 10
height = 10
conway = States.Cells()
# States.Cells.renderCells(conway, width, height, start_state)
# for i in range(0, 3):
#
#     States.Cells.nextstate(conway)
#     States.Cells.renderCells(conway, width, height)
#     States.Cells.windowdisp(conway)

if __name__ == "__main__":
    States.Cells.main(conway, width, height, start_state)

