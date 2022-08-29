import copy


class Cells:
    def __init__(self):
        self.ALIVE = '#'
        self.DEAD = '-'
        self.cells = {}
        self.nextCells = {}

    def renderCells(self, width, height, definedCells):

        self.nextCells = {}
        for x in range(width):  # Loop over every possible column.
            for y in range(height):  # Loop over every possible row.
                # 50/50 chance for starting cells being alive or dead.
                self.nextCells[(x, y)] = definedCells[x][y]
                if self.nextCells[(x, y)] == 1:
                    self.nextCells[(x, y)] = self.ALIVE  # Add a living cell.
                else:
                    self.nextCells[(x, y)] = self.DEAD  # Add a dead cell.

        self.cells = copy.deepcopy(self.nextCells)
        for x in range(width):
            for y in range(height):
                print(self.cells[(x, y)], end='')  # Print the # or space.
            print()  # Print a newline at the end of the row.

    def nextstate(self, width, height):
        for x in range(width):
            for y in range(height):
                # Get the neighboring coordinates of (x, y), even if they
                # wrap around the edge:
                left = (x - 1) % width
                right = (x + 1) % width
                above = (y - 1) % height
                below = (y + 1) % height

                # Count the number of living neighbors:
                numNeighbors = 0
                if self.cells[(left, above)] == self.ALIVE:
                    numNeighbors += 1  # Top-left neighbor is alive.
                if self.cells[(x, above)] == self.ALIVE:
                    numNeighbors += 1  # Top neighbor is alive.
                if self.cells[(right, above)] == self.ALIVE:
                    numNeighbors += 1  # Top-right neighbor is alive.
                if self.cells[(left, y)] == self.ALIVE:
                    numNeighbors += 1  # Left neighbor is alive.
                if self.cells[(right, y)] == self.ALIVE:
                    numNeighbors += 1  # Right neighbor is alive.
                if self.cells[(left, below)] == self.ALIVE:
                    numNeighbors += 1  # Bottom-left neighbor is alive.
                if self.cells[(x, below)] == self.ALIVE:
                    numNeighbors += 1  # Bottom neighbor is alive.
                if self.cells[(right, below)] == self.ALIVE:
                    numNeighbors += 1  # Bottom-right neighbor is alive.

                # Set cell based on Conway's Game of Life rules:
                if self.cells[(x, y)] == self.ALIVE and (numNeighbors == 2
                                               or numNeighbors == 3):
                    # Living cells with 2 or 3 neighbors stay alive:
                    self.nextCells[(x, y)] = self.ALIVE
                elif self.cells[(x, y)] == self.DEAD and numNeighbors == 3:
                    # Dead cells with 3 neighbors become alive:
                    self.nextCells[(x, y)] = self.ALIVE
                else:
                    # Everything else dies or stays dead:
                    self.nextCells[(x, y)] = self.DEAD

        print(self.nextCells)
