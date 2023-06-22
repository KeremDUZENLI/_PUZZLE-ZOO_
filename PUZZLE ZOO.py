from globals import *
from pages import *
from buttons import *
from functions import *


# Button Definers In While Loop--------------------------------------------------------------------------------------------------------
def buttonCircleDefinerRestart(mouse_pos):
    global page
    global clickAmount

    if (circle_restart_button1.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 1
        clickAmount = 0

    if (circle_restart_button3.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 3
        clickAmount = 0

    if (circle_restart_button5.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 5
        clickAmount = 0

    if (circle_restart_button7.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 7
        clickAmount = 0

    if (circle_restart_button9.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 9
        clickAmount = 0


def buttonCircleDefinerNext(mouse_pos):
    global page
    global clickAmount

    if (circle_next_button0.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 1
        clickAmount = 0

    if (circle_next_button1.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 2

    if (circle_next_button2.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 3
        clickAmount = 0

    if (circle_next_button3.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 4

    if (circle_next_button4.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 5
        clickAmount = 0

    if (circle_next_button5.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 6

    if (circle_next_button6.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 7
        clickAmount = 0

    if (circle_next_button7.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 8

    if (circle_next_button8.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 9
        clickAmount = 0

    if (circle_next_button9.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 10

    if (circle_next_button10.collidepoint(mouse_pos)):
        pygame.display.update()
        page = 11
        clickAmount = 0


def buttonRectDefinerForPage(mouse_pos, pageNum: float, liste, img):
    global clickAmount

    if (rect1a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rectButtonPressedHelper(40, liste, img)
        clickAmount += 1

    if (rect2a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rectButtonPressedHelper(280, liste, img)
        clickAmount += 1

    if (rect3a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rectButtonPressedHelper(520, liste, img)
        clickAmount += 1

    if (rect4a_button.collidepoint(mouse_pos)) & (page == pageNum):
        rectButtonPressedHelper(760, liste, img)
        clickAmount += 1


def rectButtonPressedHelper(numberInList, liste, img):
    if liste.index(numberInList) == clickAmount:
        pictureLocationer(numberInList, liste, img)
    else:
        pictureLocationer(numberInList)


# MAIN--------------------------------------------------------------------------------------------------------
while running:

    # PAGES --------------------------------------------------
    if page == 0:
        page0()
        circle_next_button0 = buttonNextGeneral(0)
        pygame.display.update()

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
        draw()

        circle_restart_button1 = buttonRestart(1)
        circle_next_button1 = buttonNextGeneral(1)
        page = pageUpdate(1.5)

    if page == 3:
        pageCreate(img2, yeni_liste2)
        draw()

        circle_restart_button3 = buttonRestart(2)
        circle_next_button3 = buttonNextGeneral(3)
        page = pageUpdate(3.5)

    if page == 5:
        pageCreate(img3, yeni_liste3)
        draw()

        circle_restart_button5 = buttonRestart(3)
        circle_next_button5 = buttonNextGeneral(5)
        page = pageUpdate(5.5)

    if page == 7:
        pageCreate(img4, yeni_liste4)
        draw()

        circle_restart_button7 = buttonRestart(4)
        circle_next_button7 = buttonNextGeneral(7)
        page = pageUpdate(7.5)

    if page == 9:
        pageCreate(img5, yeni_liste5)
        draw()

        circle_restart_button9 = buttonRestart(5)
        circle_next_button9 = buttonNextGeneral(9)
        page = pageUpdate(9.5)

    # EVENTS --------------------------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            buttonCircleDefinerRestart(mouse_pos)
            buttonCircleDefinerNext(mouse_pos)

            buttonRectDefinerForPage(mouse_pos, 1.5, yeni_liste1, img1)
            buttonRectDefinerForPage(mouse_pos, 3.5, yeni_liste2, img2)
            buttonRectDefinerForPage(mouse_pos, 5.5, yeni_liste3, img3)
            buttonRectDefinerForPage(mouse_pos, 7.5, yeni_liste4, img4)
            buttonRectDefinerForPage(mouse_pos, 9.5, yeni_liste5, img5)
