import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("The game is Til")
icon = pygame.image.load("image/aimLogo.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("image/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = random.randint(0, 255), random.randint(0, 255), random.randint(0)

running = True
while running:
    pass

pygame.quit()