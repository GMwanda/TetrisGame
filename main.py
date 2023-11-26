import pygame

pygame.init()


# GAME VARIABLES


def game_loop():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


game_loop()
