from collections import defaultdict
from math import prod

import re
import numpy

def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        fields = [field.split("\n") for field in f.read().split("\n\n")]
        tiles = {}
    
        for field in fields:
            tile_id = int(re.findall(r'\d+', field[0])[0])
            tile_data = numpy.array([list(line) for line in field[1:]])
            tiles[tile_id] = Tile(tile_id, tile_data)

        return tiles

class Tile:
    def __init__(self, tile_id, tile_data):
        self.id = tile_id
        self.data = tile_data
        
        borders = (
            tile_data[0, :],
            tile_data[-1, :],
            tile_data[:, 0],
            tile_data[:, -1]
        )

        borders = [tuple(border) for border in borders]

        self.borders = set(borders + [tuple(reversed(border)) for border in borders])

    def __str__(self):
        return "\n".join(["".join(line) for line in self.data])

    def __repr__(self):
        return str(self.id)

    def can_connect(self, adjacent_tile):
        return self.borders & adjacent_tile.borders

def part_1(tiles):
    corner_ids = []
    image = defaultdict(set)

    for i, tile in tiles.items():
        for j, adjacent_tile in tiles.items():
            if i != j:                                 # Different tiles
                if tile.can_connect(adjacent_tile):    # Tiles share a border
                    image[i].add(j)

        if len(image[i]) == 2:                         # Has two adjacent tiles, therefore is a corner
            corner_ids.append(i)

    return prod(corner_ids)

tiles = read_file()

print(f"Part 1: {part_1(tiles)}")
# print(f"Part 2: {part_2()}")
