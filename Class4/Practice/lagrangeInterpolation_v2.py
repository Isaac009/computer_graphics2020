"""
Modified on Feb 20 2020
@author: lbg@dongseo.ac.kr
"""

import pygame
from sys import exit
import numpy as np
import math
    
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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (178, 151, 0)

pts = [] 
knots = []
count = 0
# screen.blit(background, (0,0))
screen.fill(WHITE)

# https:#kite.com/python/docs/pygame.Surface.blit
clock= pygame.time.Clock()


def drawPoint(pt, color='GREEN', thick=3):
    pygame.draw.circle(screen, color, pt, thick)


# HW2 implement drawLine with drawPoint
def draw_lagrange(color='GREEN', thick=1):
    pygame.draw.rect(screen, WHITE, (0, 0, width, height))
    # print('pts = ', pts)

    for p in range(len(pts)):
        pygame.draw.rect(screen, GOLD, (pts[p][0] - margin, pts[p][1] - margin, 2 * margin, 2 * margin), 5)

    for t in np.arange(0, len(pts)-1, 0.01):
        f_x = np.zeros(2, dtype=np.float32)
        for i in np.arange(0, len(pts), 1):
            num, den = 1, 1
            for j in np.arange(0, len(pts), 1):
                if j!=i:
                    num = num * (t - j)
                    den = den * (i - j)
            f_x = f_x + np.dot(pts[i], num/den)
        f_x = f_x.astype(int)
        drawPoint(f_x, color=RED, thick=1)

        f_x_sl = np.dot(-t+math.floor(t), pts[math.floor(t)]) + pts[math.floor(t)] + np.dot(t-math.floor(t), pts[math.ceil(t)])
        f_x_sl = f_x_sl.astype(int)
        drawPoint(f_x_sl, color=BLUE, thick=1)


# def Hermit():
#     moveto (P1);                            # move pen to startpoint
#     for t in np.arange(0, len(pts)-1, 0.01):
#         s = t / steps;    # scale s to go from 0 to 1
#         h1 =  2*math.pow(s,3) - 3*math.pow(s,2) + 1;          # calculate basis function 1
#         h2 = -2*math.pow(s,3) + 3*math.pow(s,2);              # calculate basis function 2
#         h3 =   math.pow(s,3) - 2*math.pow(s,2) + s;         # calculate basis function 3
#         h4 =   math.pow(s,3) -  math.pow(s,2);              # calculate basis function 4
#         p = h1*P1 +  h2*P2 + h3*T1 + h4*T2; # multiply and sum all funtions
#                                         # together to build the interpolated
#                                         # point along the curve.
                    
#         # lineto (p)                            # draw to calculated point on the curve
#         print(p)

def drawPolylines(color='GREEN', thick=1):
    if count < 2:
        return

    draw_lagrange(color, thick)


# Loop until the user clicks the close button.
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

    if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0 :
        pts.append(pt) 
        count += 1
        pygame.draw.rect(screen, GOLD, (pt[0]-margin, pt[1]-margin, 2*margin, 2*margin), 5)
        print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed)+" add pts ...")
    else:
        print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed))

    if len(pts)>1:
        drawPolylines(BLUE, 1)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed

pygame.quit()

