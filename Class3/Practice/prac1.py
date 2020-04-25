

global done

done = False
# exit the program
def events():
    pressed = 0
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = -1            
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 1            
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = 0

# define display surface			
W, H = 800, 800
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Direction and Distance")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

x, y = HW, HH
pmx, pmy = x, y
dx, dy = 0, 0
distance = 0
speed = 20

# main loop
while not done:
    events()

    m = pygame.mouse.get_pressed()
    if m[0] and not distance:
        mx, my = pygame.mouse.get_pos()

        radians = math.atan2(my - pmy, mx - pmx)
        distance = math.hypot(mx - pmx, my - pmy) / speed
        distance = int(distance)

        dx = math.cos(radians) * speed
        dy = math.sin(radians) * speed		
        pmx, pmy = mx, my

    if distance:
        distance -= 1
        x += dx
        y += dy
    print("x:{},y:{}".format(x,y))
    pygame.draw.circle(DS, WHITE, (int(x), int(y)), 4, 0)
    if distance:
        pygame.draw.circle(DS, (255, 0, 0), (pmx, pmy), 5, 0)

    pygame.display.update()
    CLOCK.tick(FPS)
    # DS.fill(BLACK)
pygame.quit()

import numpy as np
print(np.arange(-10.,0.01, 0.04))