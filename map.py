import pygame as pg

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):   # Game class var created in main input as a constructor
        # Make minimap and world map attributes
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    # Method to get world map where we iterate over our array
    # and write coordinates of elements with numeric values to the dict
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    # Display map on screen
    def draw(self):
        # Iterate over world map, draw each element as unfilled square
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 50, pos[1] * 50, 50, 50), 2)
        for pos in self.world_map]