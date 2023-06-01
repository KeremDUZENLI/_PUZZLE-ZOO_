import random
from init import *

page = 0
liste = [40, 280, 520, 760]

global x
x = 0
running = True


img_background = pygame.image.load("[Background].jpg")
img_background = pygame.transform.scale(img_background, (1000, 1000))

img_restart = pygame.image.load("[Restart].png")
img_restart = pygame.transform.scale(img_restart, (80, 80))

img_next = pygame.image.load("[Next].png")
img_next = pygame.transform.scale(img_next, (80, 80))


rect1a_button = pygame.Rect(40, 760, 200, 200)
rect2a_button = pygame.Rect(280, 760, 200, 200)
rect3a_button = pygame.Rect(520, 760, 200, 200)
rect4a_button = pygame.Rect(760, 760, 200, 200)


circle_restart_button1 = pygame.Rect(0, 0, 0, 0)
circle_restart_button2 = pygame.Rect(0, 0, 0, 0)
circle_restart_button3 = pygame.Rect(0, 0, 0, 0)
circle_restart_button4 = pygame.Rect(0, 0, 0, 0)
circle_restart_button5 = pygame.Rect(0, 0, 0, 0)


circle_next_button0 = pygame.Rect(0, 0, 0, 0)
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
