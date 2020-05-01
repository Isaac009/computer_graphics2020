"""
Modified on Feb 20 2020
@author: lbg@dongseo.ac.kr
"""

import pygame
from sys import exit
import numpy as np
import math
    

MAX = 1024
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

T = []
pts = [] 
knots = []
count = 0
knotcount=0
idletv=-1
# screen.blit(background, (0,0))
screen.fill(WHITE)

# https://kite.com/python/docs/pygame.Surface.blit
clock= pygame.time.Clock()

def drawPoint(pt, color='GREEN', thick=3):
    pygame.draw.circle(screen, color, pt, thick)

def quadratic_bezier(t):
    x = np.power(1-t, 2) * pts[0][0] + \
        (1 - t) * 2 * t * pts[1][0] + t**2 * pts[2][0]
    y = np.power(1-t, 2) * pts[0][1] + \
        (1 - t) * 2 * t * pts[1][1] + t**2 *pts[2][1]
    # print('[',x,',',y,']')

    # xy = np.array([0,0], np.float32)
    # xs = [np.power(1-t, 2), (1 - t) * 2 * t, t**2]
    # ys = [np.power(1-t, 2), (1 - t) * 2 * t, t**2]
    # xy = np.dot(np.array([xs,ys]),np.array(pts))
    # print(xy)
    return [x,y]
    
def cubic_bezier(t):
    x = np.power(1-t, 3) * pts[0][0] + \
        np.power(1-t, 2) * 3 * t* pts[1][0] + \
        (1 - t) * 3 * t**2 * pts[2][0] + t**3 * pts[3][0]
    y = np.power(1-t, 3) * pts[0][1] + \
        np.power(1-t, 2) * 3 * t* pts[1][1] + \
        (1 - t) * 3 * t**2 * pts[2][1] + t**3 * pts[3][1]
    return [x,y]

def multi_curves(t):
    # moveTo(pts[0])

    for i in range(len(pts)-2):
        p0 = pts[i]
        p1 = pts[i+1]
        midx = (p0[0] + p1[0]) / 2
        midy = (p0[1] + p1[1]) / 2
        quadratic_bezier(t)
    p0 = pts[len(pts)-2]
    p1 = pts[len(pts)-1]
    quadratic_bezier(t)

def makeknots():
    XMARGIN, YMARGIN = 25, 25
    x0=XMARGIN
    x1=width-XMARGIN
    x=height-YMARGIN
    y=height-YMARGIN
    if(display_mode == BEZIER):
		knotcount=(count-1)*2
		for i in range(knotcount//2):
			T[i]=0 
			T[knotcount-i-1]=1
		for i in range(knotcount):
			TP[i][0]=(T[knotcount-1]-T[i])/(T[knotcount-1]-T[0])*x0
				+(T[i]-T[0])/(T[knotcount-1]-T[0])*x1
			TP[i][1]=y


def myBSpline():
	v = []

	# if count<=0 or count > 200:
    #     return
	# glColor3f(r, 0., 0.)
	# glBegin(GL_LINE_STRIP)
	for i in range(MAX):
		x=i/MAX*(T[knotcount-poly_deg-1]-T[poly_deg])+T[poly_deg]
		myBSplineCalculate(v, T, x, count)
		v[1]=height-v[1]
		glVertex3dv(v)

	# glEnd()

	tv=idletv*(T[knotcount-poly_deg-1]-T[poly_deg])+T[poly_deg]
	myBSplineCalculateDisplay(v, T, tv, count)


def combi(n, m):
    total = 1.0

	if(m==0 or m==n): return 1.
	else if(m<0 or m>n): return 1.
	for i in range(n, m):
		total *= i
	for i in range(n-m, 0, -1):
		total /= i
	return total


def myBezier():
	v = []

	# if count<=0 or count > 200:
    #     return
	# glColor3f(r, 0., 0.) color
	# glBegin(GL_LINE_STRIP) Line
	for i in range(MAX):
		x = i/MAX
		myBezierCalculate(v, T, x, count)
		v[1]=height-v[1]
		# glVertex3dv(v)

	tv=idletv
	# myBezierCalculateDisplay(v, T, tv, count)

def myBezierCalculate(v, t, x, size):
	v = [0.0, 0.0]
	for i in range(size):
		l=combi(size-1,i)*math.pow(x, i)*math.pow(1.-x, size-1-i)
		v[0]+=pts[i][0]*l
		v[1]+=pts[i][1]*l

def draw_lagrange(color='GREEN', thick=1):
    pygame.draw.rect(screen, WHITE, (0, 0, width, height))
    # print('pts = ', pts)

    for p in range(len(pts)):
        pygame.draw.rect(screen, GOLD, (pts[p][0] - margin, pts[p][1] - margin, 2 * margin, 2 * margin), 5)

    for t in np.arange(0, 1, 0.005):
        # f_x = np.zeros(2, dtype=np.float32)
        # print(quadratic(t))
        # f_x = np.array(quadratic(t),  dtype='f')
        f_x = np.array(multi_curves(t),  dtype='f')
        # for i in np.arange(0, len(pts), 1):
        #     num, den = 1, 1
        #     for j in np.arange(0, len(pts), 1):
        #         if j!=i:
        #             num = num * (t - j)
        #             den = den * (i - j)
        #     f_x = f_x + np.dot(pts[i], num/den)
        # f_x = f_x.astype(int)
        drawPoint(f_x, color=RED, thick=1)
    for t in np.arange(0, len(pts)-1, 0.01):
        f_x_sl = np.dot(-t+math.floor(t), pts[math.floor(t)]) + pts[math.floor(t)] + np.dot(t-math.floor(t), pts[math.ceil(t)])
        f_x_sl = f_x_sl.astype(int)
        drawPoint(f_x_sl, color=BLUE, thick=1)


def drawPolylines(color='GREEN', thick=1):
    if count < 2:
        return
    if len(pts) == 4:
        draw_lagrange(color, thick)


# Loop until the user clicks the close button.
done = False
pressed = 0
margin = 6
old_pressed = 0
old_button1 = 0

while not done:   
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all ptsU we can.
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
        # print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed)+" add pts ...")
    else:
        pass
        # print("len:"+repr(len(pts))+" mouse x:"+repr(x)+" y:"+repr(y)+" button:"+repr(button1)+" pressed:"+repr(pressed))

    if len(pts)>1:
        drawPolylines(BLUE, 1)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed

pygame.quit()

