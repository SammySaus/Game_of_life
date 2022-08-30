import copy


class Cells:
    def __init__(self):
        self.ALIVE = '#'
        self.DEAD = '-'
        self.cells = {}
        self.nextCells = {}
        self.tempCells = {}
        self.statenumber = 0

    def renderCells(self, width, height, definedCells=None):
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
        for x in range(width):
            for y in range(height):
                print(self.cells[(x, y)], end='')  # Print the # or space.
            print()  # Print a newline at the end of the row.

    def nextstate(self, width, height):
        for y in range(height):
            for x in range(width):
                # Get the neighbouring coordinates of (x, y), even if they
                # wrap around the edge:
                left = (x - 1) % width
                right = (x + 1) % width
                above = (y - 1) % height
                below = (y + 1) % height

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
