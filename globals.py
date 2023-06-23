import pygame
import random


pygame.init()
pygame.display.set_caption("PUZZLE ZOO")
screen = pygame.display.set_mode((1000, 1000))


def image_provider(path: str, width: int = 400, height: int = 400):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (width, height))


def list_new_creator():
    list_new = []
    for _ in range(100):
        number_chosen = random.choice([40, 280, 520, 760])

        if number_chosen not in list_new:
            list_new.append(number_chosen)

    return list_new


page = 0
number_click = 0
running = True


image_1 = image_provider("images/1.png")
image_2 = image_provider("images/2.png")
image_3 = image_provider("images/3.png")
image_4 = image_provider("images/4.png")
image_5 = image_provider("images/5.png")

list_new_1 = list_new_creator()
list_new_2 = list_new_creator()
list_new_3 = list_new_creator()
list_new_4 = list_new_creator()
list_new_5 = list_new_creator()


font_default = pygame.font.SysFont("calibri", 50, True)
image_background = image_provider("images/[Background].jpg", 1000, 1000)
image_button_next = image_provider("images/[Next].png", 80, 80)
image_button_restart = image_provider("images/[Restart].png", 80, 80)


button_circle_restart_1 = pygame.Rect(0, 0, 0, 0)
button_circle_restart_3 = pygame.Rect(0, 0, 0, 0)
button_circle_restart_5 = pygame.Rect(0, 0, 0, 0)
button_circle_restart_7 = pygame.Rect(0, 0, 0, 0)
button_circle_restart_9 = pygame.Rect(0, 0, 0, 0)

button_circle_next_0 = pygame.Rect(0, 0, 0, 0)
button_circle_next_1 = pygame.Rect(0, 0, 0, 0)
button_circle_next_2 = pygame.Rect(0, 0, 0, 0)
button_circle_next_3 = pygame.Rect(0, 0, 0, 0)
button_circle_next_4 = pygame.Rect(0, 0, 0, 0)
button_circle_next_5 = pygame.Rect(0, 0, 0, 0)
button_circle_next_6 = pygame.Rect(0, 0, 0, 0)
button_circle_next_7 = pygame.Rect(0, 0, 0, 0)
button_circle_next_8 = pygame.Rect(0, 0, 0, 0)
button_circle_next_9 = pygame.Rect(0, 0, 0, 0)
button_circle_next_10 = pygame.Rect(0, 0, 0, 0)

button_rectangle_four_picture_1 = pygame.Rect(40, 760, 200, 200)
button_rectangle_four_picture_2 = pygame.Rect(280, 760, 200, 200)
button_rectangle_four_picture_3 = pygame.Rect(520, 760, 200, 200)
button_rectangle_four_picture_4 = pygame.Rect(760, 760, 200, 200)
