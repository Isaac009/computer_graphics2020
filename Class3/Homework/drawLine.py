"""
Modified on March 30 2020
@author: Isack Nicholaus
"""

import pygame
from sys import exit
import numpy as np
import math, random, sys
    
width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)

# background_image_filename = 'image/curve_pattern.png'

# background = pygame.image.load(background_image_filename).convert()
# width, height = background.get_size()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("ImagePolylineMouseButton")
  
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pts = [] 
knots = []
count = 0
#screen.blit(background, (0,0))
screen.fill(WHITE)

# https://kite.com/python/docs/pygame.Surface.blit
clock= pygame.time.Clock()

# drawPoint(pt0, color=BLUE, thick=3)
#     drawPoint(pt1, color=BLUE, thick=3)
#     for t in np.arange(-0.5,1.5,0.005):
#         l_t = (1-t)*pt0 + t*pt1
#         drawPoint(l_t, color=BLUE, thick=1)
font= pygame.font.SysFont("consolas",17) 

def Computed_Coordinate(msg, color='BLACK', pos=(10,10)):
    
    textSurface = font.render(msg, True, BLACK, None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    screen.blit(textSurface, textRect)

def drawPoint(pt, color='GREEN', thick=3):
    # pygame.draw.line(screen, color, pt, pt, thick)
    pygame.draw.circle(screen, color, pt, thick)

#HW2 implement drawLine with drawPoint
def drawLine(color='GREEN', thick=2, pt0=None, pt1=None, pt2=None, pt=None):
    pt0 = np.array(pt0, dtype='f')
    pt1 = np.array(pt1, dtype='f')
    pt2 = np.array(pt2, dtype='f')
    # drawPoint(pt0, color=BLUE, thick=3)
    # drawPoint(pt1, color=BLUE, thick=3)
    # for t in np.arange(-0.5,1.5,0.005):
    #     l_t = (1-t)*pt0 + t*pt1
    #     drawPoint(l_t, color=BLUE, thick=1
    
    d1 = np.array([pt0-pt2, pt1-pt2])
    d1 = np.transpose(d1)
    d2 = np.array([pt-pt2])
    d2 = np.transpose(d2)
    t_0_t_1 = np.linalg.inv(np.array([pt0-pt2, pt1-pt2]))
    t_0_t_1 = np.matmul(t_0_t_1,d2)
    t_0 = t_0_t_1[0]
    t_1 = t_0_t_1[1]
    t_2 = 1 - t_0 - t_1
    text = str(t_0[0]) + ', ',str(t_1[0])+ ', '+str(t_2[0])
    print(text)

def drawPolylines(color='GREEN', thick=8, pt=None):
    i = 0
    # screen.fill(WHITE)
    pygame.draw.line(screen, color, pts[i], pts[i+1], thick)
    pygame.draw.line(screen, color, pts[i], pts[i+2], thick)
    pygame.draw.line(screen, color, pts[i+1], pts[i+2], thick)
    if pt is not None:
        drawLine(color, 2, pts[i], pts[i+1], pts[i+2], pt)

#Loop until the user clicks the close button.
done = False
pressed = 0
margin = 6
old_pressed = 0
old_button1 = 0

while not done:   
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = -1            
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 1            
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = 0

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    pt = [x, y]
    pygame.draw.circle(screen, RED, pt, 0)
    # if count > 2:
    #     drawPoint(pt, pts)

    if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0 and count < 3:
        pts.append(pt)
        count += 1
        pygame.draw.rect(screen, BLUE, (pt[0]-margin, pt[1]-margin, 2*margin, 2*margin), 5)
        # print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed)+" add pts ...")
    # else:
        # print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed))

    if len(pts)>2 and pt is not None:
        drawPolylines(GREEN, 4, pt)
        # drawLagrangePolylines(BLUE, 10, 3)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed

pygame.quit()

