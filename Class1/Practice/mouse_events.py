# 1 - left click

# 2 - middle click

# 3 - right click

# 4 - scroll up

# 5 - scroll down

import pygame
from sys import exit
import numpy as np

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)

background_image_filename = '../images/curve_pattern.png'

background = pygame.image.load(background_image_filename).convert()
width, height = background.get_size()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("ImagePolyline")

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

old_pt = np.array([0, 0])
cur_pt = np.array([0, 0])

screen.blit(background, (0, 0))
# https://kite.com/python/docs/pygame.Surface.blit
clock = pygame.time.Clock()


# Loop until the user clicks the close button.
done = False
while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # Mouse left click
                circ = pygame.mouse.get_pos() #Gets the mouse position
                pygame.draw.circle(screen, BLUE, (circ), 10, 0) #Draws a circle at the mouse position!
            elif event.button == 2: # Mouse Middle Click
                print("Event: ", event.button)
                x, y = pygame.mouse.get_pos() #Gets the mouse position 
                # pygame.draw.circle(screen, color, (x,y), radius, thickness)
                pygame.draw.rect(screen, RED, (x - 10//2, y-10//2, 10, 10)) #Draws a red rectangle at the mouse position!
            elif event.button == 3: # Mouse Right Click
                x, y = pygame.mouse.get_pos() #Gets the mouse position
                pygame.draw.rect(screen, BLACK, (x - 16//2, y-16//2, 16, 16)) #Draws a black rectangle at the mouse position!

    x, y = pygame.mouse.get_pos()
    cur_pt = np.array([x, y])
    if old_pt[0] != 0 and old_pt[1] != 0:
        pygame.draw.line(screen, GREEN, old_pt, cur_pt, 5)
    old_pt = cur_pt

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
pygame.quit()