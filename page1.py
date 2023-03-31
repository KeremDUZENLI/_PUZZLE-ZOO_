from globals import *

# Image - 1
img1 = pygame.image.load("1.png")
img1 = pygame.transform.scale(img1, (400, 400))

# Image Split - 1
tileSprite1 = pygame.image.load('1.png')
tileSprite1 = pygame.transform.scale(img1, (400, 400))

yeni_liste1 = []

for i in range(100):
    r = random.choice(liste)

    if r not in yeni_liste1:
        yeni_liste1.append(r)

print(yeni_liste1)
