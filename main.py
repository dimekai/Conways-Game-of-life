import pygame
import sys
from game_window_class import *


WIDTH, HEIGHT = 800, 800
CELL_SIZE = 20
BACKGROUND = (199, 199, 199)
FPS = 60

running = True

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if is_mouse_on_grid(mouse_position):
                click_cell(mouse_position)


def update():
    game_window.update()


def draw():
    window.fill(BACKGROUND)
    game_window.draw()
        

def is_mouse_on_grid(mouse_position):
    is_on_grid = False
    pos_x = mouse_position[0]
    pos_y = mouse_position[1]
    if pos_x > 100 and pos_x < (WIDTH - 100):
        if pos_y > 180 and pos_y < (HEIGHT - 20):
            is_on_grid = True
    
    return is_on_grid


def click_cell(mouse_position):
    '''
    Change the state alive when you click on the cell
    '''
    mouse_x, mouse_y = mouse_position[0], mouse_position[1]
    #print(f'Click in ({mouse_x}, {mouse_y})')

    # Getting the distance that we moved the game window
    grid_position = [mouse_x - 100, mouse_y - 180]

    # It is normalized to get the real value of a cell
    grid_position[0] = grid_position[0]//CELL_SIZE
    grid_position[1] = grid_position[1]//CELL_SIZE
    grid_x, grid_y = grid_position[0], grid_position[1]

    # cell = game_window.grid[grid_y][grid_x]
    if game_window.grid[grid_y][grid_x].alive:
        game_window.grid[grid_y][grid_x].alive = False
    else:
        game_window.grid[grid_y][grid_x].alive = True
    
    

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
x, y = 100, 180
game_window = GameWindow(window, x, y)

while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()

