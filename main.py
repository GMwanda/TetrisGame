import pygame

from GameClass import game_class

pygame.init()

# GAME VARIABLES
WIDTH = 300
HEIGHT = 600
timer = pygame.time.Clock()
fps = 60
dark_blue = (44, 44, 140)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

game = game_class()

game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 500)


def game_loop():
    running = True
    while running:
        timer.tick(fps)
        screen.fill(dark_blue)

        game.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                if event.key == pygame.K_UP:
                    game.rotate()

            if event.type == game_update:
                game.move_down()

        pygame.display.flip()
        pygame.display.update()

    pygame.quit()


game_loop()
