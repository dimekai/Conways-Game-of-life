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

        self.color = {'BLACK' : (0, 0, 0)
                    , 'WHITE' : (255, 255, 255)
                }

    def update(self):
        self.rect.topleft = (self.grid_x * self.CELL_SIZE, self.grid_y * self.CELL_SIZE)

    def draw(self):
        if self.alive:
            self.image.fill(self.color['BLACK'])
        if not self.alive:
            self.image.fill(self.color['BLACK'])

            # Reference about our image window of our border
            # (pixel, pixel, size, size)
            border = (1, 1, 18, 18)
            pygame.draw.rect(self.image, self.color['WHITE'], border)
        self.window.blit(self.image, (self.grid_x * self.CELL_SIZE, self.grid_y * self.CELL_SIZE))
    

    def get_neighbors(self, grid):
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
        
        neighbors_list = [d3_neighbor, d4_neighbor, d2_neighbor
                        , d1_neighbor, left_neighbor, right_neighbor
                        , up_neighbor, down_neighbor
        ]

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
        ''' Count how many neighbors are alive around of the current cell '''
        count = 0
        for neighbor in self.neighbors:
            if neighbor.alive:
                count += 1
        
        self.alive_neighbors = count





