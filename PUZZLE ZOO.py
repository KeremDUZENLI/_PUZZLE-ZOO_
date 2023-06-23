from globals import *
from pages import *
from buttons import *
from functions import *


def button_circle_restart_definer(mouse_pos):
    global page
    global number_click

    if (button_circle_restart_1.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 1
        number_click = 0

    if (button_circle_restart_3.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 3
        number_click = 0

    if (button_circle_restart_5.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 5
        number_click = 0

    if (button_circle_restart_7.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 7
        number_click = 0

    if (button_circle_restart_9.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 9
        number_click = 0


def button_circle_next_definer(mouse_pos):
    global page
    global number_click

    if (button_circle_next_0.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 1
        number_click = 0

    if (button_circle_next_1.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 2

    if (button_circle_next_2.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 3
        number_click = 0

    if (button_circle_next_3.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 4

    if (button_circle_next_4.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 5
        number_click = 0

    if (button_circle_next_5.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 6

    if (button_circle_next_6.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 7
        number_click = 0

    if (button_circle_next_7.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 8

    if (button_circle_next_8.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 9
        number_click = 0

    if (button_circle_next_9.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 10

    if (button_circle_next_10.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 11
        number_click = 0


def button_rectangle_four_picture_definer(mouse_pos, number_page: float):
    global page
    global number_click
    list_created, image = page_rectangle_four_picture_definer(number_page)

    if (button_rectangle_four_picture_1.collidepoint(mouse_pos)) & (page == number_page):
        page_rectangle_four_picture_validator(40, list_created, image)
        number_click += 1

    if (button_rectangle_four_picture_2.collidepoint(mouse_pos)) & (page == number_page):
        page_rectangle_four_picture_validator(280, list_created, image)
        number_click += 1

    if (button_rectangle_four_picture_3.collidepoint(mouse_pos)) & (page == number_page):
        page_rectangle_four_picture_validator(520, list_created, image)
        number_click += 1

    if (button_rectangle_four_picture_4.collidepoint(mouse_pos)) & (page == number_page):
        page_rectangle_four_picture_validator(760, list_created, image)
        number_click += 1


def page_rectangle_four_picture_definer(number_page: float):
    mapping = {
        1.5: (list_new_1, image_1),
        3.5: (list_new_2, image_2),
        5.5: (list_new_3, image_3),
        7.5: (list_new_4, image_4),
        9.5: (list_new_5, image_5)
    }

    return mapping.get(number_page)


def page_rectangle_four_picture_validator(list_number, list_giving, image):
    if list_giving.index(list_number) == number_click:
        page_rectangle_four_picture_validator_colorer(
            list_number, list_giving, image)
    else:
        page_rectangle_four_picture_validator_colorer(list_number)


while running:

    # PAGES --------------------------------------------------
    if page == 0:
        page_main()
        button_circle_next_0 = button_circle_next(0)
        pygame.display.update()

    if page == 2:
        image_provider_divided_four(image_1)
        button_circle_next_2 = button_circle_next(2)
        pygame.display.update()

    if page == 4:
        image_provider_divided_four(image_2)
        button_circle_next_4 = button_circle_next(4)
        pygame.display.update()

    if page == 6:
        image_provider_divided_four(image_3)
        button_circle_next_6 = button_circle_next(6)
        pygame.display.update()

    if page == 8:
        image_provider_divided_four(image_4)
        button_circle_next_8 = button_circle_next(8)
        pygame.display.update()

    if page == 10:
        image_provider_divided_four(image_5)
        button_circle_next_10 = button_circle_next(10)
        pygame.display.update()

    if page == 1:
        page_rectangle_four_picture_creator(list_new_1, image_1)
        draw_screen()

        button_circle_restart_1 = button_circle_restart(1)
        button_circle_next_1 = button_circle_next(1)
        page = page_updater(1.5)

    if page == 3:
        page_rectangle_four_picture_creator(list_new_2, image_2)
        draw_screen()

        button_circle_restart_3 = button_circle_restart(2)
        button_circle_next_3 = button_circle_next(3)
        page = page_updater(3.5)

    if page == 5:
        page_rectangle_four_picture_creator(list_new_3, image_3)
        draw_screen()

        button_circle_restart_5 = button_circle_restart(3)
        button_circle_next_5 = button_circle_next(5)
        page = page_updater(5.5)

    if page == 7:
        page_rectangle_four_picture_creator(list_new_4, image_4)
        draw_screen()

        button_circle_restart_7 = button_circle_restart(4)
        button_circle_next_7 = button_circle_next(7)
        page = page_updater(7.5)

    if page == 9:
        page_rectangle_four_picture_creator(list_new_5, image_5)
        draw_screen()

        button_circle_restart_9 = button_circle_restart(5)
        button_circle_next_9 = button_circle_next(9)
        page = page_updater(9.5)

    # EVENTS --------------------------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            button_circle_restart_definer(mouse_pos)
            button_circle_next_definer(mouse_pos)

            button_rectangle_four_picture_definer(mouse_pos, 1.5)
            button_rectangle_four_picture_definer(mouse_pos, 3.5)
            button_rectangle_four_picture_definer(mouse_pos, 5.5)
            button_rectangle_four_picture_definer(mouse_pos, 7.5)
            button_rectangle_four_picture_definer(mouse_pos, 9.5)
