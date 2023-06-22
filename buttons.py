from globals import *


def buttonRestart(number: int):
    pygame.draw.circle(screen, (255, 0, 0), [900, 250], 50)
    screen.blit(img_restart, (860, 210))

    if number == 1:
        circle_restart_button1 = pygame.Rect(850, 200, 100, 100)
        return circle_restart_button1

    if number == 2:
        circle_restart_button3 = pygame.Rect(850, 200, 100, 100)
        return circle_restart_button3

    if number == 3:
        circle_restart_button5 = pygame.Rect(850, 200, 100, 100)
        return circle_restart_button5

    if number == 4:
        circle_restart_button7 = pygame.Rect(850, 200, 100, 100)
        return circle_restart_button7

    if number == 5:
        circle_restart_button9 = pygame.Rect(850, 200, 100, 100)
        return circle_restart_button9


def buttonNextGeneral(number: int):
    if number == 0:
        circle_next_button0 = pygame.Rect(450, 730, 100, 100)
        return circle_next_button0

    else:
        return buttonNext(number)


def buttonNext(number: int):
    pygame.draw.circle(screen, (0, 255, 0), [900, 550], 50)
    screen.blit(img_next, (860, 510))

    if number == 1:
        circle_next_button1 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button1

    if number == 2:
        circle_next_button2 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button2

    if number == 3:
        circle_next_button3 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button3

    if number == 4:
        circle_next_button4 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button4

    if number == 5:
        circle_next_button5 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button5

    if number == 6:
        circle_next_button6 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button6

    if number == 7:
        circle_next_button7 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button7

    if number == 8:
        circle_next_button8 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button8

    if number == 9:
        circle_next_button9 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button9

    if number == 10:
        circle_next_button10 = pygame.Rect(850, 500, 100, 100)
        return circle_next_button10
