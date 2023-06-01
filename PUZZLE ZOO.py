# import the pygame module
from re import X
from pygame import mixer
from pygame.locals import *

from init import *
from globals import *
from page1 import *
from page3 import *
from page5 import *
from page7 import *
from page9 import *


# Initializing Pygame


# GLOBALS --------------------------------------------------------------------------------------------------------


# PAGE 1 --------------------------------------------------


# PAGE 3 --------------------------------------------------


# PAGE 5 --------------------------------------------------


# PAGE 7 --------------------------------------------------


# PAGE 9 --------------------------------------------------


# --------------------------------------------------------------------------------------------------------
font_1 = pygame.font.SysFont("calibri", 50, True)
# --------------------------------------------------------------------------------------------------------


def page0():
    # Fill the background colour to the screen
    screen.fill((255, 255, 255))

    # Image Background
    screen.blit(img_background, (0, 0))

    # Font
    font_1 = pygame.font.SysFont("calibri", 100, True)
    screen.blit(font_1.render("PUZZLE ZOO", True, "black"), (250, 630))

    # Start Button
    pygame.draw.circle(screen, (0, 255, 0), [500, 780], 50)
    screen.blit(img_next, (460, 740))


def pageCreate(tileSprite, liste):
    # Fill the background colour to the screen
    screen.fill((255, 255, 255))

    # Font
    screen.blit(font_1.render("PUZZLE", True, "black"), (350, 50))

    # Image Split - 1
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
    # Rectangles - Middle
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(300, 200, 200, 200), 1)
    screen.blit(font_1.render("1", True, (0, 0, 0)), (300, 200))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 200, 200, 200), 1)
    screen.blit(font_1.render("2", True, (0, 0, 0)), (500, 200))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(300, 400, 200, 200), 1)
    screen.blit(font_1.render("3", True, (0, 0, 0)), (300, 400))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(500, 400, 200, 200), 1)
    screen.blit(font_1.render("4", True, (0, 0, 0)), (500, 400))


def drawBottomRectangles():
    # Rectangles - Bottom
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(40, 760, 200, 200),  1)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(280, 760, 200, 200), 1)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(520, 760, 200, 200), 1)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(760, 760, 200, 200), 1)


def drawLine():
    # Line
    pygame.draw.line(screen, (0, 0, 0), (0, 720), (1000, 720), 3)


def buttonRestart(number: int):
    # Restart Button
    pygame.draw.circle(screen, (255, 0, 0), [900, 250], 50)
    screen.blit(img_restart, (860, 210))

    if number == 1:
        global circle_restart_button1
        circle_restart_button1 = pygame.Rect(850, 200, 100, 100)

    if number == 2:
        global circle_restart_button2
        circle_restart_button2 = pygame.Rect(850, 200, 100, 100)

    if number == 3:
        global circle_restart_button3
        circle_restart_button3 = pygame.Rect(850, 200, 100, 100)

    if number == 4:
        global circle_restart_button4
        circle_restart_button4 = pygame.Rect(850, 200, 100, 100)

    if number == 5:
        global circle_restart_button5
        circle_restart_button5 = pygame.Rect(850, 200, 100, 100)


def buttonNext(number: int):
    # Next Button - 1
    pygame.draw.circle(screen, (0, 255, 0), [900, 550], 50)
    screen.blit(img_next, (860, 510))

    if number == 1:
        global circle_next_button1
        circle_next_button1 = pygame.Rect(850, 500, 100, 100)

    if number == 2:
        global circle_next_button2
        circle_next_button2 = pygame.Rect(850, 500, 100, 100)

    if number == 3:
        global circle_next_button3
        circle_next_button3 = pygame.Rect(850, 500, 100, 100)

    if number == 4:
        global circle_next_button4
        circle_next_button4 = pygame.Rect(850, 500, 100, 100)

    if number == 5:
        global circle_next_button5
        circle_next_button5 = pygame.Rect(850, 500, 100, 100)

    if number == 6:
        global circle_next_button6
        circle_next_button6 = pygame.Rect(850, 500, 100, 100)

    if number == 7:
        global circle_next_button7
        circle_next_button7 = pygame.Rect(850, 500, 100, 100)

    if number == 8:
        global circle_next_button8
        circle_next_button8 = pygame.Rect(850, 500, 100, 100)

    if number == 9:
        global circle_next_button9
        circle_next_button9 = pygame.Rect(850, 500, 100, 100)

    if number == 10:
        global circle_next_button10
        circle_next_button10 = pygame.Rect(850, 500, 100, 100)


def pageUpdate(number: float):
    pygame.display.update()
    global page
    page = number


# --------------------------------------------------------------------------------------------------------
while running:

    # PAGES --------------------------------------------------
    if page == 0:
        page0()
        circle_next_button0 = pygame.Rect(450, 730, 100, 100)
        pageUpdate(0.5)

    # Next Button Function - 1
    def circle_next_button0_pressed():
        pygame.display.update()

    if page == 1:
        pageCreate(tileSprite1, yeni_liste1)

        # Rectangles - Middle
        drawMiddleRectangles()

        # Rectangles - Bottom
        drawBottomRectangles()

        # Line
        drawLine()

        # Restart Button
        buttonRestart(1)

        # Next Button
        buttonNext(1)

        # Update
        pageUpdate(1.5)

        # Next Button Function - 1
        def circle_next_button1_pressed():
            pygame.display.update()

    if page == 1.5:
        if yeni_liste1.index(40) == x:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)

                screenBlitListe(tileSprite1, yeni_liste1, 40)

                pygame.display.update()

        else:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste1.index(280) == x:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(280, 760, 200, 200), 1)

                screenBlitListe(tileSprite1, yeni_liste1, 280)

                pygame.display.update()

        else:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(280, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste1.index(520) == x:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(520, 760, 200, 200), 1)

                screenBlitListe(tileSprite1, yeni_liste1, 520)

                pygame.display.update()

        else:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(520, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste1.index(760) == x:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(760, 760, 200, 200), 1)

                screenBlitListe(tileSprite1, yeni_liste1, 760)

                pygame.display.update()

        else:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(760, 760, 200, 200),  1)
                pygame.display.update()

    if page == 2:
        # Fill the background colour to the screen
        screen.fill((255, 255, 255))

        # Image Real
        real_img2 = pygame.image.load("1.png")
        real_img2 = pygame.transform.scale(real_img2, (500, 500))
        screen.blit(real_img2, (250, 250))

        # Next Button
        buttonNext(2)

        # Update
        pygame.display.update()

        # Next Button Function - 2
        def circle_next_button2_pressed():
            pygame.display.update()

    if page == 3:
        pageCreate(tileSprite3, yeni_liste3)

        # Rectangles - Middle
        drawMiddleRectangles()

        # Rectangles - Bottom
        drawBottomRectangles()

        # Line
        drawLine()

        # Restart Button
        buttonRestart(2)

        # Next Button
        buttonNext(3)

        # Update
        pageUpdate(3.5)

        # Next Button Function - 3
        def circle_next_button3_pressed():
            pygame.display.update()

    if page == 3.5:
        if yeni_liste3.index(40) == x:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)

                screenBlitListe(tileSprite3, yeni_liste3, 40)

                pygame.display.update()

        else:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste3.index(280) == x:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(280, 760, 200, 200), 1)

                screenBlitListe(tileSprite3, yeni_liste3, 280)

                pygame.display.update()

        else:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(280, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste3.index(520) == x:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(520, 760, 200, 200), 1)

                screenBlitListe(tileSprite3, yeni_liste3, 520)

                pygame.display.update()

        else:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(520, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste3.index(760) == x:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(760, 760, 200, 200), 1)

                screenBlitListe(tileSprite3, yeni_liste3, 760)

                pygame.display.update()

        else:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(760, 760, 200, 200),  1)
                pygame.display.update()

    if page == 4:
        # Fill the background colour to the screen
        screen.fill((255, 255, 255))

        # Image Real
        real_img4 = pygame.image.load("2.png")
        real_img4 = pygame.transform.scale(real_img4, (500, 500))
        screen.blit(real_img4, (250, 250))

        # Next Button
        buttonNext(4)

        # Update
        pygame.display.update()

        # Next Button Function - 4
        def circle_next_button4_pressed():
            pygame.display.update()

    if page == 5:
        pageCreate(tileSprite5, yeni_liste5)

        # Rectangles - Middle
        drawMiddleRectangles()

        # Rectangles - Bottom
        drawBottomRectangles()

        # Line
        drawLine()

        # Restart Button
        buttonRestart(3)

        # Next Button
        buttonNext(5)

        # Update
        pageUpdate(5.5)

        # Next Button Function - 5
        def circle_next_button5_pressed():
            pygame.display.update()

    if page == 5.5:
        if yeni_liste5.index(40) == x:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)

                screenBlitListe(tileSprite5, yeni_liste5, 40)

                pygame.display.update()

        else:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste5.index(280) == x:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(280, 760, 200, 200), 1)

                screenBlitListe(tileSprite5, yeni_liste5, 280)

                pygame.display.update()

        else:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(280, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste5.index(520) == x:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(520, 760, 200, 200), 1)

                screenBlitListe(tileSprite5, yeni_liste5, 520)

                pygame.display.update()

        else:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(520, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste5.index(760) == x:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(760, 760, 200, 200), 1)

                screenBlitListe(tileSprite5, yeni_liste5, 760)

                pygame.display.update()

        else:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(760, 760, 200, 200),  1)
                pygame.display.update()

    if page == 6:
        # Fill the background colour to the screen
        screen.fill((255, 255, 255))

        # Image Real
        real_img6 = pygame.image.load("3.png")
        real_img6 = pygame.transform.scale(real_img6, (500, 500))
        screen.blit(real_img6, (250, 250))

        # Next Button
        buttonNext(6)

        # Update
        pygame.display.update()

        # Next Button Function - 6
        def circle_next_button6_pressed():
            pygame.display.update()

    if page == 7:
        pageCreate(tileSprite7, yeni_liste7)

        # Rectangles - Middle
        drawMiddleRectangles()

        # Rectangles - Bottom
        drawBottomRectangles()

        # Line
        drawLine()

        # Restart Button
        buttonRestart(4)

        # Next Button
        buttonNext(7)

        # Update
        pageUpdate(7.5)

        # Next Button Function - 7
        def circle_next_button7_pressed():
            pygame.display.update()

    if page == 7.5:
        if yeni_liste7.index(40) == x:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)

                screenBlitListe(tileSprite7, yeni_liste7, 40)

                pygame.display.update()

        else:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste7.index(280) == x:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(280, 760, 200, 200), 1)

                screenBlitListe(tileSprite7, yeni_liste7, 280)

                pygame.display.update()

        else:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(280, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste7.index(520) == x:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(520, 760, 200, 200), 1)

                screenBlitListe(tileSprite7, yeni_liste7, 520)

                pygame.display.update()

        else:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(520, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste7.index(760) == x:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(760, 760, 200, 200), 1)

                screenBlitListe(tileSprite7, yeni_liste7, 760)

                pygame.display.update()

        else:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(760, 760, 200, 200),  1)
                pygame.display.update()

    if page == 8:
        # Fill the background colour to the screen
        screen.fill((255, 255, 255))

        # Image Real
        real_img8 = pygame.image.load("4.png")
        real_img8 = pygame.transform.scale(real_img8, (500, 500))
        screen.blit(real_img8, (250, 250))

        # Next Button
        buttonNext(8)

        # Update
        pygame.display.update()

        # Next Button Function - 8
        def circle_next_button8_pressed():
            pygame.display.update()

    if page == 9:
        pageCreate(tileSprite9, yeni_liste9)

        # Rectangles - Middle
        drawMiddleRectangles()

        # Rectangles - Bottom
        drawBottomRectangles()

        # Line
        drawLine()

        # Restart Button
        buttonRestart(5)

        # Next Button
        buttonNext(9)

        # Update
        pageUpdate(9.5)

        # Next Button Function - 9
        def circle_next_button9_pressed():
            pygame.display.update()

    if page == 9.5:
        if yeni_liste9.index(40) == x:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)

                screenBlitListe(tileSprite9, yeni_liste9, 40)

                pygame.display.update()

        else:
            def rect1a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(40, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste9.index(280) == x:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(280, 760, 200, 200), 1)

                screenBlitListe(tileSprite9, yeni_liste9, 280)

                pygame.display.update()

        else:
            def rect2a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(280, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste9.index(520) == x:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(520, 760, 200, 200), 1)

                screenBlitListe(tileSprite9, yeni_liste9, 520)

                pygame.display.update()

        else:
            def rect3a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(520, 760, 200, 200),  1)
                pygame.display.update()

        if yeni_liste9.index(760) == x:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (0, 255, 0),
                                 pygame.Rect(760, 760, 200, 200), 1)

                screenBlitListe(tileSprite9, yeni_liste9, 760)

                pygame.display.update()

        else:
            def rect4a_button_pressed():
                pygame.draw.rect(screen, (255, 0, 0),
                                 pygame.Rect(760, 760, 200, 200),  1)
                pygame.display.update()

    if page == 10:
        # Fill the background colour to the screen
        screen.fill((255, 255, 255))

        # Image Real
        real_img10 = pygame.image.load("5.png")
        real_img10 = pygame.transform.scale(real_img10, (500, 500))
        screen.blit(real_img10, (250, 250))

        # Next Button
        buttonNext(10)

        # Update
        pygame.display.update()

        # Next Button Function - 10
        def circle_next_button10_pressed():
            pygame.display.update()

    # EVENTS --------------------------------------------------

    # Event Queue
    for event in pygame.event.get():

        # Quit
        if event.type == pygame.QUIT:
            running = False

        # Mouse Activity
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # -- Page 0 ----------------------------------------------------------------------
            if (circle_next_button0.collidepoint(mouse_pos)) & (page == 0.5):
                circle_next_button0_pressed()
                page = 1

            # -- Page 1 ----------------------------------------------------------------------
            if (rect1a_button.collidepoint(mouse_pos)) & (page == 1.5):
                rect1a_button_pressed()
                x = x + 1

            if (rect2a_button.collidepoint(mouse_pos)) & (page == 1.5):
                rect2a_button_pressed()
                x = x + 1

            if (rect3a_button.collidepoint(mouse_pos)) & (page == 1.5):
                rect3a_button_pressed()
                x = x + 1

            if (rect4a_button.collidepoint(mouse_pos)) & (page == 1.5):
                rect4a_button_pressed()
                x = x + 1

            if (circle_restart_button1.collidepoint(mouse_pos)):
                pygame.display.update()
                page = 1
                x = 0

            if (circle_next_button1.collidepoint(mouse_pos)):
                circle_next_button1_pressed()
                page = 2

            # -- Page 2 ----------------------------------------------------------------------
            if (circle_next_button2.collidepoint(mouse_pos)):
                circle_next_button2_pressed()
                page = 3
                x = 0

            # -- Page 3 ----------------------------------------------------------------------
            if (rect1a_button.collidepoint(mouse_pos)) & (page == 3.5):
                rect1a_button_pressed()
                x = x + 1

            if (rect2a_button.collidepoint(mouse_pos)) & (page == 3.5):
                rect2a_button_pressed()
                x = x + 1

            if (rect3a_button.collidepoint(mouse_pos)) & (page == 3.5):
                rect3a_button_pressed()
                x = x + 1

            if (rect4a_button.collidepoint(mouse_pos)) & (page == 3.5):
                rect4a_button_pressed()
                x = x + 1

            if (circle_restart_button2.collidepoint(mouse_pos)):
                pygame.display.update()
                page = 3
                x = 0

            if (circle_next_button3.collidepoint(mouse_pos)):
                circle_next_button3_pressed()
                page = 4

            # -- Page 4 ----------------------------------------------------------------------
            if (circle_next_button4.collidepoint(mouse_pos)):
                circle_next_button4_pressed()
                page = 5
                x = 0

            # -- Page 5 ----------------------------------------------------------------------
            if (rect1a_button.collidepoint(mouse_pos)) & (page == 5.5):
                rect1a_button_pressed()
                x = x + 1

            if (rect2a_button.collidepoint(mouse_pos)) & (page == 5.5):
                rect2a_button_pressed()
                x = x + 1

            if (rect3a_button.collidepoint(mouse_pos)) & (page == 5.5):
                rect3a_button_pressed()
                x = x + 1

            if (rect4a_button.collidepoint(mouse_pos)) & (page == 5.5):
                rect4a_button_pressed()
                x = x + 1

            if (circle_restart_button3.collidepoint(mouse_pos)):
                pygame.display.update()
                page = 5
                x = 0

            if (circle_next_button5.collidepoint(mouse_pos)):
                circle_next_button5_pressed()
                page = 6

            # -- Page 6 ----------------------------------------------------------------------
            if (circle_next_button6.collidepoint(mouse_pos)):
                circle_next_button6_pressed()
                page = 7
                x = 0

            # -- Page 7 ----------------------------------------------------------------------
            if (rect1a_button.collidepoint(mouse_pos)) & (page == 7.5):
                rect1a_button_pressed()
                x = x + 1

            if (rect2a_button.collidepoint(mouse_pos)) & (page == 7.5):
                rect2a_button_pressed()
                x = x + 1

            if (rect3a_button.collidepoint(mouse_pos)) & (page == 7.5):
                rect3a_button_pressed()
                x = x + 1

            if (rect4a_button.collidepoint(mouse_pos)) & (page == 7.5):
                rect4a_button_pressed()
                x = x + 1

            if (circle_restart_button4.collidepoint(mouse_pos)):
                pygame.display.update()
                page = 7
                x = 0

            if (circle_next_button7.collidepoint(mouse_pos)):
                circle_next_button7_pressed()
                page = 8

            # -- Page 8 ----------------------------------------------------------------------
            if (circle_next_button8.collidepoint(mouse_pos)):
                circle_next_button8_pressed()
                page = 9
                x = 0

            # -- Page 9 ----------------------------------------------------------------------
            if (rect1a_button.collidepoint(mouse_pos)) & (page == 9.5):
                rect1a_button_pressed()
                x = x + 1

            if (rect2a_button.collidepoint(mouse_pos)) & (page == 9.5):
                rect2a_button_pressed()
                x = x + 1

            if (rect3a_button.collidepoint(mouse_pos)) & (page == 9.5):
                rect3a_button_pressed()
                x = x + 1

            if (rect4a_button.collidepoint(mouse_pos)) & (page == 9.5):
                rect4a_button_pressed()
                x = x + 1

            if (circle_restart_button5.collidepoint(mouse_pos)):
                pygame.display.update()
                page = 9
                x = 0

            if (circle_next_button9.collidepoint(mouse_pos)):
                circle_next_button9_pressed()
                page = 10

            # -- Page 10 ----------------------------------------------------------------------
            if (circle_next_button10.collidepoint(mouse_pos)):
                circle_next_button10_pressed()
                page = 11
                x = 0
