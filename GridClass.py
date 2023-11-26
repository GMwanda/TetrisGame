import pygame

from ColorsClass import color_class

pygame.init()


class grids_class():
    def __init__(self):
        self.number_rows = 20
        self.number_cols = 10
        self.cell_size = 30
        self.grid = [[0] * (self.number_cols) for _ in range(self.number_rows)]
        self.colors = color_class.get_cell_colors()

    # def draw_grid(self):
    #     for row in range(self.number_rows):
    #         for col in range(self.number_cols):
    #             pass
    #             # print(self.grid[row][col], end=" ")
    #         # print()

    def draw(self, screen):
        for row in range(self.number_rows):
            for col in range(self.number_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cell_size + 11, row * self.cell_size + 11, self.cell_size - 1,
                                        self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def is_inside(self, row, column):
        return 0 <= row < self.number_rows and 0 <= column < self.number_cols

    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        for col in range(self.number_cols):
            if self.grid[row][col] == 0:
                return False
        return True

    def clear_row(self, row):
        for col in range(self.number_cols):
            self.grid[row][col] = 0

    def move_row_down(self, row, num_rows):
        for col in range(self.number_cols):
            self.grid[row + num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clear_full_row(self):
        completed = 0
        for row in range(self.number_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        for row in range(self.number_rows):
            for col in range(self.number_cols):
                self.grid[row][col] = 0
