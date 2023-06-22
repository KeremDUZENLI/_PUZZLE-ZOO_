from globals import *


def draw():
    drawMiddleRectangles()
    drawBottomRectangles()
    drawLine()


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


def page0():
    screen.fill((255, 255, 255))
    screen.blit(img_background, (0, 0))

    font_main_page = pygame.font.SysFont("calibri", 80, True)
    screen.blit(font_main_page.render("PUZZLE ZOO", True, "black"), (250, 630))

    pygame.draw.circle(screen, (0, 255, 0), [500, 780], 50)
    screen.blit(img_next, (460, 740))


def imageProvider(image):
    screen.fill((255, 255, 255))

    real_img = pygame.image.load(image)
    real_img = pygame.transform.scale(real_img, (500, 500))
    screen.blit(real_img, (250, 250))


def pageUpdate(number: float):
    pygame.display.update()
    page = number
    return page


def imageLoader(path: str):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (400, 400))


def listMixer():
    yeni_liste = []
    for _ in range(100):
        r = random.choice(liste)

        if r not in yeni_liste:
            yeni_liste.append(r)

    return yeni_liste


img1 = imageLoader("images/1.png")
img2 = imageLoader("images/2.png")
img3 = imageLoader("images/3.png")
img4 = imageLoader("images/4.png")
img5 = imageLoader("images/5.png")

yeni_liste1 = listMixer()
yeni_liste2 = listMixer()
yeni_liste3 = listMixer()
yeni_liste4 = listMixer()
yeni_liste5 = listMixer()
