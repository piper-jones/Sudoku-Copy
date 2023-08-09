import pygame
class Cell:
    # Constructor for the Cell class
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.sketch_val = None

    # Setter for this cell’s value
    def set_cell_value(self, value):
        self.value = value

    #  Setter for this cell’s sketched value
    def set_sketched_value(self, value):
        self.sketch_val = value

    def get_cell_at_loc(self, row, col):
        if self.row == row and self.col == col:
            return self.value
