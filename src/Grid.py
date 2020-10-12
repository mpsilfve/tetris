import pygame

from Block import Block, Layer
from graphics import GRID_WIDTH, GRID_HEIGHT

def get_height(cells):
    return min([y for x,y in cells])

class Grid:
    def __init__(self):
        self.height = int(GRID_HEIGHT)
        self.width = int(GRID_WIDTH)
        self.level = 2
        self.prev_level_up = -1
        self.prev_advance = -1
        self.game_over = False
        self.no_draw = False
        self.layers = []
        self.next_block()
    
    def level_up(self):
        self.prev_level_up = pygame.time.get_ticks()
        self.level += 1

    def next_block(self):
        if self.game_over:
            return
        self.block = Block.get_random_block(self)

    def clashes(self,cells):
        if cells == []:
            return False

        cells = set(cells)
        for layer in self.layers:
            if cells.intersection(layer.get_cells()):
                return True

        if max([y for x,y in cells]) >= self.height:
            return True

        if max([x for x,y in cells]) >= self.width:
            return True

        if min([x for x,y in cells]) < 0:
            return True

        return False

    def advance(self,only_layers=False):
        if self.game_over:
            return True

        for layer in self.layers:
            layer.move_y(1)

        if not only_layers:
            full_layers = len([layer for layer in self.layers if layer.is_full])
            self.layers = [layer for layer in self.layers if not layer.is_full()]
            for i in range(full_layers):
                self.advance(only_layers=True)

            self.block.move_y(1)
            if not self.block.moving:
                self.layer_insert()
                self.next_block()
                return True
        return False

    def drop(self):
        while not self.advance():
            pass

    def layer_insert(self):
        cells = self.block.get_cells()
        
        if 0 in [y for x,y in cells]:
            self.game_over = True

        block_height = get_height(cells)

        for i in range(self.height - block_height - len(self.layers)):
            self.layers.append(Layer(self,self.height - len(self.layers) - 1))

        for layer in self.layers:
            layer.add_cells(cells)
            

