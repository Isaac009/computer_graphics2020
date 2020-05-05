"""
Modified on Feb 20 2020
@author: lbg@dongseo.ac.kr
"""

import pygame
from sys import exit
import numpy as np
import math
from scipy.sparse import diags
    
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
del_pt = []
knots = []
count = 0
# screen.blit(background, (0,0))
screen.fill(WHITE)

# https:#kite.com/python/docs/pygame.Surface.blit
clock= pygame.time.Clock()

def get_pts(ptz=None):
    return ptz

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


def Hermit(color='GREEN', thick=1):
    # moveto (P1)                            # move pen to startpoint
    pygame.draw.rect(screen, WHITE, (0, 0, width, height))

    for p in range(len(pts)):
        pygame.draw.rect(screen, GOLD, (pts[p][0] - margin, pts[p][1] - margin, 2 * margin, 2 * margin), 5)
    
    T = []
    for k in range(len(pts)): 
        if k > 0 and k < len(pts)-2:
            print(pts[k+1],pts[k-1])
            T.append(0.2 * (np.array(pts[k+1]) - np.array(pts[k-1])))
        else:
            T.append([0,0])
            
    for i in range(len(pts)-1):   
        for t in np.arange(0, len(pts)-1, 0.01):
            h1 =  2*math.pow(t,3) - 3*math.pow(t,2) + 1          # calculate batit function 1
            h2 = -2*math.pow(t,3) + 3*math.pow(t,2)              # calculate batit function 2
            h3 =   math.pow(t,3) - 2*math.pow(t,2) + t         # calculate batit function 3
            h4 =   math.pow(t,3) -  math.pow(t,2)              # calculate batis function 4
            
            p = np.array(pts[i]) * h1 +  np.array(pts[i+1]) * h2 + np.array(T[i]) * h3 + np.array(T[i+1])*h4
            drawPoint(p.astype(int), color=RED, thick=1)

            f_x_sl = np.dot(-t+math.floor(t), pts[math.floor(t)]) + pts[math.floor(t)] + np.dot(t-math.floor(t), pts[math.ceil(t)])
            f_x_sl = f_x_sl.astype(int)
            drawPoint(f_x_sl, color=BLUE, thick=1)


def Bezier(color='GREEN', thick=1):
    pygame.draw.rect(screen, WHITE, (0, 0, width, height))

    for p in range(len(pts)):
        pygame.draw.rect(screen, GOLD, (pts[p][0] - margin, pts[p][1] - margin, 2 * margin, 2 * margin), 5)

    P = np.array(pts,np.float32)
    n = len(pts)-1
    
    bt = np.zeros(2,np.float32)
    for t in np.arange(0, 1, 0.01):
        for i in range(n):
            if i == 0:
                # bt_i = math.pow((1-t),n)
                bt = P[i]
            else:
                bt_i = math.factorial(n)/(math.factorial(i)*math.factorial(n - i))
                bt_i *= math.pow(t,i)*math.pow((1-t),n-i)
                bt += bt_i * P[i]
            
        print("bt(i)", bt)
        drawPoint(bt.astype(int), color=RED, thick=1)

        f_x_sl = np.dot(-t+math.floor(t), pts[math.floor(t)]) + pts[math.floor(t)] + np.dot(t-math.floor(t), pts[math.ceil(t)])
        f_x_sl = f_x_sl.astype(int)
        drawPoint(f_x_sl, color=BLUE, thick=1)

def cubic_spline(color='GREEN', thick=1, pts=None):
    pygame.draw.rect(screen, WHITE, (0, 0, width, height))
    for p in range(len(pts)):
        pygame.draw.rect(screen, GOLD, (pts[p][0] - margin, pts[p][1] - margin, 2 * margin, 2 * margin), 5)
    n = len(pts)
    k = np.array([np.ones(n-1),4*np.ones(n),np.ones(n-1)])
    offset = [-1,0,1]
    A = diags(k,offset).toarray()
    A[0][0] = 2
    A[n-1][n-1] = 2
    pts = np.array(pts,np.float32)
    if n > 2:
        r = np.zeros((n,2),np.float32)
        for c in range(n-1):
            if c < n - 1:
                if c == 0:
                    r[c] = pts[1] - pts[0]
                r[c] = 3*(pts[c+1] - pts[c])
        D = np.dot(np.linalg.inv(A), r)
        # print("r shape: ",r.shape,' D shape: ',D.shape)
        # print('r: ',r)
        # print('D: ',D)
        pts = np.array(pts,np.float32)
        for i in range(n - 2):
            if i < n:
                # a[i], b[i], c[i] = pts[i], D[i], 3*(pts[i+1]-pts[i]) - 2*D[i]-D[i+1]
                a = pts[i]
                b = D[i]
                c1 = np.dot(3,np.subtract(pts[i+1],pts[i]))
                c2 = np.dot(2,D[i]-D[i+1])
                c = np.subtract(c1,c2)
                d = np.dot(2,(pts[i]-pts[i+1])+D[i]+D[i+1])

            for t in np.arange(0, 1, 0.01):
                Y_t = a + b*t + c*t*t + d*t*t*t
                drawPoint(Y_t.astype(int), color=RED, thick=1)

                f_x_sl = np.dot(-t+math.floor(t), pts[math.floor(t)]) + pts[math.floor(t)] + np.dot(t-math.floor(t), pts[math.ceil(t)])
                f_x_sl = f_x_sl.astype(int)
                drawPoint(f_x_sl, color=BLUE, thick=1)

def mode(color='GREEN', thick=1):
    if count < 3:
        return
    screen.fill(WHITE)
    # draw_lagrange(color, thick)
    # Hermit(color, thick)
    Bezier(color, thick)
    # cubic_spline(color,thick, pts)

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
            if event.button == 3: # Mouse Right Click
                height = 16
                width = 16
                x, y = pygame.mouse.get_pos() #Gets the mouse position
                print(pts,' == ',del_pt)
                for index, p in enumerate(pts):
                    if abs(p[0] - x) <= margin and abs(p[1] - y) <= margin:
                        pts.remove(pts[index])
                # pygame.draw.rect(screen, BLACK, (x - width//2, y-height//2,  width, height)) #Draws a black rectangle at the mouse position!      
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 1            
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = 0

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    pt = [x, y]

    # if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0 :
    if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0 :
        if len(pts) == 0:
            pts.append(pt)
        else:
            added = False
            for index, p in enumerate(pts):
                if abs(p[0] - pt[0]) <= margin and abs(p[1] - pt[1]) <= margin:
                    pts.remove(pts[index])
                    pts.insert(index, pt)
                    added = True
                    print("Within")
            if not added:
                pts.append(pt) 
                print("Added")
        count += 1
        print(pts)
        pygame.draw.rect(screen, GOLD, (pt[0]-margin, pt[1]-margin, 2*margin, 2*margin), 5)
    elif old_pressed == 0 and pressed == 0 and old_button1 == 1 and button1 == 1:
        margino = 50
        for index, p in enumerate(pts):
            if abs(p[0] - pt[0]) <= margino and abs(p[1] - pt[1]) <= margino:
                pts.remove(pts[index])
                pts.insert(index, pt)
                print(pts)
        print(pts) 
        count += 1
    #     print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed)+" add pts ...")
    # else:
    #     print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed))

    if len(pts)>1:
        mode(BLUE, 1)
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed

pygame.quit()

