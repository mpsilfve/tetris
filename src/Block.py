from numpy import rot90, transpose, nonzero
from random import choice
from graphics import SHAPES

def offset(pattern,x_offset, y_offset):
    y,x = nonzero(pattern)
    x += x_offset
    y += y_offset
    return list(zip(x.tolist(),y.tolist()))

class Block:
    id = 0
    def __init__(self,pattern,grid,init_x,init_y):
        self.x = init_x
        self.y = init_y
        self.grid = grid
        self.pattern = pattern
        self.moving = True

    def move_y(self,delta_y):
        if self.moving and not self.grid.clashes(offset(self.pattern,
                                                        self.x,
                                                        self.y+delta_y)):
            self.y += delta_y
        else:
            self.moving = False

    def move_x(self,delta_x):
        if self.moving and not self.grid.clashes(offset(self.pattern,
                                                        self.x+delta_x,
                                                        self.y)):
            self.x += delta_x

    def rotate(self,dir):
        new_pattern = rot90(self.pattern) if dir else rot90(transpose(self.pattern))

        if self.moving and not self.grid.clashes(offset(new_pattern,
                                                        self.x,
                                                        self.y)):
            self.pattern = new_pattern

    def get_cells(self):
        return offset(self.pattern,self.x,self.y)

    def get_random_block(grid):
        # Spawn a block of random shape at middle of the row top in
        # the grid.
        return Block(choice(SHAPES),grid,grid.width//2 - 1,0)

class Layer(Block):
    def __init__(self,grid,init_y):
        super().__init__([[0 for i in range(grid.width)]], 
                         grid, 0, init_y)
        
    def move_y(self,delta_y):
        if not self.grid.clashes(offset(self.pattern,
                                        self.x,
                                        self.y+delta_y)):
            self.y += delta_y

    def add_cells(self,cells):
        for x,y in cells:
            if y == self.y:
                self.pattern[0][x] = 1

    def is_full(self):
        return not (0 in self.pattern[0])
