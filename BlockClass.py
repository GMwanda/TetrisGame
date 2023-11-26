import pygame

from ColorsClass import color_class

pygame.init()


class block_class():
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 40
        self.rotation_state = 0
        self.colors = color_class.get_cell_colors()

    def draw(self, screen):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1,
                                    self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
