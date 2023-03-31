from globals import *

# Image - 7
img7 = pygame.image.load("4.png")
img7 = pygame.transform.scale(img7, (400, 400))

# Image Split - 7
tileSprite7 = pygame.image.load('4.png')
tileSprite7 = pygame.transform.scale(img7, (400, 400))

yeni_liste7 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste7:
        yeni_liste7.append(r)

print(yeni_liste7)
