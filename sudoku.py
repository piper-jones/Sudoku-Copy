
import pygame

from board import Board
from sudoku_generator import generate_sudoku

pygame.init()
from variables import *

import sudoku_gui

def main():
    screen = pygame.display.set_mode((900, 1000))
    board = Board(900, 900, screen, 1)

    running = True
    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.click(mouseX, mouseY)
                # print(f"{mouseX} {mouseY}")

            if event.type == pygame.KEYDOWN:
                for i in range(1, 10):
                    if event.key == getattr(pygame, f"K_{i}"):
                        board.sketch(i)

                if event.key == pygame.K_RETURN:
                        if board.get_sketch() != 0:
                            board.place_number(board.get_sketch())
                            board.sketch(0)


                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    board.clear()
                elif event.key == pygame.K_LEFT:
                    board.move_selected_cell(pygame.K_LEFT)
                elif event.key == pygame.K_RIGHT:
                    board.move_selected_cell(pygame.K_RIGHT)
                elif event.key == pygame.K_UP:
                    board.move_selected_cell(pygame.K_UP)
                elif event.key == pygame.K_DOWN:
                    board.move_selected_cell(pygame.K_DOWN)
                else:
                    pass


        board.draw()
        # board.select(1,1)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    sudoku_gui.show_starter_screen()  # Call the starter screen function
    main()