"""
# @Author Nicholaus, Isack Thomas
# ID: 20195032
# Dongseo University 
# Computer Engineering 
# Department of Computer Engineering
""" 

"""
NOTE: Press left click of the mouse on the black surface (window) to draw 
        your polygon.
"""
import pygame
from sys import exit
import numpy as np

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)

# background_image_filename = '../images/curve_pattern.png'

# background = pygame.image.load(background_image_filename).convert()
# width, height = background.get_size()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Drawing Polygon")

# screen.blit(background, (0, 0))

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DEEP_PINK = (255, 0, 0)

clock = pygame.time.Clock()
i = 0
point1 = np.array([0, 0])
point2 = np.array([0, 0])
done = False
while not done:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 2 or event.button == 3:
                if i%2 == 0:
                    x, y = pygame.mouse.get_pos()
                    point1 = np.array([x, y])
                    height = 10
                    width = 10
                    if event.button == 1:
                        pygame.draw.rect(screen, DEEP_PINK, (x - width//2, y-height//2,  width, height),3)
                    elif event.button == 2:
                        pygame.draw.rect(screen, BLUE, (x - width//2, y-height//2,  width, height),3)
                    else:
                        pygame.draw.rect(screen, WHITE, (x - width//2, y-height//2,  width, height),3)
                else:
                    x, y = pygame.mouse.get_pos()
                    point2 = np.array([x, y])
                    height = 10
                    width = 10
                    if event.button == 1:
                        pygame.draw.rect(screen, DEEP_PINK, (x - width//2, y-height//2,  width, height),3)
                    elif event.button == 2:
                        pygame.draw.rect(screen, BLUE, (x - width//2, y-height//2,  width, height),3)
                    else:
                        pygame.draw.rect(screen, WHITE, (x - width//2, y-height//2,  width, height),3)
                if i > 0:
                    pygame.draw.aaline(screen, GREEN, point1, point2)
                i += 1
    x, y = pygame.mouse.get_pos()
    pt = [x, y]
    pygame.draw.circle(screen, RED, pt, 0)
    
    pygame.display.update()
pygame.quit()