from re import X
from pygame import mixer
from pygame.locals import *

from functions import *
from buttons import *
from globals import *
from init import *
from pages import *


def buttonNextGeneral(number: int):
    global circle_next_button0

    if number == 0:
        circle_next_button0 = pygame.Rect(450, 730, 100, 100)

    else:
        buttonNext(number)


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


def buttonCircleDefiner(mouse_pos):
    global page
    global clickAmount

    # -- Page 0 ----------------------------------------------------------------------
    if (circle_next_button0.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 1
        clickAmount = 0

    # -- Page 1 ----------------------------------------------------------------------
    if (circle_restart_button1.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 1
        clickAmount = 0

    if (circle_next_button1.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 2

    # -- Page 2 ----------------------------------------------------------------------
    if (circle_next_button2.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 3
        clickAmount = 0

    # -- Page 3 ----------------------------------------------------------------------
    if (circle_restart_button2.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 3
        clickAmount = 0

    if (circle_next_button3.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 4

    # -- Page 4 ----------------------------------------------------------------------
    if (circle_next_button4.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 5
        clickAmount = 0

    # -- Page 5 ----------------------------------------------------------------------
    if (circle_restart_button3.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 5
        clickAmount = 0

    if (circle_next_button5.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 6

    # -- Page 6 ----------------------------------------------------------------------
    if (circle_next_button6.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 7
        clickAmount = 0

    # -- Page 7 ----------------------------------------------------------------------
    if (circle_restart_button4.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 7
        clickAmount = 0

    if (circle_next_button7.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 8

    # -- Page 8 ----------------------------------------------------------------------
    if (circle_next_button8.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 9
        clickAmount = 0

    # -- Page 9 ----------------------------------------------------------------------
    if (circle_restart_button5.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 9
        clickAmount = 0

    if (circle_next_button9.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 10

    # -- Page 10 ----------------------------------------------------------------------
    if (circle_next_button10.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 11
        clickAmount = 0


def rectButtonPressed(liste, tileSprite):
    global rect1a_button_pressed
    global rect2a_button_pressed
    global rect3a_button_pressed
    global rect4a_button_pressed

    def rect1a_button_pressed(): rectButtonPressedHelper(40, liste, tileSprite)
    def rect2a_button_pressed(): rectButtonPressedHelper(280, liste, tileSprite)
    def rect3a_button_pressed(): rectButtonPressedHelper(520, liste, tileSprite)
    def rect4a_button_pressed(): rectButtonPressedHelper(760, liste, tileSprite)


def rectButtonPressedHelper(numberInList, liste, tileSprite):
    if liste.index(numberInList) == clickAmount:
        pictureLocationer(numberInList, liste, tileSprite)
    else:
        pictureLocationer(numberInList)


def buttonRectDefinerForPage(mouse_pos, pageNum: float):
    global clickAmount

    rect1a_button = pygame.Rect(40, 760, 200, 200)
    rect2a_button = pygame.Rect(280, 760, 200, 200)
    rect3a_button = pygame.Rect(520, 760, 200, 200)
    rect4a_button = pygame.Rect(760, 760, 200, 200)

    if (rect1a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect1a_button_pressed()
        clickAmount = clickAmount + 1

    if (rect2a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect2a_button_pressed()
        clickAmount = clickAmount + 1

    if (rect3a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect3a_button_pressed()
        clickAmount = clickAmount + 1

    if (rect4a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect4a_button_pressed()
        clickAmount = clickAmount + 1


# --------------------------------------------------------------------------------------------------------
while running:

    # PAGES --------------------------------------------------
    if page == 1.5:
        rectButtonPressed(yeni_liste1, tileSprite1)

    if page == 3.5:
        rectButtonPressed(yeni_liste3, tileSprite3)

    if page == 5.5:
        rectButtonPressed(yeni_liste5, tileSprite5)

    if page == 7.5:
        rectButtonPressed(yeni_liste7, tileSprite7)

    if page == 9.5:
        rectButtonPressed(yeni_liste9, tileSprite9)

    if page == 0:
        page0()
        buttonNextGeneral(0)
        page = pageUpdate(0.5)

    if page == 2:
        imageProvider("1.png")
        buttonNextGeneral(2)
        pygame.display.update()

    if page == 4:
        imageProvider("2.png")
        buttonNextGeneral(4)
        pygame.display.update()

    if page == 6:
        imageProvider("3.png")
        buttonNextGeneral(6)
        pygame.display.update()

    if page == 8:
        imageProvider("4.png")
        buttonNextGeneral(8)
        pygame.display.update()

    if page == 10:
        imageProvider("5.png")
        buttonNextGeneral(10)
        pygame.display.update()

    if page == 1:
        pageCreate(tileSprite1, yeni_liste1)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(1)
        buttonNextGeneral(1)
        page = pageUpdate(1.5)

    if page == 3:
        pageCreate(tileSprite3, yeni_liste3)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(2)
        buttonNextGeneral(3)
        page = pageUpdate(3.5)

    if page == 5:
        pageCreate(tileSprite5, yeni_liste5)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(3)
        buttonNextGeneral(5)
        page = pageUpdate(5.5)

    if page == 7:
        pageCreate(tileSprite7, yeni_liste7)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(4)
        buttonNextGeneral(7)
        page = pageUpdate(7.5)

    if page == 9:
        pageCreate(tileSprite9, yeni_liste9)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        buttonRestart(5)
        buttonNextGeneral(9)
        page = pageUpdate(9.5)

    # EVENTS --------------------------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            buttonCircleDefiner(mouse_pos)
            buttonRectDefinerForPage(mouse_pos, 1.5)
            buttonRectDefinerForPage(mouse_pos, 3.5)
            buttonRectDefinerForPage(mouse_pos, 5.5)
            buttonRectDefinerForPage(mouse_pos, 7.5)
            buttonRectDefinerForPage(mouse_pos, 9.5)
