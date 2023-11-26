import random

import pygame

pygame.init()
from Blocks import *
from GridClass import grids_class


class game_class:
    def __init__(self):
        self.grid = grids_class()
        self.blocks = [IBlock(), TBlock(), JBlock(), OBlock(), SBlock(), ZBlock(), LBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound('Sound/rotate.ogg')
        self.clear_sound = pygame.mixer.Sound('Sound/clear.ogg')

        pygame.mixer.music.load('Sound/music.ogg')
        pygame.mixer.music.play(-1)

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), TBlock(), JBlock(), OBlock(), SBlock(), ZBlock(), LBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)

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
        rows_cleared = self.grid.clear_full_row()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        return all(self.grid.is_inside(tile.row, tile.column) for tile in tiles)

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.undo_rotate()
        else:
            self.rotate_sound.play()

    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), TBlock(), JBlock(), OBlock(), SBlock(), ZBlock(), LBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 400
        elif lines_cleared == 2:
            self.score += 600
        self.score += move_down_points
