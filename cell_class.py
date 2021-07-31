import pygame
import random

class Cell:
    def __init__(self, window, grid_x, grid_y):
        self.alive = False
        self.window = window
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.CELL_SIZE = 20
        self.image = pygame.Surface((self.CELL_SIZE, self.CELL_SIZE))
        self.rect = self.image.get_rect()
        self.neighbors = []
        self.alive_neighbors = 0
        self.__COLORS = {'BLACK' : (0, 0, 0)
                       , 'WHITE' : (255, 255, 255)
                }
        self.current_color = self.__COLORS['BLACK']

    def update(self):
        self.rect.topleft = (self.grid_x * self.CELL_SIZE, self.grid_y * self.CELL_SIZE)

    def draw(self):
        if self.alive:
            self.image.fill(self.current_color)
        if not self.alive:
            self.image.fill(self.__COLORS['BLACK'])

            # Reference about our image window of our border
            # (pixel, pixel, size, size)
            border = (1, 1, 18, 18)
            pygame.draw.rect(self.image, self.__COLORS['WHITE'], border)
        
        self.window.blit(self.image, (self.grid_x * self.CELL_SIZE, self.grid_y * self.CELL_SIZE))
    

    def get_neighbors(self, grid):        
        neighbors_list = self.__get_neighbors()

        for neighbor in neighbors_list:
            neighbor[0] += self.grid_x
            neighbor[1] += self.grid_y
        
        # Verify value-neighbor is inside of our workspace (grid) for each cell
        for neighbor in neighbors_list:
            if neighbor[0] < 0:
                neighbor[0] += 30
            if neighbor[1] < 0:
                neighbor[1] += 30
            if neighbor[1] > 29:
                neighbor[1] -= 30
            if neighbor[0] > 29:
                neighbor[0] -= 30
        
        for neighbor in neighbors_list:
            try:
                pos_x, pos_y = neighbor[0], neighbor[1]
                self.neighbors.append(grid[pos_y][pos_x])
            except:
                print(f'Neighbor: {neighbor}')
    
    
    def count_live_neighbors(self):
        ''' Count how many neighbors are alive around of the current cell'''
        count = 0
        for neighbor in self.neighbors:
            if neighbor.alive:
                count += 1
        
        self.alive_neighbors = count


    def set_color(self):
        for cell in self.neighbors:
            if cell.current_color != self.__COLORS['BLACK']:
                self.current_color = cell.current_color
            else:
                self.current_color = self.__generate_color()


    def __get_neighbors(self):
        '''
        +----+-----+-----+
        | d1 | up  |  d3 |
        +----+-----+-----+
        |left| cen |right|
        +----+-----+-----+
        | d4 |down | d2  |
        +----+-----+-----+
        
        '''
        up_neighbor, down_neighbor = [1, 0], [-1, 0]
        left_neighbor, right_neighbor = [0, -1], [0, 1]
        d1_neighbor, d2_neighbor = [1, -1], [-1, 1]
        d3_neighbor, d4_neighbor = [1, 1], [-1, -1]

        return [d3_neighbor, d4_neighbor, d2_neighbor, d1_neighbor
             , left_neighbor, right_neighbor, up_neighbor, down_neighbor
            ]
    
    
    def __generate_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    




