import pygame

from constants import *

# The main surface where everything is drawn. 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_shadow(x,y,screen):
    pygame.draw.rect(screen,SHADOW_COLOR,
                     pygame.Rect(x*CELL_DIM,
                                 y*CELL_DIM,
                                 CELL_DIM,
                                 HEIGHT))

def draw_cell(color, x, y, screen):
    dark_bg_color = [int(c*0.8) for c in color]
    light_bg_color = [int(c*1.2) for c in color]
    pygame.draw.rect(screen, dark_bg_color, 
                     pygame.Rect(x * CELL_DIM, 
                                 y * CELL_DIM, 
                                 CELL_DIM,
                                 CELL_DIM))
    pygame.draw.polygon(screen,
                        light_bg_color,
                        [(x * CELL_DIM,y * CELL_DIM),
                         ((x+1) * (CELL_DIM),y * CELL_DIM),
                         ((x+1) * CELL_DIM,(y+1) * CELL_DIM)])

    pygame.draw.rect(screen, color, 
                     pygame.Rect(x * CELL_DIM + 3, 
                                 y * CELL_DIM + 3, 
                                 CELL_DIM - 6,
                                 CELL_DIM - 6))

def draw(grid):
    if grid.no_draw:
        return

    if pygame.time.get_ticks() - grid.prev_level_up < 300:
        screen.fill(ACTIVE_BLOCK_COLOR)
    else:
        screen.fill(BG_COLOR)        

    for x, y in grid.block.get_cells():
        draw_shadow(x,y,screen)
    for x, y in grid.block.get_cells():
        draw_cell(ACTIVE_BLOCK_COLOR,x,y,screen)
    for layer in grid.layers:
        for x, y in layer.get_cells():
            if layer.is_full():
                draw_cell(FULL_LAYER_COLOR,x,y,screen)
            else:
                draw_cell(LAYER_COLOR,x,y,screen)
    if grid.game_over:
        grid.no_draw = True
        screen.blit(GAME_OVER,(25,250))

    pygame.display.flip()

