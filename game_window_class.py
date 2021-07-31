import pygame
import copy
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
        self.grid = self.__generate_grid()
        
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
    

    def reset_grid(self):
        self.grid = self.__generate_grid()
        for row in self.grid:
            for cell in row:
                cell.get_neighbors(self.grid)

    def __generate_grid(self):
        return [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]

    def evaluate(self):
        '''
        Each square has neighbors and rules that come with number of "live" neighbors.
        1. Live cell with fewer than two live neighbors, then dead cell
        2. Live cell with more than three live neighbors, then dead cell
        3. Live cell with two or three live neighbors, then live cell
        4. Live cell with three live neighbors, then live cell
        '''
        new_grid = copy.copy(self.grid)
        
        # Count how many neighbors are alive around of the current cell
        for row in self.grid:
            for cell in row:
                cell.count_live_neighbors()
        
        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbors == 2 or cell.alive_neighbors == 3:
                        new_grid[yidx][xidx].alive = True
                    if cell.alive_neighbors < 2 or cell.alive_neighbors > 3:
                        new_grid[yidx][xidx].alive = False
                else:
                    if cell.alive_neighbors == 3:
                        new_grid[yidx][xidx].alive = True

        self.grid = new_grid





            

        