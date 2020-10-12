from random import choice, random

import pygame

from Grid import Grid
from graphics import draw
from events import handle_events

pygame.init()
grid = Grid()

while 1:    
    events = pygame.event.get()
    # A False return value signifies quit.
    if not handle_events(events,grid):
        break

    draw(grid)

    # Sleep a bit every iteration to reduce CPU load.
    pygame.time.wait(35)

    # The current active block will fall one row downward every
    # 1/level seconds.
    if pygame.time.get_ticks() - grid.prev_advance >= 1000/grid.level:
        grid.prev_advance = pygame.time.get_ticks()
        grid.advance()
        
    # The level will increase every 50 second
    if pygame.time.get_ticks() - grid.prev_level_up >= 50000:
        grid.level_up()
