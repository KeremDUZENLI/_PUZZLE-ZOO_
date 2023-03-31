from globals import *

# Image - 9
img9 = pygame.image.load("5.png")
img9 = pygame.transform.scale(img9, (400, 400))

# Image Split - 9
tileSprite9 = pygame.image.load('5.png')
tileSprite9 = pygame.transform.scale(img9, (400, 400))

yeni_liste9 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste9:
        yeni_liste9.append(r)

print(yeni_liste9)
