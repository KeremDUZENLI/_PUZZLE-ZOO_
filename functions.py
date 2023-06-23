from globals import *


def page_rectangle_four_picture_creator(list_giving, image):
    screen.fill((255, 255, 255))
    screen.blit(font_default.render("PUZZLE", True, "black"), (350, 50))

    page_rectangle_four_picture_creator_helper(list_giving, image)


def page_rectangle_four_picture_creator_helper(list_giving, image):
    screen.blit(image, (list_giving[0], 760), (0, 0, 200, 200))  # image_1
    screen.blit(image, (list_giving[1], 760), (200, 0, 200, 200))  # image_2
    screen.blit(image, (list_giving[2], 760), (0, 200, 200, 200))  # image_2
    screen.blit(image, (list_giving[3], 760), (200, 200, 200, 200))  # image_4


def page_rectangle_four_picture_validator_colorer(list_number, list_giving=None, image=None):
    if image is not None and list_giving is not None:
        pygame.draw.rect(screen, (0, 255, 0),
                         pygame.Rect(list_number, 760, 200, 200),  1)
        page_rectangle_four_picture_validator_locationer(
            list_number, list_giving, image)

    else:
        pygame.draw.rect(screen, (255, 0, 0),
                         pygame.Rect(list_number, 760, 200, 200),  1)

    pygame.display.update()


def page_rectangle_four_picture_validator_locationer(list_number, list_giving, image):
    if list_giving[0] == list_number:
        screen.blit(image, (300, 200), (0, 0, 200, 200))  # image_1

    if list_giving[1] == list_number:
        screen.blit(image, (500, 200), (200, 0, 200, 200))  # image_2

    if list_giving[2] == list_number:
        screen.blit(image, (300, 400), (0, 200, 200, 200))  # image_2

    if list_giving[3] == list_number:
        screen.blit(image, (500, 400), (200, 200, 200, 200))  # image_4
