"""
Modified on Feb 20 2020
@author: lbg@dongseo.ac.kr
"""

import pygame
from sys import exit
import numpy as np
import math
from scipy.sparse import diags
from menu import Controller
    
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
bright_red = (255,0,0)
bright_green = (0,255,0)


# screen.blit(background, (0,0))
screen.fill(WHITE)

# https:#kite.com/python/docs/pygame.Surface.blit
clock= pygame.time.Clock()

def drawPoint(pt, color='GREEN', thick=3):
    pygame.draw.circle(screen, color, pt, thick)


# HW2 implement drawLine with drawPoint
def draw_lagrange(color='GREEN', thick=1):
    
    pygame.draw.rect(screen, WHITE, (0, 0, width, height))

    for p in range(len(pts)):
        pygame.draw.rect(screen, GREEN, (pts[p][0] - margin, pts[p][1] - margin, 2 * margin, 2 * margin), 5)

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
        drawPoint(f_x, color=GREEN, thick=1)

        f_x_sl = np.dot(-t+math.floor(t), pts[math.floor(t)]) + pts[math.floor(t)] + np.dot(t-math.floor(t), pts[math.ceil(t)])
        f_x_sl = f_x_sl.astype(int)
        drawPoint(f_x_sl, color=RED, thick=1)


def Hermite(color='GREEN', thick=1):
    pygame.draw.rect(screen, WHITE, (0, 0, width, height))

    for p in range(len(pts)):
        pygame.draw.rect(screen, BLACK, (pts[p][0] - margin, pts[p][1] - margin, 2 * margin, 2 * margin), 6)
    const=0.5
    n = len(pts)
    ptz = np.array(pts, np.float32)
    for t in np.arange(0, 1, 0.005):
        h1 = (2 * (t ** 3)) - (3 * (t ** 2)) + 1
        h2 = (-2 * (t ** 3)) + (3 * (t ** 2))
        h3 = (t ** 3) - (2 * (t ** 2)) + t
        h4 = (t ** 3) - (t ** 2)
        for i in np.arange(0, n-1, 1):
            if n>2:
                if i == 0:
                    tangent2 = ptz[i + 2] - ptz[i]
                    tangent1 = np.zeros(2, np.float32)
                    tan_dp2 = np.dot(const, tangent2)
                elif i > 0 and i < n-2:
                    tan_pt1 = ptz[i + 1] - ptz[i - 1]
                    tangent2 = ptz[i + 2] - ptz[i]
                    tangent1 = np.dot(const,tan_pt1)
                    tan_dp2 = np.dot(const,tangent2)
                else:
                    tan_pt1 = ptz[i + 1] - ptz[i - 1]
                    tangent1 = np.dot(const, tan_pt1)
                    tan_dp2 = np.zeros(2, np.float32)
            else:
                tangent1 = np.zeros(2, np.float32)
                tan_dp2 = np.zeros(2, np.float32)

            c_h = np.dot(h1,pts[i]) + np.dot(h2,pts[i+1]) + np.dot(h3,tangent1) + np.dot(h4,tan_dp2)
            c_h = c_h.astype(int)
            drawPoint(c_h, color=GREEN, thick=1)

            # f_x_sl = np.dot(-t+math.floor(t), pts[math.floor(t)]) + pts[math.floor(t)] + np.dot(t-math.floor(t), pts[math.ceil(t)])
            # f_x_sl = f_x_sl.astype(int)
            # drawPoint(f_x_sl, color=BLUE, thick=1)

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

def Bezier(color='GREEN', thick=1):
    pygame.draw.rect(screen, WHITE, (0, 0, width, height))

    for p in range(len(pts)):
        pygame.draw.rect(screen, BLACK, (pts[p][0] - margin, pts[p][1] - margin, 2 * margin, 2 * margin), 5)

    pygame.draw.rect(screen, BLACK, (950 - margin, height - 55 - margin, 2 * margin, 2 * margin), 3)

    n = len(pts)
    for t in np.arange(0, 1, 0.005):
        b_z  = np.zeros(2, dtype=np.float32)
        for i in range(n):
            if n > 2:
                b_z = b_z + np.dot(nCr(n-1, i)*((1-t)**(n-1-i))*(t**i),pts[i])
            if i < n-1:
                b_z_sl = np.dot((1-t),pts[i]) + np.dot(t,pts[i+1])
                b_z_sl = b_z_sl.astype(int)
                drawPoint(b_z_sl, color=BLUE, thick=1)

        b_z = b_z.astype(int)
        drawPoint(b_z, color=RED, thick=1)


def cubic_spline(color='GREEN', thick=1):
    pygame.draw.rect(screen, WHITE, (0, 0, width, height))
    if pts is None:
        return
    for p in range(len(pts)):
        pygame.draw.rect(screen, BLACK, (pts[p][0] - margin, pts[p][1] - margin, 2 * margin, 2 * margin), 5)
    n = len(pts)

    ptz = np.array(pts,np.float32)
    if n > 2:
        k = np.array([np.ones(n-1),4*np.ones(n),np.ones(n-1)])
        offset = [-1,0,1]
        A = diags(k,offset).toarray()
        A[0][0], A[n-1][n-1] = 2, 2

        r = np.zeros((n,2),np.float32)
        for c in range(n):
            if c == 0: r[c] = ptz[1] - ptz[0]
            elif c > 0 and c < n - 1: r[c] = ptz[c+1] - ptz[c-1]
            else: r[c] = ptz[c] - ptz[c-1]

        D = np.dot(np.linalg.inv(A),3*r)

        for t in np.arange(0, 1, 0.002):
            for i in range(n-1):
                a, b = ptz[i], D[i]
                c=np.dot(3, (ptz[i+1] - ptz[i]))-np.dot(2, D[i]) - D[i+1]
                d = np.dot(2,(ptz[i]-ptz[i+1]))+D[i]+D[i+1]
                Y_t = a + b*t + c*t*t + d*t*t*t
                drawPoint(Y_t.astype(int), color=RED, thick=1)
                # outline_points = np.dot(-t+math.floor(t), pts[math.floor(t)]) + pts[math.floor(t)] + np.dot(t-math.floor(t), pts[math.ceil(t)])
                # outline_points = outline_points.astype(int)
                # drawPoint(outline_points, color=BLUE, thick=1)

def run_mode(color='GREEN', thick=1):
    if count < 3:
        return
    screen.fill(WHITE)
    if mode == 2:
        Bezier(color, thick)
    elif mode == 3:
        Hermite(color, thick)
    elif mode == 4:
        cubic_spline(color,thick)
    else:
        draw_lagrange(color, thick)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def main_window(mode_v=0):
    global pts
    global count
    global margin
    global mode

    pts = [] 
    count = 0
    del_pt = []
    knots = []
    
    mode = mode_v

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
                    for index, p in enumerate(pts):
                        if abs(p[0] - x) <= margin and abs(p[1] - y) <= margin:
                            del_pt = pts[index]
                            pts.remove(pts[index])
                            print("Deleted Point: ",del_pt)

                if event.button == 2:
                    done = True
                    screen.fill(WHITE)
                    pts.clear()
                    count = 0
                    print("Reset Control Points List...")
                    pygame.display.update()
                    cntr = Controller()
                    cntr.show_main()
                    print("***** Select Any Operation!!! ******")
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = 1            
            elif event.type == pygame.QUIT:
                done = True
                print("***** Select Any Operation!!! ******")
            else:
                pressed = 0

        button1, button2, button3 = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        pt = [x, y]

        
        if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0 :
            print("Mode: ", mode)
            if len(pts) == 0:
                pts.append(pt)
            else:
                added = False
                for index, p in enumerate(pts):
                    if abs(p[0] - pt[0]) <= margin and abs(p[1] - pt[1]) <= margin:
                        pts.remove(pts[index])
                        pts.insert(index, pt)
                        added = True
                if not added:
                    pts.append(pt)
            count += 1
            print(pts)
            pygame.draw.rect(screen, BLACK, (pt[0]-margin, pt[1]-margin, 2*margin, 2*margin), 5)
        elif old_pressed == 0 and pressed == 0 and old_button1 == 1 and button1 == 1:
                print("Mode: ", mode)
                margino = 50
                for index, p in enumerate(pts):
                    if abs(p[0] - pt[0]) <= margino and abs(p[1] - pt[1]) <= margino:
                        pts.remove(pts[index])
                        pts.insert(index, pt)
                        print(pts)
                print(pts) 
                count += 1
        
        if len(pts)>1:
            run_mode(BLUE, 1)

        pygame.display.update()
        old_button1 = button1
        old_pressed = pressed
        if mode == 5: # Quit
            break