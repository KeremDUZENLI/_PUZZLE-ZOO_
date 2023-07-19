from globals import *
from pages import *
from buttons import *
from functions import *


pages = Pages()
buttons = Buttons()
functions = Functions()


def define_button_circle_restart(mouse_pos):
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


def define_button_circle_next(mouse_pos):
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


def define_button_rectangle_four_picture(mouse_pos, number_page: float):
    global page
    global number_click
    list_created, image = define_page_rectangle_four_picture(number_page)

    if (button_rectangle_four_picture_1.collidepoint(mouse_pos)) & (page == number_page):
        validate_page_rectangle_four_picture(40, list_created, image)
        number_click += 1

    if (button_rectangle_four_picture_2.collidepoint(mouse_pos)) & (page == number_page):
        validate_page_rectangle_four_picture(280, list_created, image)
        number_click += 1

    if (button_rectangle_four_picture_3.collidepoint(mouse_pos)) & (page == number_page):
        validate_page_rectangle_four_picture(520, list_created, image)
        number_click += 1

    if (button_rectangle_four_picture_4.collidepoint(mouse_pos)) & (page == number_page):
        validate_page_rectangle_four_picture(760, list_created, image)
        number_click += 1


def validate_page_rectangle_four_picture(list_number, list_giving, image):
    if list_giving.index(list_number) == number_click:
        functions.color_page_rectangle_four_picture(
            list_number, list_giving, image)
    else:
        functions.color_page_rectangle_four_picture(list_number)


while running:

    # PAGES --------------------------------------------------
    if page == 0:
        pages.page_main()
        button_circle_next_0
        pygame.display.update()

    if page == 2:
        provide_image_divided_four(image_1)
        button_circle_next_2 = buttons.button_circle_next()
        pygame.display.update()

    if page == 4:
        provide_image_divided_four(image_2)
        button_circle_next_4 = buttons.button_circle_next()
        pygame.display.update()

    if page == 6:
        provide_image_divided_four(image_3)
        button_circle_next_6 = buttons.button_circle_next()
        pygame.display.update()

    if page == 8:
        provide_image_divided_four(image_4)
        button_circle_next_8 = buttons.button_circle_next()
        pygame.display.update()

    if page == 10:
        provide_image_divided_four(image_5)
        button_circle_next_10 = buttons.button_circle_next()
        pygame.display.update()

    if page == 1:
        functions.create_page_rectangle_four_picture(list_new_1, image_1)
        pages.draw_screen()

        button_circle_restart_1 = buttons.button_circle_restart()
        button_circle_next_1 = buttons.button_circle_next()
        page = pages.update_page(1.5)

    if page == 3:
        functions.create_page_rectangle_four_picture(list_new_2, image_2)
        pages.draw_screen()

        button_circle_restart_3 = buttons.button_circle_restart()
        button_circle_next_3 = buttons.button_circle_next()
        page = pages.update_page(3.5)

    if page == 5:
        functions.create_page_rectangle_four_picture(list_new_3, image_3)
        pages.draw_screen()

        button_circle_restart_5 = buttons.button_circle_restart()
        button_circle_next_5 = buttons.button_circle_next()
        page = pages.update_page(5.5)

    if page == 7:
        functions.create_page_rectangle_four_picture(list_new_4, image_4)
        pages.draw_screen()

        button_circle_restart_7 = buttons.button_circle_restart()
        button_circle_next_7 = buttons.button_circle_next()
        page = pages.update_page(7.5)

    if page == 9:
        functions.create_page_rectangle_four_picture(list_new_5, image_5)
        pages.draw_screen()

        button_circle_restart_9 = buttons.button_circle_restart()
        button_circle_next_9 = buttons.button_circle_next()
        page = pages.update_page(9.5)

    # EVENTS --------------------------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            define_button_circle_restart(mouse_pos)
            define_button_circle_next(mouse_pos)

            define_button_rectangle_four_picture(mouse_pos, 1.5)
            define_button_rectangle_four_picture(mouse_pos, 3.5)
            define_button_rectangle_four_picture(mouse_pos, 5.5)
            define_button_rectangle_four_picture(mouse_pos, 7.5)
            define_button_rectangle_four_picture(mouse_pos, 9.5)
