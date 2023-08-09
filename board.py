import pygame

from sudoku_generator import generate_sudoku as gs
from sudoku_generator import SudokuGenerator

from variables import *
from cell import Cell
import copy

pygame.init()

class Board:

    # Constructor for the Board class.
    # screen is a window from PyGame.
    # difficulty is a variable to indicate if the user chose easy, medium, or hard.
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        removed = 30
        if difficulty == 'easy':
            removed = 30
        elif difficulty == 'medium':
            removed = 40
        elif difficulty == 'hard':
            removed = 50

        self.current_board, self.original_board = gs(9, removed)
        self.selected_cell = [0, 0]

        self.locked_board = copy.deepcopy(self.current_board)
        self.temp_cells = copy.deepcopy(self.current_board)




    # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    # Draws every cell on this board.
    def draw(self):
        black = pygame.Color("black")
        white = pygame.Color("white")
        red = pygame.Color("red")
        merp_red = (160, 16, 25)
        blupe = (230, 240, 255)

        # draws indiviudal cells
        y_place = 0
        for row in range(9):
            cell_size = 100
            x_place = 0
            for col in range(9):
                pygame.draw.rect(self.screen, blupe, pygame.Rect(x_place, y_place, cell_size, cell_size))
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

        pygame.draw.rect(self.screen, red, pygame.Rect((self.selected_cell[0] * 100), (self.selected_cell[1] * 100), 100, 100), width=6)

        # draw text for permanent numbers
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 64)
        for row in range(9):
            for col in range(9):
                if self.locked_board[row][col] != 0:
                    text = font.render(str(self.current_board[row][col]), True, black, None)
                    self.screen.blit(text, (35+(100*col), 15+(100*row)))

        # draws input numbers
        for row in range(9):
            for col in range(9):
                if self.locked_board[row][col] == 0 and self.current_board[row][col] != 0:
                    text = font.render(str(self.current_board[row][col]), True, merp_red, None)
                    self.screen.blit(text, (35 + (100 * col), 15+(100 * row)))

        #draws temp number
        for row in range(9):
            for col in range(9):
                    if self.locked_board[row][col] == 0 and self.temp_cells[row][col] != 0:
                        light_grey = (150, 150, 150)
                        text = font.render(str(self.temp_cells[row][col]), True, light_grey, None)
                        self.screen.blit(text, (5 + (100 * col), (100 * row) - 5))




    # Marks the cell at (row, col) in the board as the current selected cell.
    # Once a cell has been selected, the user can edit its value or sketched value.

    def select(self, row, col):
        # red = pygame.Color("red")
        # pygame.draw.rect(self.screen, red, pygame.Rect((row * 100), (col * 100), cell_size, cell_size), width=6)
        self.selected_cell = [col, row]
        print(f"selected cell update: {self.selected_cell}")

    # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    # of the cell which was clicked. Otherwise, this function returns None.
    def click(self, x, y):
        # cells are 100x100 pixels in size
        if x or y > 901:
            row = y // 100
            col = x // 100
            print(f"selected cell check: {self.selected_cell} vs {[col, row]}")
            if self.selected_cell != [col, row]:
                self.select(row, col)
            return row, col
        return None

    # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    # filled by themselves.
    def clear(self):
        row, col = self.selected_cell
        self.current_board[col][row] = 0
            #remember to add a function to main that returns true to this statment when a key is pressed


    # Sets the value of the current selected cell equal to user entered value.
    # Called when the user presses the Enter key.
    def place_number(self, value):
        col, row = self.selected_cell
        self.current_board[row][col] = value  # Update the value in the current_board
        self.update_board()

    def sketch(self, value):
        col, row = self.selected_cell
        self.temp_cells[row][col] = value  # Update the value in the current_board
        self.update_board()

    def get_sketch(self):
        col, row = self.selected_cell
        return self.temp_cells[row][col]


    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
    def reset_to_original(self):
        self.board = self.original_board

    # Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        board = self.current_board
        for i in range(len(board)):
            for y in range(len(board[i])):
                if board[i][y] != 0:
                    continue
                else:
                    return False
        return True

    # Updates the underlying 2D board with the values in all cells.
    def update_board(self):
        # No need to create a new Cell instance here
        # Update the current_board directly
        self.current_board = self.current_board

    def update_cells(self):
        self.locked_board = self.locked_board

    # Finds an empty cell and returns its row and col as a tuple (x, y).
    def find_empty(self):
        board = SudokuGenerator.get_board()
        empty_tup = ()
        for i in board:
            for y in board[i]:
                if board[i][y] == 0:
                    empty_tup = (i, y)
                    return empty_tup


    # Check whether the Sudoku board is solved correctly.
    def check_board(self):
        board = self.current_board
        while self.is_full() is True:
            for i in board:
                for y in board[i]:
                    if board[i][y] == self.original_board[i][y]:
                        continue
                    else:
                        return False
            return True
        # don't forget to add a call of this function in main that checks if it returns true

    # move selected cell based on direction
    # direction - string based directional movement
    def move_selected_cell(self, direction):
        if direction == pygame.K_LEFT:
            self.selected_cell = ((self.selected_cell[0] - 1) % 9, self.selected_cell[1])
        elif direction == pygame.K_RIGHT:
            self.selected_cell = ((self.selected_cell[0] + 1) % 9, self.selected_cell[1])
        elif direction == pygame.K_UP:
            self.selected_cell = (self.selected_cell[0], (self.selected_cell[1] - 1) % 9)
        elif direction == pygame.K_DOWN:
            self.selected_cell = (self.selected_cell[0], (self.selected_cell[1] + 1) % 9)
            