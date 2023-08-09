
import pygame

from board import Board
from sudoku_generator import generate_sudoku

pygame.init()
from variables import *

screen = pygame.display.set_mode((900, 900))
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
            if event.type == pygame.K_DELETE or pygame.K_BACKSPACE:
                board.clear()
            elif event.key == pygame.K_1:
                board.place_number(1)
            elif event.key == pygame.K_2:
                board.place_number(2)
            elif event.key == pygame.K_3:
                board.place_number(3)
            elif event.key == pygame.K_4:
                board.place_number(4)
            elif event.key == pygame.K_5:
                board.place_number(5)
            elif event.key == pygame.K_6:
                board.place_number(6)
            elif event.key == pygame.K_7:
                board.place_number(7)
            elif event.key == pygame.K_8:
                board.place_number(8)
            elif event.key == pygame.K_9:
                board.place_number(9)
            else:
                pass





    board.draw()
    # board.select(1,1)

    pygame.display.flip()

pygame.quit()