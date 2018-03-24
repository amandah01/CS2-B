import pygame, sys, random
from pygame.locals import *

#set up pygame
pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Images and Sounds')

#set up color
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

#here is where we set up the player and food structure
foodCounter = 0
FOODSIZE = 25
NEWFOOD = 40
player = pygame.Rect(250, 200, 50, 50)
playerImage = pygame.image.load('gamecharacter.jpg')
playerStrechedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('gamefood.jpg')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH-FOODSIZE), random.randint(0, WINDOWHEIGHT-FOODSIZE),
    FOODSIZE, FOODSIZE)) #here we are expecting an error

#set up the movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 10

#set up the music
pickUpSound = pygame.mixer.Sound('hyena-laugh_daniel-simion.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True 

#run the game loop
while True:
    #checking for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            #change the movement variables
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveDown = True
                moveUp = False

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft =False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
                if event.key == K_x:
                    player.top = random.randint(0, WINDOWHEIGHT)
                    player.left = random.randint(0, WINDOWWIDTH)
                if event.key == K_m:
                    if musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    musicPlaying = not musicPlaying

            if event.type == MOUSEBUTTONUP:
                foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT),
                FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        #add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT),
        FOODSIZE, FOODSIZE))

    #draw the white background
    windowSurface.fill(WHITE)

    #move the player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.right -= MOVESPEED
    if moveRight and player.right < WINDOWHEIGHT:
        player.right += MOVESPEED

    #draw the player onto the surface
    #pygame.draw.rect(windowSurface, BLACK, player)
    windowSurface.blit(playerStretchedImage, player)

    #checking whether our player is eating or touching any other food sources
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            #add effects to the player in here
            player = pygame.Rect(player.left, player.top, player.width+2, player.height+2)
            playerStretchedImage = pyame.transform.scale(playerImage, (player.width,
            player.height)
                
                                                                            

    # draw the food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])
            #rectangular object is 'food'
            #our image is 'foodImage'
            #

    #draw the window onto the sreen
    pygame.display.update()
    mainClock.tick(40)
            
            
            
            
                    
                             

    
                 
