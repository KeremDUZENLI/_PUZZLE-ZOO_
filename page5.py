from globals import *

# Image - 5
img5 = pygame.image.load("3.png")
img5 = pygame.transform.scale(img5, (400, 400))

# Image Split - 5
tileSprite5 = pygame.image.load('3.png')
tileSprite5 = pygame.transform.scale(img5, (400, 400))

yeni_liste5 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste5:
        yeni_liste5.append(r)

print(yeni_liste5)
