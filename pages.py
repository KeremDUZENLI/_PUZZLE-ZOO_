import random

from globals import *


# PAGE_1----------------------------------------------------------------
# Image - 1
img1 = pygame.image.load("images/1.png")
img1 = pygame.transform.scale(img1, (400, 400))

# Image Split - 1
tileSprite1 = pygame.image.load("images/1.png")
tileSprite1 = pygame.transform.scale(img1, (400, 400))

yeni_liste1 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste1:
        yeni_liste1.append(r)


# PAGE_3----------------------------------------------------------------
# Image - 3
img3 = pygame.image.load("images/2.png")
img3 = pygame.transform.scale(img3, (400, 400))

# Image Split - 3
tileSprite3 = pygame.image.load("images/2.png")
tileSprite3 = pygame.transform.scale(img3, (400, 400))

yeni_liste3 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste3:
        yeni_liste3.append(r)


# PAGE_5----------------------------------------------------------------
# Image - 5
img5 = pygame.image.load("images/3.png")
img5 = pygame.transform.scale(img5, (400, 400))

# Image Split - 5
tileSprite5 = pygame.image.load("images/3.png")
tileSprite5 = pygame.transform.scale(img5, (400, 400))

yeni_liste5 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste5:
        yeni_liste5.append(r)


# PAGE_7----------------------------------------------------------------
# Image - 7
img7 = pygame.image.load("images/4.png")
img7 = pygame.transform.scale(img7, (400, 400))

# Image Split - 7
tileSprite7 = pygame.image.load("images/4.png")
tileSprite7 = pygame.transform.scale(img7, (400, 400))

yeni_liste7 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste7:
        yeni_liste7.append(r)


# PAGE_9----------------------------------------------------------------
# Image - 9
img9 = pygame.image.load("images/5.png")
img9 = pygame.transform.scale(img9, (400, 400))

# Image Split - 9
tileSprite9 = pygame.image.load("images/5.png")
tileSprite9 = pygame.transform.scale(img9, (400, 400))

yeni_liste9 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste9:
        yeni_liste9.append(r)
