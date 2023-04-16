import copy
import tkinter as tk
import numpy as np


class Cells:
    def __init__(self):
        self.ALIVE = '#'
        self.DEAD = '-'
        self.cells = {}
        self.nextCells = {}
        self.tempCells = {}
        self.statenumber = 0
        self.width = 0
        self.height = 0

    def renderCells(self, width, height, definedCells=None):
        self.width = width
        self.height = height
        self.statenumber += 1
        print("State: " + str(self.statenumber))
        if definedCells is None:
            self.cells = copy.deepcopy(self.nextCells)
        # print(definedCells)
        else:
            self.tempCells = {}
            for x in range(width):  # Loop over every possible column.
                for y in range(height):  # Loop over every possible row.
                    # 50/50 chance for starting cells being alive or dead.
                    self.tempCells[(x, y)] = definedCells[x][y]
                    if self.tempCells[(x, y)] == 1:
                        self.tempCells[(x, y)] = self.ALIVE  # Add a living cell.
                    else:
                        self.tempCells[(x, y)] = self.DEAD  # Add a dead cell.

            self.cells = copy.deepcopy(self.tempCells)
        # for x in range(width):
        #     for y in range(height):
        #         print(self.cells[(x, y)], end='')  # Print the # or space.
        #     print()  # Print a newline at the end of the row.

    def windowdisp(self):
        # Create the window, grid and labels
        window = tk.Tk()
        labels = [[None for y in range(self.height)] for x in range(self.width)]
        for x in range(self.width):
            window.grid_columnconfigure(x, minsize=20)
            for y in range(self.height):
                window.grid_rowconfigure(y, minsize=20)
                frame = tk.Frame(master=window, borderwidth=1)
                frame.grid(row=x, column=y)
                label = tk.Label(master=frame, text=self.cells[(x, y)])
                label.pack()
                labels[x][y] = label

        # Define the update function
        def update():
            Cells.nextstate(self)
            Cells.renderCells(self, self.width, self.height)
            for x in range(self.width):
                for y in range(self.height):
                    labels[x][y].configure(text=self.cells[(x, y)])
            window.after(100, update)

        update()
        window.mainloop()

    def main(self, width, height, start_state):
        Cells.renderCells(self, width, height, start_state)

        Cells.windowdisp(self)


    def nextstate(self):

        for y in range(self.height):
            for x in range(self.width):
                # Get the neighbouring coordinates of (x, y), even if they
                # wrap around the edge:
                left = (x - 1) % self.width
                right = (x + 1) % self.width
                above = (y - 1) % self.height
                below = (y + 1) % self.height

                # Count the number of living neighbours:
                numNeighbours = 0
                if self.cells[(left, above)] == self.ALIVE:
                    numNeighbours += 1  # Top-left neighbour is alive.
                if self.cells[(x, above)] == self.ALIVE:
                    numNeighbours += 1  # Top neighbour is alive.
                if self.cells[(right, above)] == self.ALIVE:
                    numNeighbours += 1  # Top-right neighbour is alive.
                if self.cells[(left, y)] == self.ALIVE:
                    numNeighbours += 1  # Left neighbour is alive.
                if self.cells[(right, y)] == self.ALIVE:
                    numNeighbours += 1  # Right neighbour is alive.
                if self.cells[(left, below)] == self.ALIVE:
                    numNeighbours += 1  # Bottom-left neighbour is alive.
                if self.cells[(x, below)] == self.ALIVE:
                    numNeighbours += 1  # Bottom neighbour is alive.
                if self.cells[(right, below)] == self.ALIVE:
                    numNeighbours += 1  # Bottom-right neighbour is alive.

                # Set cell based on Conway's Game of Life rules:
                if self.cells[(x, y)] == self.ALIVE and (numNeighbours == 2
                                                         or numNeighbours == 3):
                    # Living cells with 2 or 3 neighbours stay alive:
                    self.nextCells[(x, y)] = self.ALIVE
                elif self.cells[(x, y)] == self.DEAD and numNeighbours == 3:
                    # Dead cells with 3 neighbours become alive:
                    self.nextCells[(x, y)] = self.ALIVE
                else:
                    # Everything else dies or stays dead:
                    self.nextCells[(x, y)] = self.DEAD

        # print(self.nextCells)
