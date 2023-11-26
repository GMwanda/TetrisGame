import random

from Blocks import *
from GridClass import grids_class


class game_class:
    def __init__(self):
        self.grid = grids_class()
        self.blocks = [IBlock(), TBlock(), JBlock(), OBlock(), SBlock(), ZBlock(), LBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), TBlock(), JBlock(), OBlock(), SBlock(), ZBlock(), LBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

    def move_left(self):
        self.current_block.movement(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.movement(0, 1)

    def move_right(self):
        self.current_block.movement(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.movement(0, -1)

    def move_down(self):
        self.current_block.movement(1, 0)
        if not self.block_inside() or self.block_fits() == False:
            self.current_block.movement(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_position()
        for pos in tiles:
            self.grid.grid[pos.row][pos.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full_row()

    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        return all(self.grid.is_inside(tile.row, tile.column) for tile in tiles)

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.undo_rotate()

    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
