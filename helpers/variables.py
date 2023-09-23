import pygame
import random


pygame.init()
pygame.display.set_caption("PUZZLE ZOO")
screen = pygame.display.set_mode((1000, 1000))


page = 0
number_click = 0
running = True


def provide_image(path: str, width: int = 400, height: int = 400):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (width, height))


def provide_image_divided_four(image):
    screen.fill((255, 255, 255))

    image_scaled = pygame.transform.scale(image, (500, 500))
    screen.blit(image_scaled, (250, 250))


font_default = pygame.font.SysFont("calibri", 50, True)
image_background = provide_image("images/[Background].jpg", 1000, 1000)
image_button_next = provide_image("images/[Next].png", 80, 80)
image_button_restart = provide_image("images/[Restart].png", 80, 80)


def create_list_new():
    list_new = []
    for _ in range(100):
        number_chosen = random.choice([40, 280, 520, 760])

        if number_chosen not in list_new:
            list_new.append(number_chosen)

    return list_new


image_1 = provide_image("images/1.png")
image_2 = provide_image("images/2.png")
image_3 = provide_image("images/3.png")
image_4 = provide_image("images/4.png")
image_5 = provide_image("images/5.png")

list_new_1 = create_list_new()
list_new_2 = create_list_new()
list_new_3 = create_list_new()
list_new_4 = create_list_new()
list_new_5 = create_list_new()


def define_page_rectangle_four_picture(number_page: float):
    mapping = {
        1.5: (list_new_1, image_1),
        3.5: (list_new_2, image_2),
        5.5: (list_new_3, image_3),
        7.5: (list_new_4, image_4),
        9.5: (list_new_5, image_5)
    }

    return mapping.get(number_page)


button_circle_restart_1 = pygame.Rect(0, 0, 0, 0)
button_circle_restart_3 = pygame.Rect(0, 0, 0, 0)
button_circle_restart_5 = pygame.Rect(0, 0, 0, 0)
button_circle_restart_7 = pygame.Rect(0, 0, 0, 0)
button_circle_restart_9 = pygame.Rect(0, 0, 0, 0)


button_circle_next_0 = pygame.Rect(450, 730, 100, 100)
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
