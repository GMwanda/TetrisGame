import pygame

from ColorsClass import color_class

pygame.init()


class grids_class():
    def __init__(self):
        self.number_rows = 20
        self.number_cols = 10
        self.cell_size = 40
        self.grid = [[0] * (self.number_cols) for _ in range(self.number_rows)]
        self.colors = color_class.get_cell_colors()

    def draw_grid(self):
        for row in range(self.number_rows):
            for col in range(self.number_cols):
                print(self.grid[row][col], end=" ")
            print()

    def draw(self, screen):
        for row in range(self.number_rows):
            for col in range(self.number_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cell_size + 1, row * self.cell_size + 1, self.cell_size - 1,
                                        self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
