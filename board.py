import pygame
pygame.init()

from sudoku_generator import SudokuGenerator
SG = SudokuGenerator()

=======
from sudoku_generator import SudokuGenerator

from variables import *
from cell import Cell

class Board:
    # Constructor for the Board class.
    # screen is a window from PyGame.
    # difficulty is a variable to indicate if the user chose easy, medium, or hard.
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None

    #Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    # Draws every cell on this board.
    def draw(self):
        black = pygame.Color("black")
        white = pygame.Color("white")

        # draws indiviudal cells
        y_place = 0
        for row in range(9):
            cell_size = 100
            x_place = 0
            for col in range(9):
                pygame.draw.rect(self.screen, white, pygame.Rect(x_place, y_place, cell_size, cell_size))
                x_place += 100
            y_place += 100


        # draws thick lines
        pygame.draw.line(self.screen, black, (0, 2), (900, 2), thick_line)
        pygame.draw.line(self.screen, black, (0, 303), (900, 303), thick_line)
        pygame.draw.line(self.screen, black, (0, 603), (900, 603), thick_line)
        pygame.draw.line(self.screen, black, (0, 897), (900, 897), thick_line)

        pygame.draw.line(self.screen, black, (2, 0), (2, 900), thick_line)
        pygame.draw.line(self.screen, black, (303, 0), (303, 900), thick_line)
        pygame.draw.line(self.screen, black, (603, 0), (603, 900), thick_line)
        pygame.draw.line(self.screen, black, (897, 0), (897, 900), thick_line)

        # draws thin lines
        location = 100
        for i in range(9):
            pygame.draw.line(self.screen, black, (0, location), (900, location), thin_line)
            pygame.draw.line(self.screen, black, (location, 0), (location, 900), thin_line)
            location += 100


    #Marks the cell at (row, col) in the board as the current selected cell.
    #Once a cell has been selected, the user can edit its value or sketched value.
    def select(self, row, col):
        self.selected_cell = SG.get_board()[row][col]


    #If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    #of the cell which was clicked. Otherwise, this function returns None.
    def click(self, x, y):
        if x and y <= 900:
            row = (y// 100)
            col = (x // 100)
            return(row, col)
        return None

    #Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    #filled by themselves.
    def clear(self):
        pass


    #Sets the sketched value of the current selected cell equal to user entered value.
    #It will be displayed at the top left corner of the cell using the draw() function.
    def sketch(self, value):
        Cell.draw()

    # Sets the value of the current selected cell equal to user entered value.
    # Called when the user presses the Enter key.
    def place_number(self, value):
        pass

    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
    def reset_to_original(self):
        pass

    # Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        pass

    # Updates the underlying 2D board with the values in all cells.
    def update_board(self):
        pass

    # Finds an empty cell and returns its row and col as a tuple (x, y).
    def find_empty(self):
        pass

    # Check whether the Sudoku board is solved correctly.
    def check_board(self):
        pass

