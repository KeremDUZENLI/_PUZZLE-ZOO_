from globals import *


class Buttons:
    def __init__(self):
        pass

    def button_circle_restart(self):
        pygame.draw.circle(screen, (255, 0, 0), [900, 250], 50)
        screen.blit(image_button_restart, (860, 210))

        button_circle_restart = pygame.Rect(850, 200, 100, 100)
        return button_circle_restart

    def button_circle_next(self):
        pygame.draw.circle(screen, (0, 255, 0), [900, 550], 50)
        screen.blit(image_button_next, (860, 510))

        button_circle_next = pygame.Rect(850, 500, 100, 100)
        return button_circle_next
