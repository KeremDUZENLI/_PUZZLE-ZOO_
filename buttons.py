from globals import *


def button_circle_restart(number_page: int):
    pygame.draw.circle(screen, (255, 0, 0), [900, 250], 50)
    screen.blit(image_button_restart, (860, 210))

    if number_page == 1:
        button_circle_restart_1 = pygame.Rect(850, 200, 100, 100)
        return button_circle_restart_1

    if number_page == 2:
        button_circle_restart_3 = pygame.Rect(850, 200, 100, 100)
        return button_circle_restart_3

    if number_page == 3:
        button_circle_restart_5 = pygame.Rect(850, 200, 100, 100)
        return button_circle_restart_5

    if number_page == 4:
        button_circle_restart_7 = pygame.Rect(850, 200, 100, 100)
        return button_circle_restart_7

    if number_page == 5:
        button_circle_restart_9 = pygame.Rect(850, 200, 100, 100)
        return button_circle_restart_9


def button_circle_next(number_page: int):
    if number_page == 0:
        button_circle_next_0 = pygame.Rect(450, 730, 100, 100)
        return button_circle_next_0

    else:
        return button_circle_next_helper(number_page)


def button_circle_next_helper(number_page: int):
    pygame.draw.circle(screen, (0, 255, 0), [900, 550], 50)
    screen.blit(image_button_next, (860, 510))

    if number_page == 1:
        button_circle_next_1 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_1

    if number_page == 2:
        button_circle_next_2 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_2

    if number_page == 3:
        button_circle_next_3 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_3

    if number_page == 4:
        button_circle_next_4 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_4

    if number_page == 5:
        button_circle_next_5 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_5

    if number_page == 6:
        button_circle_next_6 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_6

    if number_page == 7:
        button_circle_next_7 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_7

    if number_page == 8:
        button_circle_next_8 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_8

    if number_page == 9:
        button_circle_next_9 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_9

    if number_page == 10:
        button_circle_next_10 = pygame.Rect(850, 500, 100, 100)
        return button_circle_next_10
