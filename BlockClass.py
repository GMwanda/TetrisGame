import pygame

from ColorsClass import color_class
from PositionClass import position_class

pygame.init()


class block_class():
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = color_class.get_cell_colors()
        self.row_offset = 0
        self.column_offset = 0

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_position()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + offset_x, tile.row * self.cell_size + offset_y,
                                    self.cell_size - 1,
                                    self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

    def movement(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = position_class(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)

        return moved_tiles

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotate(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1
