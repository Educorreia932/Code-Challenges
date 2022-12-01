import functools
import operator
import matplotlib.pyplot as plt
import numpy

from mpl_toolkits.mplot3d import Axes3D

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        return [line.replace("#", "1").replace(".", "0") for line in f.read().split("\n")]

def combinations(elements, prefix, n, k): 
    """Get all possible combinations of n elements with repetition"""
    result = []

    if k == 0: 
        return prefix

    for i in range(n): 
        new_prefix = prefix + [elements[i]]

        result.append(combinations(elements, new_prefix, n, k - 1))

    return result

class Grid:
    """Class that represents the grid"""

    def __init__(self, grid, dimension: int):
        self.dimension = dimension
        self.grid = numpy.array(grid)

        # Get all possible directions as offsets in the axis
        self.directions = combinations([-1, 0, 1], [], 3, dimension) 

        # Two level flatten of directions list 
        for _ in range(dimension - 1):
            self.directions = functools.reduce(operator.iconcat, self.directions, [])

        self.directions.remove([0] * dimension)

    def __str__(self):
        return "\n" + str(self.grid)

    def neighbors(self, coordinates):
        """Returns the number of active neighbors of a cell""" 
        active = 0

        for direction in self.directions:
            neighbor_coordinates = numpy.add(coordinates, direction)

            for i, coordinate in enumerate(neighbor_coordinates):
                if coordinate < 0 or coordinate >= self.grid.shape[i]:
                    break

            else:
                active += self.grid[tuple(neighbor_coordinates)]

        return active
    
    def grow(self):
        for i, shape in enumerate(self.grid.shape):
            self.grid = numpy.insert(self.grid, 0, numpy.zeros(1), axis=i) 
            self.grid = numpy.insert(self.grid, shape + 1, numpy.zeros(1), axis=i) 

    def step(self):
        """Generate next cycle"""
        self.grow()

        next_round = numpy.copy(self.grid)

        for i in range(self.grid.size):
            coordinates = numpy.unravel_index(i, self.grid.shape)
            active = self.neighbors(coordinates)

            # Cube is active
            if self.grid[coordinates] == 1 and (active < 2 or active > 3):
                next_round[coordinates] = 0

            # Cube is inactive
            elif self.grid[coordinates] == 0 and active == 3:
                next_round[coordinates] = 1

        self.grid = next_round

    def save(self, filename):
        """Save the grid's picture"""
        x, y, z = self.grid.nonzero()

        fig = plt.figure()

        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, marker=r'$\#$', s=[40])

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')

        plt.savefig(f"{filename}.png")

def part_1(lines):
    grid = [[[int(x)] for x in list(line)] for line in lines]
    grid = Grid(grid, 3)

    for _ in range(6):
        grid.step()

    return numpy.count_nonzero(grid.grid == 1)

def part_2(lines):
    grid = [[[[int(x)]] for x in list(line)] for line in lines]
    grid = Grid(grid, 4)

    for _ in range(6):
        grid.step()

    return numpy.count_nonzero(grid.grid == 1)

lines = read_file()

print(f"Part 1: {part_1(lines)}")
print(f"Part 2: {part_2(lines)}")
