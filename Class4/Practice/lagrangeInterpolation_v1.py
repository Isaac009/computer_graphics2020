"""
Modified on April 14 2020
@author: Isack Nicholaus

Implement Lagrange Interpolation and Bezier Curves + alpha(GUI) with HW 4.
add control points
move control points
delete control points
change time
capture video and upload cloud
"""

import pygame
from sys import exit
import numpy as np
import math, random, sys
    
width = 1200
height = 1000
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
screen.fill(BLACK)

# https://kite.com/python/docs/pygame.Surface.blit
clock= pygame.time.Clock()


def drawPoint(pt, color='GREEN', thick=2):
    pygame.draw.circle(screen, color, pt, thick)

#HW2 implement drawLine with drawPoint
def drawLine(pt0, pt1, color='GREEN', thick=2):
    pt0 = np.array(pt0, dtype='f')
    pt1 = np.array(pt1, dtype='f')
    t_s = np.arange(0.,1.0, 0.005)
    for t in t_s:
        pt_t = (1-t)*pt0 + t*pt1
        drawPoint(pt_t, color)

def lagrang(color='RED'):
    pygame.draw.rect(screen, BLACK, (0, 0, width, height))
    for i in range(count-1):
        drawLine(pts[i], pts[i+1], color)
    for t in range(len(pts)):
        pygame.draw.rect(screen, RED, (pts[t][0] - margin, pts[t][1] - margin, 2 * margin, 2 * margin), 5)
    
    n_pxy = np.array(pts, dtype='f')
    xs = n_pxy[:,0]
    ys = n_pxy[:,1]
    xplt = np.arange(xs[0], xs[-1], 0.5)
    yplt = np.array([], dtype='f')
    
    for xp in xplt:
        yp = 0
        for xi, yi in zip(xs,ys):
            yp += yi * np.prod((xp - xs[xs != xi])/(xi - xs[xs != xi]))
        yplt = np.append(yplt, yp)
    for xp, yp in zip(xplt, yplt):
        pt = np.array([xp,yp], dtype='f')
        drawPoint(pt, color=RED, thick=2)

def drawPolylines(color='GREEN', thick=2):
    # screen.fill(WHITE)
    if(count < 2): return
    # c_mouse_pos = pygame.mouse.get_pos()
    lagrang(color)
   
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
    # pygame.draw.circle(screen, RED, pt, 0)

    if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0 :
        pts.append(pt) 
        count += 1
        pygame.draw.rect(screen, RED, (pt[0]-margin, pt[1]-margin, 2*margin, 2*margin), 5)
        # print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed)+" add pts ...")
    # else:
        # print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed))

    if len(pts)>1:
        lagrang(GREEN)
        # drawPolylines(GREEN, 1)
        # drawLagrangePolylines(BLUE, 10, 3)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed

pygame.quit()

