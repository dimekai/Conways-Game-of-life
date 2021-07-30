import pygame
from cell_class import *

vec = pygame.math.Vector2

class GameWindow:
    def __init__(self, window, x, y):
        self.window = window
        self.pos = vec(x, y)
        self.width = 600
        self.height = 600
        self.CELL_SIZE = 20
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rows = self.width//self.CELL_SIZE
        self.cols = self.height//self.CELL_SIZE
        # Set up all cells in our grid in a random way
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbors(self.grid)
        self.color = {'DARK_GRAY' : (102, 102, 102)}

    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()
        

    def draw(self):
        self.image.fill(self.color['DARK_GRAY'])
        for row in self.grid:
            for cell in row:
                cell.draw()

        self.window.blit(self.image, (self.pos.x, self.pos.y))
    
        