"""
Modified on Feb 20 2020
@author: lbg@dongseo.ac.kr
"""

import pygame
from sys import exit
import numpy as np
    
width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)

# background_image_filename = 'image/curve_pattern.png'

# background = pygame.image.load(background_image_filename).convert()
# width, height = background.get_size()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("ImagePolylineMouseButton")

font= pygame.font.SysFont("consolas",17) 
  
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

# print text function
def printText(msg, color='BLUE', pos=(10,10)):
    textSurface = font.render(msg, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos
    screen.blit(textSurface, textRect)

def drawPoint(pt, color='GREEN', thick=3):
    # pygame.draw.line(screen, color, pt, pt, thick)
    pygame.draw.circle(screen, color, pt, thick)

#HW2 implement drawLine with drawPoint
def drawLine(pt0, pt1, color='GREEN', thick=3):
    pt0 = np.array(pt0, dtype=np.float32)
    pt1 = np.array(pt1, dtype=np.float32)

    drawPoint(pt0, color=RED, thick=3)
    drawPoint(pt1, color=RED, thick=3)
    for t in np.arange(-0.5,1.5,0.005):
        l_t = (1-t)*pt0 + t*pt1
        drawPoint(l_t, color=RED, thick=1)

def lagrang(pxy):
    x = np.array(pxy[:,0], float)
    y = np.array(pxy[:,1], float)
    print(x, y)

    # xplt = np.linspace(x[0],x[-1])
    # yplt = np.array([], float)

    # for xp in xplt:
    #     yp = 0
    #     for xi, yi in zip(x,y):
    #         yp += yi * np.prod((xp - x[x != xi])/(xi - x[x != xi]))
    #     yplt = np.append(yplt, yp)
    # for xp, yp in zip(xplt, yplt):
    #     print(xp, yp)
    # drawLine()

def t_calc(current_pos):
    xy0, xy1, xy2 = pts[0], pts[1], pts[2]
    t01 = np.zeros((2, 2))
    t01[0] = np.subtract(xy0, xy2)
    t01[1] = np.subtract(xy1, xy2)
    xy_xy2 = np.subtract(current_pos, xy2)
    t01 = t01.transpose()
    xy_xy2 = xy_xy2.transpose()
    t01 = np.dot(np.linalg.inv(t01), xy_xy2)
    t012 = np.append(t01, 1-(t01[0]+t01[1]))
    return t012

def drawPolylines(color='GREEN', thick=3):
    if(count < 3): return

    for i in range(count-1):
        if i == 0:
            drawLine(pts[i], pts[i+2], color)
            # printText('pt' + str(i) + ' ' + str(tuple(pts[i])),'RED', (10,10))
        
        drawLine(pts[i], pts[i+1], color)
        pos_y = 10 + ((i+1)*20)
        # printText('pt' + str(i+1) + ' ' + str(tuple(pts[i+1])),'RED', (10,pos_y))

    current_pos = pygame.mouse.get_pos()
    t012 = t_calc(current_pos)
    t012 = np.round(t012,2)
    pygame.draw.rect(screen, WHITE, (10, 10, 190, 30))
    printText('pt  ' + str(current_pos) + ' ==> ' + str(tuple(t012)),'RED', (10, 17))
    

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

    if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0 and count < 3:
        pts.append(pt) 
        count += 1
        pygame.draw.rect(screen, WHITE, (pt[0]-margin, pt[1]-margin, 2*margin, 2*margin), 5)
        print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed)+" add pts ...")
    else:
        print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed))

    if len(pts)==3:
        drawPolylines(GREEN, 1)
    elif len(pts)>3:
        del pts[0]
        count = count - 1
        pygame.draw.rect(screen, WHITE, (10, 10, 200, 160))
        # drawLagrangePolylines(BLUE, 10, 3)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed

pygame.quit()

