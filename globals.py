import pygame
import random


pygame.init()
pygame.display.set_caption("PUZZLE ZOO")
screen = pygame.display.set_mode((1000, 1000))


page = 0
liste = [40, 280, 520, 760]
running = True
clickAmount = 0


font_default = pygame.font.SysFont("calibri", 50, True)

img_background = pygame.image.load("images/[Background].jpg")
img_background = pygame.transform.scale(img_background, (1000, 1000))

img_restart = pygame.image.load("images/[Restart].png")
img_restart = pygame.transform.scale(img_restart, (80, 80))

img_next = pygame.image.load("images/[Next].png")
img_next = pygame.transform.scale(img_next, (80, 80))


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
