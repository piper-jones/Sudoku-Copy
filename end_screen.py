import pygame
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 1000
curr = 1


starter_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("You Lose!")
sudoku_background = pygame.image.load("starter_img.webp")
sudoku_background = pygame.transform.scale(sudoku_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", 60, bold=True)

run = True
while run:

    status = True
    if status:
        main_screen_status = True
        starter_text = font.render("You Lose!", font, (69, 16, 12))
        starter_screen.blit(sudoku_background, (0, 0))
        starter_screen.blit(starter_text, (150, 0))
        main_menu = font.render('Return to Main Menu', True, 'black')

        main_menu_button = pygame.Rect(100, 200, 500, 80)


        a, b = pygame.mouse.get_pos()
        if main_menu_button.x <= a <= main_menu_button.x + 500 and main_menu_button.y <= b <= main_menu_button.y + 80:
            pygame.draw.rect(starter_screen, (180, 180, 180), main_menu_button)
        else:
            pygame.draw.rect(starter_screen, (110, 110, 110), main_menu_button)


        starter_screen.blit(main_menu, (main_menu_button.x + 5, main_menu_button.y + 5))


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and (main_menu_button.x <= a <= main_menu_button.x + 120 and main_menu_button.y <= b <= main_menu_button.y + 80):
            pygame.display.set_caption("Main Screen")
            starter_screen.fill((173, 23, 23))

        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()