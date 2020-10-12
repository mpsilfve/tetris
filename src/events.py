import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_q

def get_event(events):
    for event in events:
        if pygame.event.event_name(event.type) == "KeyDown":
            return event
    return None

def handle_events(events,grid):
    event = get_event(events)

    if event:
        if event.key == K_LEFT:
            grid.block.move_x(-1)
        elif event.key == K_RIGHT:
            grid.block.move_x(1)
        elif event.key == K_UP:
            grid.block.rotate(-1)
        elif event.key == K_SPACE:
            grid.drop()
        elif event.key == K_q:
            return False

    return True
