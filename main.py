import pygame

from ColorsClass import color_class
from GameClass import game_class

pygame.init()

# GAME VARIABLES
WIDTH = 500
HEIGHT = 620
timer = pygame.time.Clock()
fps = 60

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, color_class.white)
next_surface = title_font.render("Next", True, color_class.white)
game_over_surface = title_font.render("GAME OVER", True, color_class.white)
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

game = game_class()

game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 200)


def game_loop():
    running = True
    while running:
        timer.tick(fps)
        screen.fill(color_class.dark_blue)

        game.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate()
                if game.game_over == True:
                    game.game_over = False
                    game.reset()

            if event.type == game_update and game.game_over == False:
                game.move_down()

        score_value_surface = title_font.render(str(game.score), True, color_class.white)
        pygame.draw.rect(screen, color_class.light_blue, score_rect, 0, 10)
        pygame.draw.rect(screen, color_class.light_blue, next_rect, 0, 10)

        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))

        screen.blit(score_value_surface,
                    score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))

        if game.game_over:
            screen.blit(game_over_surface, (320, 450, 50, 50))

        game.draw(screen)
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()


game_loop()
