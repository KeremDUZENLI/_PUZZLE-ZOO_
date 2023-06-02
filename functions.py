from re import X
from pygame import mixer
from pygame.locals import *

from init import *
from globals import *


def page0():
    screen.fill((255, 255, 255))
    screen.blit(img_background, (0, 0))

    font_main_page = pygame.font.SysFont("calibri", 80, True)
    screen.blit(font_main_page.render("PUZZLE ZOO", True, "black"), (250, 630))

    pygame.draw.circle(screen, (0, 255, 0), [500, 780], 50)
    screen.blit(img_next, (460, 740))


def pageCreate(tileSprite, liste):
    screen.fill((255, 255, 255))
    screen.blit(font_default.render("PUZZLE", True, "black"), (350, 50))

    screenBlit(tileSprite, liste)


def screenBlit(tileSprite, liste):
    screen.blit(tileSprite, (liste[0], 760), (0, 0, 200, 200))  # img1
    screen.blit(tileSprite, (liste[1], 760), (200, 0, 200, 200))  # img2
    screen.blit(tileSprite, (liste[2], 760), (0, 200, 200, 200))  # img3
    screen.blit(tileSprite, (liste[3], 760), (200, 200, 200, 200))  # img4


def screenBlitListe(liste, numberInList, tileSprite):
    if liste[0] == numberInList:
        screen.blit(tileSprite, (300, 200), (0, 0, 200, 200))  # img1

    if liste[1] == numberInList:
        screen.blit(tileSprite, (500, 200), (200, 0, 200, 200))  # img2

    if liste[2] == numberInList:
        screen.blit(tileSprite, (300, 400), (0, 200, 200, 200))  # img3

    if liste[3] == numberInList:
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


def pictureLocationer(numberInList, liste=None, tileSprite=None):
    if tileSprite is not None and liste is not None:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(
            numberInList, 760, 200, 200),  1)
        screenBlitListe(liste, numberInList, tileSprite)

    else:
        pygame.draw.rect(screen, (255, 0, 0),
                         pygame.Rect(numberInList, 760, 200, 200),  1)

    pygame.display.update()


def imageProvider(image):
    screen.fill((255, 255, 255))

    real_img = pygame.image.load(image)
    real_img = pygame.transform.scale(real_img, (500, 500))
    screen.blit(real_img, (250, 250))


def pageUpdate(number: float):
    pygame.display.update()
    page = number
    return page
