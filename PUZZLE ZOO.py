# import the pygame module
from re import X
import pygame
from pygame import mixer
from pygame.locals import*
import random



# Initializing Pygame
pygame.init()

# Set the caption of the screen
pygame.display.set_caption('PUZZLE ZOO')

# Define the dimensions (width,height)
screen = pygame.display.set_mode((1000, 1000))



### GLOBALS --------------------------------------------------------------------------------------------------------
page = 0
liste = [40,280,520,760]

global x
x = 0
running = True


img_background = pygame.image.load("[Background].jpg")
img_background = pygame.transform.scale(img_background, (1000, 1000))

img_restart = pygame.image.load("[Restart].png")
img_restart = pygame.transform.scale(img_restart, (80, 80))

img_next = pygame.image.load("[Next].png")
img_next = pygame.transform.scale(img_next, (80, 80))


rect1a_button = pygame.Rect(0 ,0, 0, 0)
rect2a_button = pygame.Rect(0 ,0, 0, 0)
rect3a_button = pygame.Rect(0 ,0, 0, 0)
rect4a_button = pygame.Rect(0 ,0, 0, 0)


circle_restart_button1 = pygame.Rect(0 ,0, 0, 0)
circle_restart_button3 = pygame.Rect(0 ,0, 0, 0)
circle_restart_button5 = pygame.Rect(0 ,0, 0, 0)
circle_restart_button7 = pygame.Rect(0 ,0, 0, 0)
circle_restart_button9 = pygame.Rect(0 ,0, 0, 0)


circle_next_button1 = pygame.Rect(0, 0, 0, 0)
circle_next_button2 = pygame.Rect(0, 0, 0, 0)
circle_next_button3 = pygame.Rect(0, 0, 0, 0)
circle_next_button4 = pygame.Rect(0, 0, 0, 0)
circle_next_button5 = pygame.Rect(0, 0, 0, 0)
circle_next_button6 = pygame.Rect(0, 0, 0, 0)
circle_next_button7 = pygame.Rect(0, 0, 0, 0)
circle_next_button8 = pygame.Rect(0, 0, 0, 0)
circle_next_button9 = pygame.Rect(0, 0, 0, 0)
circle_next_button10 = pygame.Rect(0, 0, 0, 0)


def rect1a_button_pressed():
	None
	
def rect2a_button_pressed():
	None
	
def rect3a_button_pressed():
	None
	
def rect4a_button_pressed():
	None


def circle_restart_button1_pressed():
	None

def circle_restart_button3_pressed():
	None

def circle_restart_button5_pressed():
	None

def circle_restart_button7_pressed():
	None

def circle_restart_button9_pressed():
	None



### PAGE 1 --------------------------------------------------
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



### PAGE 3 --------------------------------------------------
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



### PAGE 5 --------------------------------------------------
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



### PAGE 7 --------------------------------------------------
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



### PAGE 9 --------------------------------------------------
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



# --------------------------------------------------------------------------------------------------------
while running:

	### PAGES --------------------------------------------------
	if page == 0:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Image Background
		screen.blit(img_background, (0,0))

		# Font
		font_1 = pygame.font.SysFont("calibri", 100, True)
		screen.blit(font_1.render("PUZZLE ZOO", True, "black"), (250, 630))

		# Start Button
		circle_next0 = pygame.draw.circle(screen, (0,255,0), [500, 780], 50)
		screen.blit(img_next, (460, 740))
		circle_next_button0 = pygame.Rect(450, 730, 100, 100)

		# Update
		pygame.display.update()
		page = 0.5

		# Next Button Function - 1
		def circle_next_button0_pressed():
			pygame.display.update()



	if page == 1:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Font
		font_1 = pygame.font.SysFont("calibri", 50, True)
		screen.blit(font_1.render("PUZZLE - 1.", True, "black"), (350, 50))

		# Image Split - 1
		screen.blit(tileSprite1, (yeni_liste1[0], 760), (0, 0, 200, 200)) 	  #img1
		screen.blit(tileSprite1, (yeni_liste1[1], 760), (200, 0, 200, 200))   #img2
		screen.blit(tileSprite1, (yeni_liste1[2], 760), (0, 200, 200, 200))   #img3
		screen.blit(tileSprite1, (yeni_liste1[3], 760), (200, 200, 200, 200)) #img4

		# Rectangles - Middle
		rect1 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 200, 200, 200), 1)
		text1 = screen.blit(font_1.render("1", True, (0,0,0)), (300, 200))

		rect2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 200, 200, 200), 1)
		text2 = screen.blit(font_1.render("2", True, (0,0,0)), (500, 200))

		rect3 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 400, 200, 200), 1)
		text3 = screen.blit(font_1.render("3", True, (0,0,0)), (300, 400))

		rect4 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 400, 200, 200), 1)
		text4 = screen.blit(font_1.render("4", True, (0,0,0)), (500, 400))

		# Rectangles - Bottom
		rect1a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(40, 760, 200, 200),  1)
		rect1a_button = pygame.Rect(40, 760, 200, 200)

		rect2a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(280, 760, 200, 200), 1)
		rect2a_button = pygame.Rect(280, 760, 200, 200)

		rect3a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(520, 760, 200, 200), 1)
		rect3a_button = pygame.Rect(520, 760, 200, 200)

		rect4a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(760, 760, 200, 200), 1)
		rect4a_button = pygame.Rect(760, 760, 200, 200)

		# Line
		pygame.draw.line(screen, (0, 0, 0), (0, 720), (1000, 720), 3)

		# Restart Button - 1
		circle_restart1 = pygame.draw.circle(screen, (255,0,0), [900, 250], 50)
		screen.blit(img_restart, (860, 210))
		circle_restart_button1 = pygame.Rect(850, 200, 100, 100)

		# Next Button - 1
		circle_next1 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button1 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()
		page = 1.5

		# Rectart Button Function - 1
		def circle_restart_button1_pressed():
			pygame.display.update()

		# Next Button Function - 1
		def circle_next_button1_pressed():
			pygame.display.update()



	if page == 1.5:
		if yeni_liste1.index(40) == x:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(40, 760, 200, 200),  1)

				if yeni_liste1[0] == 40:
					screen.blit(tileSprite1, (300, 200), (0, 0, 200, 200)) 		#img1

				if yeni_liste1[1] == 40:
					screen.blit(tileSprite1, (500, 200), (200, 0, 200, 200)) 	#img2

				if yeni_liste1[2] == 40:
					screen.blit(tileSprite1, (300, 400), (0, 200, 200, 200)) 	#img3

				if yeni_liste1[3] == 40:
					screen.blit(tileSprite1, (500, 400), (200, 200, 200, 200)) 	#img4

				pygame.display.update()

		else:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(40, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste1.index(280) == x:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(280, 760, 200, 200), 1)

				if yeni_liste1[0] == 280:
					screen.blit(tileSprite1, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste1[1] == 280:
					screen.blit(tileSprite1, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste1[2] == 280:
					screen.blit(tileSprite1, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste1[3] == 280:
					screen.blit(tileSprite1, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(280, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste1.index(520) == x:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(520, 760, 200, 200), 1)

				if yeni_liste1[0] == 520:
					screen.blit(tileSprite1, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste1[1] == 520:
					screen.blit(tileSprite1, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste1[2] == 520:
					screen.blit(tileSprite1, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste1[3] == 520:
					screen.blit(tileSprite1, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()
				
		else:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(520, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste1.index(760) == x:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(760, 760, 200, 200), 1)

				if yeni_liste1[0] == 760:
					screen.blit(tileSprite1, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste1[1] == 760:
					screen.blit(tileSprite1, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste1[2] == 760:
					screen.blit(tileSprite1, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste1[3] == 760:
					screen.blit(tileSprite1, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(760, 760, 200, 200),  1)
				pygame.display.update()



	if page == 2:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Image Real
		real_img2 = pygame.image.load("1.png")
		real_img2 = pygame.transform.scale(real_img2, (500, 500))
		screen.blit(real_img2, (250,250))

		# Next Button - 2
		circle_next2 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button2 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()

		# Next Button Function - 2
		def circle_next_button2_pressed():
			pygame.display.update()



	if page == 3:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Font
		font_1 = pygame.font.SysFont("calibri", 50, True)
		screen.blit(font_1.render("PUZZLE - 2.", True, "black"), (350, 50))

		# Image Split - 3
		screen.blit(tileSprite3, (yeni_liste3[0], 760), (0, 0, 200, 200)) 	  #img1
		screen.blit(tileSprite3, (yeni_liste3[1], 760), (200, 0, 200, 200))   #img2
		screen.blit(tileSprite3, (yeni_liste3[2], 760), (0, 200, 200, 200))   #img3
		screen.blit(tileSprite3, (yeni_liste3[3], 760), (200, 200, 200, 200)) #img4

		# Rectangles - Middle
		rect1 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 200, 200, 200), 1)
		text1 = screen.blit(font_1.render("1", True, (0,0,0)), (300, 200))

		rect2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 200, 200, 200), 1)
		text2 = screen.blit(font_1.render("2", True, (0,0,0)), (500, 200))

		rect3 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 400, 200, 200), 1)
		text3 = screen.blit(font_1.render("3", True, (0,0,0)), (300, 400))

		rect4 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 400, 200, 200), 1)
		text4 = screen.blit(font_1.render("4", True, (0,0,0)), (500, 400))

		# Rectangles - Bottom
		rect1a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(40, 760, 200, 200),  1)
		rect1a_button = pygame.Rect(40, 760, 200, 200)

		rect2a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(280, 760, 200, 200), 1)
		rect2a_button = pygame.Rect(280, 760, 200, 200)

		rect3a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(520, 760, 200, 200), 1)
		rect3a_button = pygame.Rect(520, 760, 200, 200)

		rect4a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(760, 760, 200, 200), 1)
		rect4a_button = pygame.Rect(760, 760, 200, 200)

		# Line
		pygame.draw.line(screen, (0, 0, 0), (0, 720), (1000, 720), 3)

		# Restart Button - 3
		circle_restart3 = pygame.draw.circle(screen, (255,0,0), [900, 250], 50)
		screen.blit(img_restart, (860, 210))
		circle_restart_button3 = pygame.Rect(850, 200, 100, 100)

		# Next Button - 3
		circle_next3 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button3 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()
		page = 3.5

		# Rectart Button Function - 3
		def circle_restart_button3_pressed():
			pygame.display.update()

		# Next Button Function - 3
		def circle_next_button3_pressed():
			pygame.display.update()



	if page == 3.5:
		if yeni_liste3.index(40) == x:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(40, 760, 200, 200),  1)

				if yeni_liste3[0] == 40:
					screen.blit(tileSprite3, (300, 200), (0, 0, 200, 200)) 		#img1

				if yeni_liste3[1] == 40:
					screen.blit(tileSprite3, (500, 200), (200, 0, 200, 200)) 	#img2

				if yeni_liste3[2] == 40:
					screen.blit(tileSprite3, (300, 400), (0, 200, 200, 200)) 	#img3

				if yeni_liste3[3] == 40:
					screen.blit(tileSprite3, (500, 400), (200, 200, 200, 200)) 	#img4

				pygame.display.update()

		else:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(40, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste3.index(280) == x:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(280, 760, 200, 200), 1)

				if yeni_liste3[0] == 280:
					screen.blit(tileSprite3, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste3[1] == 280:
					screen.blit(tileSprite3, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste3[2] == 280:
					screen.blit(tileSprite3, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste3[3] == 280:
					screen.blit(tileSprite3, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(280, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste3.index(520) == x:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(520, 760, 200, 200), 1)

				if yeni_liste3[0] == 520:
					screen.blit(tileSprite3, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste3[1] == 520:
					screen.blit(tileSprite3, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste3[2] == 520:
					screen.blit(tileSprite3, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste3[3] == 520:
					screen.blit(tileSprite3, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()
				
		else:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(520, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste3.index(760) == x:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(760, 760, 200, 200), 1)

				if yeni_liste3[0] == 760:
					screen.blit(tileSprite3, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste3[1] == 760:
					screen.blit(tileSprite3, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste3[2] == 760:
					screen.blit(tileSprite3, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste3[3] == 760:
					screen.blit(tileSprite3, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(760, 760, 200, 200),  1)
				pygame.display.update()



	if page == 4:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Image Real
		real_img4 = pygame.image.load("2.png")
		real_img4 = pygame.transform.scale(real_img4, (500, 500))
		screen.blit(real_img4, (250,250))

		# Next Button - 4
		circle_next4 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button4 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()

		# Next Button Function - 4
		def circle_next_button4_pressed():
			pygame.display.update()



	if page == 5:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Font
		font_1 = pygame.font.SysFont("calibri", 50, True)
		screen.blit(font_1.render("PUZZLE - 3.", True, "black"), (350, 50))

		# Image Split - 5
		screen.blit(tileSprite5, (yeni_liste5[0], 760), (0, 0, 200, 200)) 	  #img1
		screen.blit(tileSprite5, (yeni_liste5[1], 760), (200, 0, 200, 200))   #img2
		screen.blit(tileSprite5, (yeni_liste5[2], 760), (0, 200, 200, 200))   #img3
		screen.blit(tileSprite5, (yeni_liste5[3], 760), (200, 200, 200, 200)) #img4

		# Rectangles - Middle
		rect1 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 200, 200, 200), 1)
		text1 = screen.blit(font_1.render("1", True, (0,0,0)), (300, 200))

		rect2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 200, 200, 200), 1)
		text2 = screen.blit(font_1.render("2", True, (0,0,0)), (500, 200))

		rect3 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 400, 200, 200), 1)
		text3 = screen.blit(font_1.render("3", True, (0,0,0)), (300, 400))

		rect4 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 400, 200, 200), 1)
		text4 = screen.blit(font_1.render("4", True, (0,0,0)), (500, 400))

		# Rectangles - Bottom
		rect1a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(40, 760, 200, 200),  1)
		rect1a_button = pygame.Rect(40, 760, 200, 200)

		rect2a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(280, 760, 200, 200), 1)
		rect2a_button = pygame.Rect(280, 760, 200, 200)

		rect3a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(520, 760, 200, 200), 1)
		rect3a_button = pygame.Rect(520, 760, 200, 200)

		rect4a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(760, 760, 200, 200), 1)
		rect4a_button = pygame.Rect(760, 760, 200, 200)

		# Line
		pygame.draw.line(screen, (0, 0, 0), (0, 720), (1000, 720), 3)

		# Restart Button - 5
		circle_restart5 = pygame.draw.circle(screen, (255,0,0), [900, 250], 50)
		screen.blit(img_restart, (860, 210))
		circle_restart_button5 = pygame.Rect(850, 200, 100, 100)

		# Next Button - 5
		circle_next5 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button5 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()
		page = 5.5

		# Rectart Button Function - 5
		def circle_restart_button5_pressed():
			pygame.display.update()

		# Next Button Function - 5
		def circle_next_button5_pressed():
			pygame.display.update()



	if page == 5.5:
		if yeni_liste5.index(40) == x:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(40, 760, 200, 200),  1)

				if yeni_liste5[0] == 40:
					screen.blit(tileSprite5, (300, 200), (0, 0, 200, 200)) 		#img1

				if yeni_liste5[1] == 40:
					screen.blit(tileSprite5, (500, 200), (200, 0, 200, 200)) 	#img2

				if yeni_liste5[2] == 40:
					screen.blit(tileSprite5, (300, 400), (0, 200, 200, 200)) 	#img3

				if yeni_liste5[3] == 40:
					screen.blit(tileSprite5, (500, 400), (200, 200, 200, 200)) 	#img4

				pygame.display.update()

		else:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(40, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste5.index(280) == x:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(280, 760, 200, 200), 1)

				if yeni_liste5[0] == 280:
					screen.blit(tileSprite5, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste5[1] == 280:
					screen.blit(tileSprite5, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste5[2] == 280:
					screen.blit(tileSprite5, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste5[3] == 280:
					screen.blit(tileSprite5, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(280, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste5.index(520) == x:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(520, 760, 200, 200), 1)

				if yeni_liste5[0] == 520:
					screen.blit(tileSprite5, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste5[1] == 520:
					screen.blit(tileSprite5, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste5[2] == 520:
					screen.blit(tileSprite5, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste5[3] == 520:
					screen.blit(tileSprite5, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()
				
		else:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(520, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste5.index(760) == x:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(760, 760, 200, 200), 1)

				if yeni_liste5[0] == 760:
					screen.blit(tileSprite5, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste5[1] == 760:
					screen.blit(tileSprite5, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste5[2] == 760:
					screen.blit(tileSprite5, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste5[3] == 760:
					screen.blit(tileSprite5, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(760, 760, 200, 200),  1)
				pygame.display.update()



	if page == 6:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Image Real
		real_img6 = pygame.image.load("3.png")
		real_img6 = pygame.transform.scale(real_img6, (500, 500))
		screen.blit(real_img6, (250,250))

		# Next Button - 6
		circle_next6 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button6 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()

		# Next Button Function - 6
		def circle_next_button6_pressed():
			pygame.display.update()



	if page == 7:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Font
		font_1 = pygame.font.SysFont("calibri", 50, True)
		screen.blit(font_1.render("PUZZLE - 4.", True, "black"), (350, 50))

		# Image Split - 7
		screen.blit(tileSprite7, (yeni_liste7[0], 760), (0, 0, 200, 200)) 	  #img1
		screen.blit(tileSprite7, (yeni_liste7[1], 760), (200, 0, 200, 200))   #img2
		screen.blit(tileSprite7, (yeni_liste7[2], 760), (0, 200, 200, 200))   #img3
		screen.blit(tileSprite7, (yeni_liste7[3], 760), (200, 200, 200, 200)) #img4

		# Rectangles - Middle
		rect1 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 200, 200, 200), 1)
		text1 = screen.blit(font_1.render("1", True, (0,0,0)), (300, 200))

		rect2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 200, 200, 200), 1)
		text2 = screen.blit(font_1.render("2", True, (0,0,0)), (500, 200))

		rect3 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 400, 200, 200), 1)
		text3 = screen.blit(font_1.render("3", True, (0,0,0)), (300, 400))

		rect4 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 400, 200, 200), 1)
		text4 = screen.blit(font_1.render("4", True, (0,0,0)), (500, 400))

		# Rectangles - Bottom
		rect1a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(40, 760, 200, 200),  1)
		rect1a_button = pygame.Rect(40, 760, 200, 200)

		rect2a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(280, 760, 200, 200), 1)
		rect2a_button = pygame.Rect(280, 760, 200, 200)

		rect3a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(520, 760, 200, 200), 1)
		rect3a_button = pygame.Rect(520, 760, 200, 200)

		rect4a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(760, 760, 200, 200), 1)
		rect4a_button = pygame.Rect(760, 760, 200, 200)

		# Line
		pygame.draw.line(screen, (0, 0, 0), (0, 720), (1000, 720), 3)

		# Restart Button - 7
		circle_restart7 = pygame.draw.circle(screen, (255,0,0), [900, 250], 50)
		screen.blit(img_restart, (860, 210))
		circle_restart_button7 = pygame.Rect(850, 200, 100, 100)

		# Next Button - 7
		circle_next7 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button7 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()
		page = 7.5

		# Rectart Button Function - 7
		def circle_restart_button7_pressed():
			pygame.display.update()

		# Next Button Function - 7
		def circle_next_button7_pressed():
			pygame.display.update()



	if page == 7.5:
		if yeni_liste7.index(40) == x:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(40, 760, 200, 200),  1)

				if yeni_liste7[0] == 40:
					screen.blit(tileSprite7, (300, 200), (0, 0, 200, 200)) 		#img1

				if yeni_liste7[1] == 40:
					screen.blit(tileSprite7, (500, 200), (200, 0, 200, 200)) 	#img2

				if yeni_liste7[2] == 40:
					screen.blit(tileSprite7, (300, 400), (0, 200, 200, 200)) 	#img3

				if yeni_liste7[3] == 40:
					screen.blit(tileSprite7, (500, 400), (200, 200, 200, 200)) 	#img4

				pygame.display.update()

		else:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(40, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste7.index(280) == x:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(280, 760, 200, 200), 1)

				if yeni_liste7[0] == 280:
					screen.blit(tileSprite7, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste7[1] == 280:
					screen.blit(tileSprite7, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste7[2] == 280:
					screen.blit(tileSprite7, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste7[3] == 280:
					screen.blit(tileSprite7, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(280, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste7.index(520) == x:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(520, 760, 200, 200), 1)

				if yeni_liste7[0] == 520:
					screen.blit(tileSprite7, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste7[1] == 520:
					screen.blit(tileSprite7, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste7[2] == 520:
					screen.blit(tileSprite7, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste7[3] == 520:
					screen.blit(tileSprite7, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()
				
		else:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(520, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste7.index(760) == x:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(760, 760, 200, 200), 1)

				if yeni_liste7[0] == 760:
					screen.blit(tileSprite7, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste7[1] == 760:
					screen.blit(tileSprite7, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste7[2] == 760:
					screen.blit(tileSprite7, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste7[3] == 760:
					screen.blit(tileSprite7, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(760, 760, 200, 200),  1)
				pygame.display.update()



	if page == 8:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Image Real
		real_img8 = pygame.image.load("4.png")
		real_img8 = pygame.transform.scale(real_img8, (500, 500))
		screen.blit(real_img8, (250,250))

		# Next Button - 8
		circle_next8 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button8 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()

		# Next Button Function - 8
		def circle_next_button8_pressed():
			pygame.display.update()



	if page == 9:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Font
		font_1 = pygame.font.SysFont("calibri", 50, True)
		screen.blit(font_1.render("PUZZLE - 5.", True, "black"), (350, 50))

		# Image Split - 9
		screen.blit(tileSprite9, (yeni_liste9[0], 760), (0, 0, 200, 200)) 	  #img1
		screen.blit(tileSprite9, (yeni_liste9[1], 760), (200, 0, 200, 200))   #img2
		screen.blit(tileSprite9, (yeni_liste9[2], 760), (0, 200, 200, 200))   #img3
		screen.blit(tileSprite9, (yeni_liste9[3], 760), (200, 200, 200, 200)) #img4

		# Rectangles - Middle
		rect1 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 200, 200, 200), 1)
		text1 = screen.blit(font_1.render("1", True, (0,0,0)), (300, 200))

		rect2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 200, 200, 200), 1)
		text2 = screen.blit(font_1.render("2", True, (0,0,0)), (500, 200))

		rect3 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(300, 400, 200, 200), 1)
		text3 = screen.blit(font_1.render("3", True, (0,0,0)), (300, 400))

		rect4 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 400, 200, 200), 1)
		text4 = screen.blit(font_1.render("4", True, (0,0,0)), (500, 400))

		# Rectangles - Bottom
		rect1a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(40, 760, 200, 200),  1)
		rect1a_button = pygame.Rect(40, 760, 200, 200)

		rect2a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(280, 760, 200, 200), 1)
		rect2a_button = pygame.Rect(280, 760, 200, 200)

		rect3a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(520, 760, 200, 200), 1)
		rect3a_button = pygame.Rect(520, 760, 200, 200)

		rect4a = pygame.draw.rect(screen, (0,0,0), pygame.Rect(760, 760, 200, 200), 1)
		rect4a_button = pygame.Rect(760, 760, 200, 200)

		# Line
		pygame.draw.line(screen, (0, 0, 0), (0, 720), (1000, 720), 3)

		# Restart Button - 9
		circle_restart9 = pygame.draw.circle(screen, (255,0,0), [900, 250], 50)
		screen.blit(img_restart, (860, 210))
		circle_restart_button9 = pygame.Rect(850, 200, 100, 100)

		# Next Button - 9
		circle_next9 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button9 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()
		page = 9.5

		# Rectart Button Function - 9
		def circle_restart_button9_pressed():
			pygame.display.update()

		# Next Button Function - 9
		def circle_next_button9_pressed():
			pygame.display.update()



	if page == 9.5:
		if yeni_liste9.index(40) == x:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(40, 760, 200, 200),  1)

				if yeni_liste9[0] == 40:
					screen.blit(tileSprite9, (300, 200), (0, 0, 200, 200)) 		#img1

				if yeni_liste9[1] == 40:
					screen.blit(tileSprite9, (500, 200), (200, 0, 200, 200)) 	#img2

				if yeni_liste9[2] == 40:
					screen.blit(tileSprite9, (300, 400), (0, 200, 200, 200)) 	#img3

				if yeni_liste9[3] == 40:
					screen.blit(tileSprite9, (500, 400), (200, 200, 200, 200)) 	#img4

				pygame.display.update()

		else:
			def rect1a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(40, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste9.index(280) == x:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(280, 760, 200, 200), 1)

				if yeni_liste9[0] == 280:
					screen.blit(tileSprite9, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste9[1] == 280:
					screen.blit(tileSprite9, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste9[2] == 280:
					screen.blit(tileSprite9, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste9[3] == 280:
					screen.blit(tileSprite9, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect2a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(280, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste9.index(520) == x:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(520, 760, 200, 200), 1)

				if yeni_liste9[0] == 520:
					screen.blit(tileSprite9, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste9[1] == 520:
					screen.blit(tileSprite9, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste9[2] == 520:
					screen.blit(tileSprite9, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste9[3] == 520:
					screen.blit(tileSprite9, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()
				
		else:
			def rect3a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(520, 760, 200, 200),  1)
				pygame.display.update()


		if yeni_liste9.index(760) == x:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(760, 760, 200, 200), 1)

				if yeni_liste9[0] == 760:
					screen.blit(tileSprite9, (300, 200), (0, 0, 200, 200))		#img1

				if yeni_liste9[1] == 760:
					screen.blit(tileSprite9, (500, 200), (200, 0, 200, 200))	#img2

				if yeni_liste9[2] == 760:
					screen.blit(tileSprite9, (300, 400), (0, 200, 200, 200))	#img3

				if yeni_liste9[3] == 760:
					screen.blit(tileSprite9, (500, 400), (200, 200, 200, 200))	#img4

				pygame.display.update()

		else:
			def rect4a_button_pressed():
				pygame.draw.rect(screen, (255,0,0), pygame.Rect(760, 760, 200, 200),  1)
				pygame.display.update()



	if page == 10:
		# Fill the background colour to the screen
		screen.fill((255, 255, 255))

		# Image Real
		real_img10 = pygame.image.load("5.png")
		real_img10 = pygame.transform.scale(real_img10, (500, 500))
		screen.blit(real_img10, (250,250))

		# Next Button - 10
		circle_next10 = pygame.draw.circle(screen, (0,255,0), [900, 550], 50)
		screen.blit(img_next, (860, 510))
		circle_next_button10 = pygame.Rect(850, 500, 100, 100)

		# Update
		pygame.display.update()

		# Next Button Function - 10
		def circle_next_button10_pressed():
			pygame.display.update()





	### EVENTS --------------------------------------------------

	# Event Queue
	for event in pygame.event.get():

		# Quit
		if event.type == pygame.QUIT:
			running = False

		# Mouse Activity
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = event.pos



			#-- Page 0 ----------------------------------------------------------------------
			if (circle_next_button0.collidepoint(mouse_pos)) & (page == 0.5):
				circle_next_button0_pressed()
				page = 1



			#-- Page 1 ----------------------------------------------------------------------
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
				circle_restart_button1_pressed()
				page = 1
				x = 0

			if (circle_next_button1.collidepoint(mouse_pos)):
				circle_next_button1_pressed()
				page = 2



			#-- Page 2 ----------------------------------------------------------------------
			if (circle_next_button2.collidepoint(mouse_pos)):
				circle_next_button2_pressed()
				page = 3
				x = 0



			#-- Page 3 ----------------------------------------------------------------------
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

			if (circle_restart_button3.collidepoint(mouse_pos)):
				circle_restart_button3_pressed()
				page = 3
				x = 0

			if (circle_next_button3.collidepoint(mouse_pos)):
				circle_next_button3_pressed()
				page = 4



			#-- Page 4 ----------------------------------------------------------------------
			if (circle_next_button4.collidepoint(mouse_pos)):
				circle_next_button4_pressed()
				page = 5
				x = 0



			#-- Page 5 ----------------------------------------------------------------------
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

			if (circle_restart_button5.collidepoint(mouse_pos)):
				circle_restart_button5_pressed()
				page = 5
				x = 0

			if (circle_next_button5.collidepoint(mouse_pos)):
				circle_next_button5_pressed()
				page = 6



			#-- Page 6 ----------------------------------------------------------------------
			if (circle_next_button6.collidepoint(mouse_pos)):
				circle_next_button6_pressed()
				page = 7
				x = 0



			#-- Page 7 ----------------------------------------------------------------------
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

			if (circle_restart_button7.collidepoint(mouse_pos)):
				circle_restart_button7_pressed()
				page = 7
				x = 0

			if (circle_next_button7.collidepoint(mouse_pos)):
				circle_next_button7_pressed()
				page = 8



			#-- Page 8 ----------------------------------------------------------------------
			if (circle_next_button8.collidepoint(mouse_pos)):
				circle_next_button8_pressed()
				page = 9
				x = 0



			#-- Page 9 ----------------------------------------------------------------------
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

			if (circle_restart_button9.collidepoint(mouse_pos)):
				circle_restart_button9_pressed()
				page = 9
				x = 0

			if (circle_next_button9.collidepoint(mouse_pos)):
				circle_next_button9_pressed()
				page = 10



			#-- Page 10 ----------------------------------------------------------------------
			if (circle_next_button10.collidepoint(mouse_pos)):
				circle_next_button10_pressed()
				page = 11
				x = 0


