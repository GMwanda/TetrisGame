import pygame

from Blocks import *
from GridClass import grids_class

pygame.init()

# GAME VARIABLES
WIDTH = 400
HEIGHT = 600
timer = pygame.time.Clock()
fps = 60
dark_blue = (44, 44, 140)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

game_grid = grids_class()
game_grid.draw_grid()

lblock = LBlock()
jblock = JBlock()


def game_loop():
    running = True
    while running:
        timer.tick(fps)
        screen.fill(dark_blue)
        game_grid.draw(screen)
        # lblock.draw(screen)
        jblock.draw(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()


game_loop()
