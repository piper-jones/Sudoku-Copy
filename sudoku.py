
import pygame

from board import Board

pygame.init()
from variables import *

screen = pygame.display.set_mode((900, 900))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board = Board(900, 900, screen, 1)
    board.draw()

    pygame.display.flip()

pygame.quit()