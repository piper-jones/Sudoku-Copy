import pygame
pygame.init()

class Removal:
    def __init__(self):
        self.difficulty = None
        self.state = None

def starter_screen():

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 1000
    curr = 1

    starter_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Main Screen")
    sudoku_background = pygame.image.load("starter1.jpg")
    sudoku_background = pygame.transform.scale(sudoku_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
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

                if event.type == pygame.MOUSEBUTTONDOWN and (
                        easy_button.x <= a <= easy_button.x + 120 and easy_button.y <= b <= easy_button.y + 80):
                    status = False
                    pygame.display.set_caption("Easy Difficulty")
                    Removal.difficulty = "easy"
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN and (
                        medium_button.x <= a <= medium_button.x + 120 and medium_button.y <= b <= medium_button.y + 80):
                    status = False
                    pygame.display.set_caption("Medium Difficulty")
                    Removal.difficulty = "medium"
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN and (
                        hard_button.x <= a <= hard_button.x + 120 and hard_button.y <= b <= hard_button.y + 80):
                    status = False
                    Removal.difficulty = "hard"
                    pygame.display.set_caption("Hard Difficulty")
                    run = False

                if event.type == pygame.QUIT:
                    run = False

        pygame.display.flip()

    pygame.quit()

def lose_screen():

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 1000
    curr = 1

    end_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("End Screen")
    end_background = pygame.image.load("end1.jpg")
    end_background = pygame.transform.scale(end_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 55, bold=True)
    big_font = pygame.font.SysFont("Arial", 300, bold=True)

    status = True
    run = True
    while run:

        if status:
            main_screen_status = True
            white = pygame.Color("white")
            lose_text = font.render("Game Over :(", big_font, white)
            end_screen.blit(end_background, (0, 0))
            end_screen.blit(lose_text, (300, 50))
            restart_text = font.render('Restart', True, 'black')

            lose_button = pygame.Rect(350, 200, 180, 70)

            a, b = pygame.mouse.get_pos()
            if lose_button.x <= a <= lose_button.x + 180 and lose_button.y <= b <= lose_button.y + 70:
                pygame.draw.rect(end_screen, (180, 180, 180), lose_button)
            else:
                pygame.draw.rect(end_screen, (110, 110, 110), lose_button)

            end_screen.blit(restart_text, (lose_button.x + 5, lose_button.y + 5))

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN and (
                        lose_button.x <= a <= lose_button.x + 120 and lose_button.y <= b <= lose_button.y + 80):
                    starter_screen()
                    status = False
                    run = False

                if event.type == pygame.QUIT:
                    run = False

        pygame.display.flip()

    pygame.quit()


def win_screen():

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 1000
    curr = 1

    win_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Win Screen")
    win_background = pygame.image.load("end2.jpg")
    win_background = pygame.transform.scale(win_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 55, bold=True)
    big_font = pygame.font.SysFont("Arial", 300, bold=True)

    status = True
    run = True
    while run:

        if status:
            main_screen_status = True
            white = pygame.Color("white")
            win_text = font.render("Game Won!", big_font, white)
            win_screen.blit(win_background, (0, 0))
            win_screen.blit(win_text, (350, 50))
            exit_text = font.render('Exit', True, 'black')

            exit_button = pygame.Rect(420, 170, 100, 70)

            a, b = pygame.mouse.get_pos()
            if exit_button.x <= a <= exit_button.x + 170 and exit_button.y <= b <= exit_button.y + 70:
                pygame.draw.rect(win_screen, (180, 180, 180), exit_button)
            else:
                pygame.draw.rect(win_screen, (110, 110, 110), exit_button)

            win_screen.blit(exit_text, (exit_button.x + 5, exit_button.y + 5))

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN and (
                        exit_button.x <= a <= exit_button.x + 120 and exit_button.y <= b <= exit_button.y + 80):
                    pygame.quit()
                    exit(0)
                    status = False
                    run = False

                if event.type == pygame.QUIT:
                    run = False

        pygame.display.flip()

    pygame.quit()
