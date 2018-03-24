import pygame, sys, time, random
from pygame.locals import *

def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

#set up pygame
pygame.init()

#set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation + Chaser')

#set up directionvariables
DOWNLEFT =  'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

#set up the colors
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)

#set up the black data structure
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':CYAN, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 40, 20), 'color':MAGENTA, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
b4= {'rect':pygame.Rect(50, 250, 170, 30), 'color':WHITE, 'dir':UPRIGHT}

blocks = [b1, b2, b3, b4]


#new food and food counters
foodCounter = 0
NEWFOOD = 30
FOODSIZE = 20
bouncer = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':UPLEFT}
foodImage = pygame.image.load('gamefood.jpg')
foods = []
for i in range(10):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH-FOODSIZE), random.randint(0, WINDOWHEIGHT-FOODSIZE),
    FOODSIZE, FOODSIZE))


#set up the music
pickUpSound = pygame.mixer.Sound('hyena-laugh_daniel-simion.wav')
pygame.mixer.music.load('hyena-laugh_daniel-simion.wav')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True 

#run the game loop
while True:
    #check for QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #draw the background onto the surface
    windowSurface.fill(BLACK)

    for b in blocks:
        #move the block data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        #check to see if the block has moved out of the window
        #if the value of the y coordinate at the top most side is less than zero, it is no longer in the window.
        if b['rect'].top < 0:
            #block has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            #block has moved past the bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
                #block has moved past the left side
                if b['dir'] == DOWNLEFT:
                    b['dir'] = DOWNRIGHT
                if b['dir'] == UPLEFT:
                    b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
                #block has moved past the right side
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = DOWNLEFT
                if b['dir'] == UPRIGHT:
                    b['dir'] = UPLEFT

        #draw the block onto the surface
        pygame.draw.rect(windowSurface, b['color'], b['rect'])


    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    for food in foods[:]:
        if doRectsOverlap(b['rect'], food):
            foods.remove(food)
            
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREY, foods[i])

    
    #draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)
