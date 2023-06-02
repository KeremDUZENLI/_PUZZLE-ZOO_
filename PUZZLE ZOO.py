from re import X
from pygame import mixer
from pygame.locals import *

from functions import *
from globals import *
from init import *
from page1 import *
from page3 import *
from page5 import *
from page7 import *
from page9 import *


def page0():
    global circle_next_button0
    global circle_next_button0_pressed

    screen.fill((255, 255, 255))
    screen.blit(img_background, (0, 0))

    font_main_page = pygame.font.SysFont("calibri", 80, True)
    screen.blit(font_main_page.render("PUZZLE ZOO", True, "black"), (250, 630))

    pygame.draw.circle(screen, (0, 255, 0), [500, 780], 50)
    screen.blit(img_next, (460, 740))

    circle_next_button0 = pygame.Rect(450, 730, 100, 100)

    def circle_next_button0_pressed():
        pygame.display.update()


def pageCreate(tileSprite, liste):
    screen.fill((255, 255, 255))
    screen.blit(font_default.render("PUZZLE", True, "black"), (350, 50))

    screenBlit(tileSprite, liste)


def screenBlit(tileSprite, liste):
    screen.blit(tileSprite, (liste[0], 760), (0, 0, 200, 200))  # img1
    screen.blit(tileSprite, (liste[1], 760), (200, 0, 200, 200))  # img2
    screen.blit(tileSprite, (liste[2], 760), (0, 200, 200, 200))  # img3
    screen.blit(tileSprite, (liste[3], 760), (200, 200, 200, 200))  # img4


def screenBlitListe(tileSprite, liste, value):
    if liste[0] == value:
        screen.blit(tileSprite, (300, 200), (0, 0, 200, 200))  # img1

    if liste[1] == value:
        screen.blit(tileSprite, (500, 200), (200, 0, 200, 200))  # img2

    if liste[2] == value:
        screen.blit(tileSprite, (300, 400), (0, 200, 200, 200))  # img3

    if liste[3] == value:
        screen.blit(tileSprite, (500, 400), (200, 200, 200, 200))  # img4


def drawMiddleRectangles():
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(300, 200, 200, 200), 1)
    screen.blit(font_default.render("1", True, (0, 0, 0)), (300, 200))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 200, 200, 200), 1)
    screen.blit(font_default.render("2", True, (0, 0, 0)), (500, 200))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(300, 400, 200, 200), 1)
    screen.blit(font_default.render("3", True, (0, 0, 0)), (300, 400))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 400, 200, 200), 1)
    screen.blit(font_default.render("4", True, (0, 0, 0)), (500, 400))


def drawBottomRectangles():
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(40, 760, 200, 200),  1)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(280, 760, 200, 200), 1)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(520, 760, 200, 200), 1)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(760, 760, 200, 200), 1)


def drawLine():
    pygame.draw.line(screen, (0, 0, 0), (0, 720), (1000, 720), 3)


def buttonRestart(number: int):
    pygame.draw.circle(screen, (255, 0, 0), [900, 250], 50)
    screen.blit(img_restart, (860, 210))

    global circle_restart_button1
    global circle_restart_button2
    global circle_restart_button3
    global circle_restart_button4
    global circle_restart_button5

    if number == 1:
        circle_restart_button1 = pygame.Rect(850, 200, 100, 100)

    if number == 2:
        circle_restart_button2 = pygame.Rect(850, 200, 100, 100)

    if number == 3:
        circle_restart_button3 = pygame.Rect(850, 200, 100, 100)

    if number == 4:
        circle_restart_button4 = pygame.Rect(850, 200, 100, 100)

    if number == 5:
        circle_restart_button5 = pygame.Rect(850, 200, 100, 100)


def buttonNext(number: int):
    pygame.draw.circle(screen, (0, 255, 0), [900, 550], 50)
    screen.blit(img_next, (860, 510))

    global circle_next_button1
    global circle_next_button2
    global circle_next_button3
    global circle_next_button4
    global circle_next_button5
    global circle_next_button6
    global circle_next_button7
    global circle_next_button8
    global circle_next_button9
    global circle_next_button10

    if number == 1:
        circle_next_button1 = pygame.Rect(850, 500, 100, 100)

    if number == 2:
        circle_next_button2 = pygame.Rect(850, 500, 100, 100)

    if number == 3:
        circle_next_button3 = pygame.Rect(850, 500, 100, 100)

    if number == 4:
        circle_next_button4 = pygame.Rect(850, 500, 100, 100)

    if number == 5:
        circle_next_button5 = pygame.Rect(850, 500, 100, 100)

    if number == 6:
        circle_next_button6 = pygame.Rect(850, 500, 100, 100)

    if number == 7:
        circle_next_button7 = pygame.Rect(850, 500, 100, 100)

    if number == 8:
        circle_next_button8 = pygame.Rect(850, 500, 100, 100)

    if number == 9:
        circle_next_button9 = pygame.Rect(850, 500, 100, 100)

    if number == 10:
        circle_next_button10 = pygame.Rect(850, 500, 100, 100)


def pageUpdate(number: float):
    pygame.display.update()

    global page
    page = number


def rectButtonPressed(tileSprite, liste):
    global rect1a_button_pressed
    global rect2a_button_pressed
    global rect3a_button_pressed
    global rect4a_button_pressed

    if liste.index(40) == x:
        def rect1a_button_pressed():
            pictureLocationer(tileSprite, liste, 40)

    else:
        def rect1a_button_pressed():
            pictureLocationerDefault(40)

    if liste.index(280) == x:
        def rect2a_button_pressed():
            pictureLocationer(tileSprite, liste, 280)

    else:
        def rect2a_button_pressed():
            pictureLocationerDefault(280)

    if liste.index(520) == x:
        def rect3a_button_pressed():
            pictureLocationer(tileSprite, liste, 520)

    else:
        def rect3a_button_pressed():
            pictureLocationerDefault(520)

    if liste.index(760) == x:
        def rect4a_button_pressed():
            pictureLocationer(tileSprite, liste, 760)

    else:
        def rect4a_button_pressed():
            pictureLocationerDefault(760)


def pictureLocationer(tileSprite, liste, numberInList):
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(
        numberInList, 760, 200, 200),  1)

    screenBlitListe(tileSprite, liste, numberInList)
    pygame.display.update()


def pictureLocationerDefault(numberInList):
    pygame.draw.rect(screen, (255, 0, 0),
                     pygame.Rect(numberInList, 760, 200, 200),  1)
    pygame.display.update()


def imageProvider(image):
    screen.fill((255, 255, 255))

    real_img = pygame.image.load(image)
    real_img = pygame.transform.scale(real_img, (500, 500))
    screen.blit(real_img, (250, 250))


def buttonRectDefinerForPage(pageNum: float):
    global x

    rect1a_button = pygame.Rect(40, 760, 200, 200)
    rect2a_button = pygame.Rect(280, 760, 200, 200)
    rect3a_button = pygame.Rect(520, 760, 200, 200)
    rect4a_button = pygame.Rect(760, 760, 200, 200)

    if (rect1a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect1a_button_pressed()
        x = x + 1

    if (rect2a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect2a_button_pressed()
        x = x + 1

    if (rect3a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect3a_button_pressed()
        x = x + 1

    if (rect4a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect4a_button_pressed()
        x = x + 1


def buttonCircleDefiner():
    global page
    global x

    # -- Page 0 ----------------------------------------------------------------------
    if (circle_next_button0.collidepoint(mouse_pos)) & (page == 0.5):
        circle_next_button0_pressed()
        page = 1

    # -- Page 1 ----------------------------------------------------------------------
    if (circle_restart_button1.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 1
        x = 0

    if (circle_next_button1.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 2

    # -- Page 2 ----------------------------------------------------------------------
    if (circle_next_button2.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 3
        x = 0

    # -- Page 3 ----------------------------------------------------------------------
    if (circle_restart_button2.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 3
        x = 0

    if (circle_next_button3.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 4

    # -- Page 4 ----------------------------------------------------------------------
    if (circle_next_button4.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 5
        x = 0

    # -- Page 5 ----------------------------------------------------------------------
    if (circle_restart_button3.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 5
        x = 0

    if (circle_next_button5.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 6

    # -- Page 6 ----------------------------------------------------------------------
    if (circle_next_button6.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 7
        x = 0

    # -- Page 7 ----------------------------------------------------------------------
    if (circle_restart_button4.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 7
        x = 0

    if (circle_next_button7.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 8

    # -- Page 8 ----------------------------------------------------------------------
    if (circle_next_button8.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 9
        x = 0

    # -- Page 9 ----------------------------------------------------------------------
    if (circle_restart_button5.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 9
        x = 0

    if (circle_next_button9.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 10

    # -- Page 10 ----------------------------------------------------------------------
    if (circle_next_button10.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 11
        x = 0


# --------------------------------------------------------------------------------------------------------
while running:

    # PAGES --------------------------------------------------
    if page == 0:
        page0()
        pageUpdate(0.5)

    if page == 1:
        pageCreate(tileSprite1, yeni_liste1)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(1)
        buttonNext(1)
        pageUpdate(1.5)

    if page == 1.5:
        rectButtonPressed(tileSprite1, yeni_liste1)

    if page == 2:
        imageProvider("1.png")
        buttonNext(2)
        pygame.display.update()

    if page == 3:
        pageCreate(tileSprite3, yeni_liste3)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(2)
        buttonNext(3)
        pageUpdate(3.5)

    if page == 3.5:
        rectButtonPressed(tileSprite3, yeni_liste3)

    if page == 4:
        imageProvider("2.png")
        buttonNext(4)
        pygame.display.update()

    if page == 5:
        pageCreate(tileSprite5, yeni_liste5)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(3)
        buttonNext(5)
        pageUpdate(5.5)

    if page == 5.5:
        rectButtonPressed(tileSprite5, yeni_liste5)

    if page == 6:
        imageProvider("3.png")
        buttonNext(6)
        pygame.display.update()

    if page == 7:
        pageCreate(tileSprite7, yeni_liste7)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(4)
        buttonNext(7)
        pageUpdate(7.5)

    if page == 7.5:
        rectButtonPressed(tileSprite7, yeni_liste7)

    if page == 8:
        imageProvider("4.png")
        buttonNext(8)
        pygame.display.update()

    if page == 9:
        pageCreate(tileSprite9, yeni_liste9)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(5)
        buttonNext(9)
        pageUpdate(9.5)

    if page == 9.5:
        rectButtonPressed(tileSprite9, yeni_liste9)

    if page == 10:
        imageProvider("5.png")
        buttonNext(10)
        pygame.display.update()

    # EVENTS --------------------------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            buttonCircleDefiner()
            buttonRectDefinerForPage(1.5)
            buttonRectDefinerForPage(3.5)
            buttonRectDefinerForPage(5.5)
            buttonRectDefinerForPage(7.5)
            buttonRectDefinerForPage(9.5)
