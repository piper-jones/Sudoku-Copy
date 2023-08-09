import pygame
from board import Board
import sys
from sudoku_generator import generate_sudoku
from variables import *
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1000
curr = 1


starter_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Screen")
sudoku_background = pygame.image.load("starter_img.webp")
sudoku_background = pygame.transform.scale(sudoku_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
game_background = pygame.image.load('sudoku_background.webp')
game_background = pygame.transform.scale(game_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Arial", 60, bold=True)
status = True
run = True
while run:

    if status:
        main_screen_status = True
        starter_text = font.render("Welcome to Sudoku!", font, (69, 16, 12))
        starter_screen.blit(sudoku_background, (0, 0))
        starter_screen.blit(starter_text, (150, 0))
        easy_text = font.render('Easy', True, 'black')
        medium_text = font.render('Medium', True, 'black')
        hard_text = font.render('Hard', True, 'black')

        easy_button = pygame.Rect(100, 200, 120, 80)
        medium_button = pygame.Rect(400, 200, 200, 80)
        hard_button = pygame.Rect(700, 200, 120, 80)

        a, b = pygame.mouse.get_pos()
        if easy_button.x <= a <= easy_button.x + 120 and easy_button.y <= b <= easy_button.y + 80:
            pygame.draw.rect(starter_screen, (180, 180, 180), easy_button)
        else:
            pygame.draw.rect(starter_screen, (110, 110, 110), easy_button)

        if medium_button.x <= a <= medium_button.x + 200 and medium_button.y <= b < medium_button.y + 60:
            pygame.draw.rect(starter_screen, (180, 180, 180), medium_button)
        else:
            pygame.draw.rect(starter_screen, (110, 110, 110), medium_button)

        if hard_button.x <= a <= hard_button.x + 110 and hard_button.y <= b <= hard_button.y + 60:
            pygame.draw.rect(starter_screen, (180, 180, 180), hard_button)
        else:
            pygame.draw.rect(starter_screen, (110, 110, 110), hard_button)

        starter_screen.blit(easy_text, (easy_button.x + 5, easy_button.y + 5))
        starter_screen.blit(medium_text, (medium_button.x + 5, medium_button.y + 5))
        starter_screen.blit(hard_text, (hard_button.x + 5, hard_button.y + 5))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and (easy_button.x <= a <= easy_button.x + 120 and easy_button.y <= b <= easy_button.y + 80):
            pygame.display.set_caption("Easy Difficulty")
            status = False
            screen = pygame.display.set_mode((900, 1000))
            screen.fill((255, 255, 255))
            board = Board(900, 900, screen, 1)
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 1000, 900, 100))
            pygame.display.flip()
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
                        if event.key == pygame.K_1:
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
                        elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
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
                mouseX, mouseY = pygame.mouse.get_pos()
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 900, 900, 100))
                reset_button = pygame.Rect(100, 900, 120, 80)
                restart_button = pygame.Rect(400, 900, 120, 80)
                exit_button = pygame.Rect(700, 900, 120, 80)
                reset_text = font.render('RESET', True, 'black')
                restart_text = font.render('RESTART', True, 'black')
                exit_text = font.render('EXIT', True, 'black')
                reset = screen.blit(reset_text, (reset_button.x + 5, reset_button.y + 5))
                restart = screen.blit(restart_text, (restart_button.x + 5, restart_button.y + 5))
                exit_blit = screen.blit(exit_text, (exit_button.x + 5, exit_button.y + 5))
                if exit_button.collidepoint((mouseX, mouseY)) and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    exit(0)
                pygame.display.flip()
                # board.select(1,1)

                pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN and (medium_button.x <= a <= medium_button.x + 120 and medium_button.y <= b <= medium_button.y + 80):
            status = False
            pygame.display.set_caption("Medium Difficulty")
            screen = pygame.display.set_mode((900, 1000))
            screen.fill((255, 255, 255))
            board = Board(900, 900, screen, 1)
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 1000, 900, 100))
            pygame.display.flip()
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
                        if event.key == pygame.K_1:
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
                        elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
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
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 900, 900, 100))
                reset_button = pygame.Rect(100, 900, 120, 80)
                restart_button = pygame.Rect(400, 900, 120, 80)
                exit_button = pygame.Rect(700, 900, 120, 80)
                reset_text = font.render('RESET', True, 'black')
                restart_text = font.render('RESTART', True, 'black')
                exit_text = font.render('EXIT', True, 'black')

                reset = screen.blit(reset_text, (reset_button.x + 5, reset_button.y + 5))
                restart = screen.blit(restart_text, (restart_button.x + 5, restart_button.y + 5))
                exit_blit = screen.blit(exit_text, (exit_button.x + 5, exit_button.y + 5))
                if exit_button.collidepoint((mouseX, mouseY)) and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    exit(0)
                pygame.display.flip()
                # board.select(1,1)

                pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN and (hard_button.x <= a <= hard_button.x + 120 and hard_button.y <= b <= hard_button.y + 80):
            status = False
            pygame.display.set_caption("Hard Difficulty")
            pygame.display.flip()
            screen = pygame.display.set_mode((900, 1000))
            screen.fill((255, 255, 255))
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
                        if event.key == pygame.K_1:
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
                        elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
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
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 900, 900, 100))
                reset_text = font.render('RESET', True, 'black')
                restart_text = font.render('RESTART', True, 'black')
                exit_text = font.render('EXIT', True, 'black')
                reset_button = pygame.Rect(100, 900, 150, 80)
                restart_button = pygame.Rect(400, 900, 120, 80)
                exit_button = pygame.Rect(700, 900, 120, 80)

                reset = screen.blit(reset_text, (reset_button.x + 5, reset_button.y + 5))
                restart = screen.blit(restart_text, (restart_button.x + 5, restart_button.y + 5))
                exit_blit = screen.blit(exit_text, (exit_button.x + 5, exit_button.y + 5))
                if exit_button.collidepoint((mouseX, mouseY)) and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    exit(0)
                pygame.display.flip()




        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()
