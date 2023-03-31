from globals import *

# Image - 3
img3 = pygame.image.load("2.png")
img3 = pygame.transform.scale(img3, (400, 400))

# Image Split - 3
tileSprite3 = pygame.image.load('2.png')
tileSprite3 = pygame.transform.scale(img3, (400, 400))

yeni_liste3 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste3:
        yeni_liste3.append(r)

print(yeni_liste3)
