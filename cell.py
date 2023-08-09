import pygame
class Cell:
    # Constructor for the Cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch_val = None
        self.selected = False

    # Setter for this cell’s value
    def set_cell_value(self, value):
        self.value = value

    #  Setter for this cell’s sketched value
    def set_sketched_value(self, value):
        self.sketch_val = value

    # Draws this cell, along with the value inside it.
    # If this cell has a nonzero value, that value is displayed.
    # Otherwise, no value is displayed in the cell.
    # The cell is outlined red if it is currently selected.
    def draw(self):
        cell_width= 100
        cell_height=100
        cell_x= self.col*cell_width
        cell_y=self.row*cell_height
        outline_color=pygame.color("red")
        if self.selected:
            pygame.draw.rect(self.screen, outline_color, (cell_x, cell_y, cell_width, cell_height, 3))
        if self.value !=0:
            value_font = pygame.font.Font(None, 48)
            value_text = value_font.render(str(self.value),True,(0,0,0))
            value_rect= value_text.get_rect(center=(cell_x + cell_width/2, cell_y + cell_height/2))
            self.screen.blit(value_text, value_rect)
        if self.sketch_val is not None:
            sketch_font = pygame.font.Font(None,20)
            sketch_text = sketch_font.render(str(self.sketch_val), True, (128,128,128))
            sketch_rect = sketch_text.get_rect(topleft=(cell_x +5, cell_y +5))
            self.screen.blit(sketch_text, sketch_rect)

