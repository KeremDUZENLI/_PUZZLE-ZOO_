from globals import *
from pages import *
from buttons import *
from functions import *


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


def rectButtonPressed(liste, img):
    global rect1a_button_pressed
    global rect2a_button_pressed
    global rect3a_button_pressed
    global rect4a_button_pressed

    def rect1a_button_pressed(): rectButtonPressedHelper(40, liste, img)
    def rect2a_button_pressed(): rectButtonPressedHelper(280, liste, img)
    def rect3a_button_pressed(): rectButtonPressedHelper(520, liste, img)
    def rect4a_button_pressed(): rectButtonPressedHelper(760, liste, img)


def rectButtonPressedHelper(numberInList, liste, img):
    if liste.index(numberInList) == clickAmount:
        pictureLocationer(numberInList, liste, img)
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
        clickAmount += 1

    if (rect2a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect2a_button_pressed()
        clickAmount += 1

    if (rect3a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect3a_button_pressed()
        clickAmount += 1

    if (rect4a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rect4a_button_pressed()
        clickAmount += 1


# --------------------------------------------------------------------------------------------------------
while running:

    # PAGES --------------------------------------------------
    if page == 1.5:
        rectButtonPressed(yeni_liste1, img1)

    if page == 3.5:
        rectButtonPressed(yeni_liste2, img2)

    if page == 5.5:
        rectButtonPressed(yeni_liste3, img3)

    if page == 7.5:
        rectButtonPressed(yeni_liste4, img4)

    if page == 9.5:
        rectButtonPressed(yeni_liste5, img5)

    if page == 0:
        page0()
        circle_next_button0 = buttonNextGeneral(0)
        page = pageUpdate(0.5)

    if page == 2:
        imageProvider("images/1.png")
        circle_next_button2 = buttonNextGeneral(2)
        pygame.display.update()

    if page == 4:
        imageProvider("images/2.png")
        circle_next_button4 = buttonNextGeneral(4)
        pygame.display.update()

    if page == 6:
        imageProvider("images/3.png")
        circle_next_button6 = buttonNextGeneral(6)
        pygame.display.update()

    if page == 8:
        imageProvider("images/4.png")
        circle_next_button8 = buttonNextGeneral(8)
        pygame.display.update()

    if page == 10:
        imageProvider("images/5.png")
        circle_next_button10 = buttonNextGeneral(10)
        pygame.display.update()

    if page == 1:
        pageCreate(img1, yeni_liste1)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        circle_restart_button1 = buttonRestart(1)
        circle_next_button1 = buttonNextGeneral(1)
        page = pageUpdate(1.5)

    if page == 3:
        pageCreate(img2, yeni_liste2)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        circle_restart_button2 = buttonRestart(2)
        circle_next_button3 = buttonNextGeneral(3)
        page = pageUpdate(3.5)

    if page == 5:
        pageCreate(img3, yeni_liste3)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        circle_restart_button3 = buttonRestart(3)
        circle_next_button5 = buttonNextGeneral(5)
        page = pageUpdate(5.5)

    if page == 7:
        pageCreate(img4, yeni_liste4)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        circle_restart_button4 = buttonRestart(4)
        circle_next_button7 = buttonNextGeneral(7)
        page = pageUpdate(7.5)

    if page == 9:
        pageCreate(img5, yeni_liste5)

        drawMiddleRectangles()
        drawBottomRectangles()

        drawLine()

        circle_restart_button5 = buttonRestart(5)
        circle_next_button9 = buttonNextGeneral(9)
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
