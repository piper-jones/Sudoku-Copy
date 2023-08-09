
import pygame
pygame.init()

from board import Board
from gui import *

def main():
    screen = pygame.display.set_mode((900, 1000))
    board = Board(900, 900, screen, Removal.difficulty)

    running = True
    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint((mouseX, mouseY)):
                    pygame.quit()
                    exit(0)
                if restart_button.collidepoint((mouseX, mouseY)):
                    starter_screen()
                    main()
                    return
                if reset_button.collidepoint((mouseX, mouseY)):
                    for i in range(9):
                        for y in range(9):
                            if board.current_board[i][y] != board.locked_board[i][y]:
                                board.current_board[i][y] = 0
                            if board.temp_cells[i][y] != board.locked_board[i][y]:
                                board.temp_cells[i][y] = 0
                board.click(mouseX, mouseY)

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
        if board.is_full() and board.check_board():
            win_screen()

        if board.is_full() and not board.check_board():
            lose_screen()
        #buttons for underneath the board
        font = pygame.font.SysFont("Arial", 60, bold=True)
        mouseX, mouseY = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 900, 900, 100))
        # these are the reset, restart, and exit buttons
        reset_button = pygame.Rect(100, 900, 120, 80)
        restart_button = pygame.Rect(400, 900, 120, 80)
        exit_button = pygame.Rect(700, 900, 120, 80)
        reset_text = font.render('RESET', True, 'black')
        restart_text = font.render('RESTART', True, 'black')
        exit_text = font.render('EXIT', True, 'black')
        reset = screen.blit(reset_text, (reset_button.x + 5, reset_button.y + 5))
        restart = screen.blit(restart_text, (restart_button.x + 5, restart_button.y + 5))
        exit_blit = screen.blit(exit_text, (exit_button.x + 5, exit_button.y + 5))
        # when exit button is clicked and hovered over the game quits (the above comments I made and the code around it is the same for medium and hard difficulty

        pygame.display.flip()
        # board.select(1,1)

    pygame.quit()

if __name__ == "__main__":
    while True:
        starter_screen()
        main()
