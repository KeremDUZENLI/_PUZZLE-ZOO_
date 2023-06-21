from globals import *


def page0():
    screen.fill((255, 255, 255))
    screen.blit(img_background, (0, 0))

    font_main_page = pygame.font.SysFont("calibri", 80, True)
    screen.blit(font_main_page.render("PUZZLE ZOO", True, "black"), (250, 630))

    pygame.draw.circle(screen, (0, 255, 0), [500, 780], 50)
    screen.blit(img_next, (460, 740))


def pageCreate(img, liste):
    screen.fill((255, 255, 255))
    screen.blit(font_default.render("PUZZLE", True, "black"), (350, 50))

    screenBlit(img, liste)


def screenBlit(img, liste):
    screen.blit(img, (liste[0], 760), (0, 0, 200, 200))  # img1
    screen.blit(img, (liste[1], 760), (200, 0, 200, 200))  # img2
    screen.blit(img, (liste[2], 760), (0, 200, 200, 200))  # img2
    screen.blit(img, (liste[3], 760), (200, 200, 200, 200))  # img4


def pictureLocationer(numberInList, liste=None, img=None):
    if img is not None and liste is not None:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(
            numberInList, 760, 200, 200),  1)
        screenBlitListe(liste, numberInList, img)

    else:
        pygame.draw.rect(screen, (255, 0, 0),
                         pygame.Rect(numberInList, 760, 200, 200),  1)

    pygame.display.update()


def screenBlitListe(liste, numberInList, img):
    if liste[0] == numberInList:
        screen.blit(img, (300, 200), (0, 0, 200, 200))  # img1

    if liste[1] == numberInList:
        screen.blit(img, (500, 200), (200, 0, 200, 200))  # img2

    if liste[2] == numberInList:
        screen.blit(img, (300, 400), (0, 200, 200, 200))  # img2

    if liste[3] == numberInList:
        screen.blit(img, (500, 400), (200, 200, 200, 200))  # img4
