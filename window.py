from cgi import test
import pygame
from sys import exit
from Door import *
from Key import *
from Player import *
import random
import time

# starts pygmae and instantiates all libraries
pygame.mixer.init(48000, -16, 1, 1024)

openSound = pygame.mixer.Sound('Sounds/openDoor.mp3')
invalidSound = pygame.mixer.Sound('Sounds/invalidDoor.mp3')
theme = pygame.mixer.Sound('Sounds/theme.mp3')
scare = pygame.mixer.Sound('Sounds/jumpscare.mp3')
foundFood = pygame.mixer.Sound('Sounds/win.wav')


pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('FeedTheCat')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# conver() helps game run faster
cat_surface = pygame.image.load('graphics/room.PNG').convert_alpha()
# ground_surface = pygame.image.load('graphics/ground.png').convert()
keyUI = pygame.image.load('graphics/UI.png').convert_alpha()

introScene = pygame.image.load('graphics/start/Start.png').convert_alpha()
tutorial = pygame.image.load('graphics/tutorial/Tutorial.png').convert_alpha()

lose = pygame.image.load('graphics/lose/Lose2.png').convert_alpha()
win = pygame.image.load('graphics/win/Win2.png').convert_alpha()

# outside animation
out1 = pygame.image.load(
    'graphics/Doors/Outside1/Outside1.png').convert_alpha()
out2 = pygame.image.load(
    'graphics/Doors/Outside2/Outside2.png').convert_alpha()

# cat animation
cat1 = pygame.image.load('graphics/Final/Cat1.png').convert_alpha()
cat2 = pygame.image.load('graphics/Final/Cat2.png').convert_alpha()
cat3 = pygame.image.load('graphics/Final/Cat3.png').convert_alpha()
cat4 = pygame.image.load('graphics/Final/Cat4.png').convert_alpha()
cat5 = pygame.image.load('graphics/Final/Cat5.png').convert_alpha()

# Variables
screen_pos = -1500
screenRightMax = -3000

rectx = 750
recty = 500

screenLeftMax = 0
screen_change = 0
rect_change = 0
keyflag = False
doorOpen = True
doorlen = 14
x = 1

doorlist = []
keyList = []
mouseKeys = []

touching = False
posClick = any

rflag = False
lflag = False

resetTimer = True

# state
keyState = 0

# loads all door images from graphics
# x variable defines how many doors need to be loaded into the game
# A is closed door
# B is open door


t0 = time.time()


def loadFile():
    global x
    rand = random.randint(1, 14)  # decides which door has cat food
    print(rand)
    while (x <= doorlen):
        catFoodFile = ''
        file = 'graphics/Doors/D/Door' + str(x) + 'A.png'
        fileB = 'graphics/Doors/D/Door' + str(x) + 'B.png'
        if x == rand:
            catFoodFile = 'graphics/Doors/D/Door' + str(x) + 'BFood.png'
        door = Door(x, screen, rectx, recty, file, fileB, catFoodFile)
        doorlist.append(door)

        keyFile = 'graphics/Keys/Key' + str(x) + '.png'
        keyHighlightFile = 'graphics/Keys/Key' + str(x) + 'H.png'
        key = Key(x, screen, keyFile, keyHighlightFile, rectx, recty)
        keyList.append(key)

        mouseFile = 'graphics/MouseKeys/Key' + str(x) + '.png'
        player = Player(x, mouseFile, screen)
        mouseKeys.append(player)
        x += 1


def addSpeed():
    global screen_pos, rectx
    screen_pos += screen_change
    rectx += rect_change
    for i in doorlist:
        i.changeXandY(rectx)


soundState = True
gameState = 1
o = 0
loadFile()
# will never be false and must be broken from the inside
while True:
    t1 = time.time()
    # calculate the difference, i.e. the time elapsed
    seconds = t1 - t0
    if gameState == 0:
        if soundState:
            pygame.mixer.Sound.play(theme)
            soundState = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # this also closes the while loop

            keys = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    keyflag = True
                    rflag = True
                    lflag = False
                    screen_change = -16
                    rect_change = -16
                elif event.key == pygame.K_LEFT:
                    keyflag = True
                    rflag = False
                    lflag = True
                    screen_change = 16
                    rect_change = 16
                if event.key == pygame.K_UP:
                    if (len(mouseKeys) - 1 == keyState):
                        keyState = 0
                    else:
                        keyState += 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    screen_change = 0
                    rect_change = 0
                    keyflag = False
                    rflag = False
                    lflag = False
                elif event.key == pygame.K_LEFT:
                    screen_change = 0
                    rect_change = 0
                    keyflag = False
                    rflag = False
                    lflag = False
                if event.key == pygame.K_DOWN:

                    if (keyState == 0):
                        keyState = len(mouseKeys) - 1
                    else:
                        keyState -= 1

            if event.type == pygame.MOUSEBUTTONUP:
                posClick = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                posClick = pygame.mouse.get_pos()

        if keyflag == True:
            if (screen_pos <= screenLeftMax and screen_pos >= screenRightMax):
                addSpeed()
            elif (screen_pos >= screenLeftMax and rflag == True):
                addSpeed()
            elif (screen_pos <= screenRightMax and lflag == True):
                addSpeed()

        pos = pygame.mouse.get_pos()

        screen.blit(cat_surface, (screen_pos, 0))  # block image transfer

        if seconds > 40:
            pygame.mixer.Sound.stop(theme)
            pygame.mixer.Sound.play(scare)
            gameState = 2

        for i in doorlist:
            # pos_in_mask = pos[0] - i.rect.x, pos[1] - i.rect.y
            # touching = i.rect.collidepoint(*pos) and i.mask.get_at(pos_in_mask)
            # if touching and pos == posClick:
            #
            i.draw()
            # print(keyState)
            if i.isWin == True and i.flag == True:
                pygame.mixer.Sound.stop(theme)
                if (resetTimer):
                    pygame.mixer.Sound.play(foundFood)
                    start_ticks = pygame.time.get_ticks()  # starter tick
                    resetTimer = False
                doneSec = (pygame.time.get_ticks()-start_ticks) / \
                    1000  # calculate how many seconds
                i.drawCatFood()
                print(doneSec)
                if doneSec > 2:
                    gameState = 3

            offsetX = i.rect.x - mouseKeys[keyState].keyRect.left
            offsetY = i.rect.y - mouseKeys[keyState].keyRect.top
            if mouseKeys[keyState].mask.overlap(i.mask, (offsetX, offsetY)) and pos == posClick:
                if mouseKeys[keyState].x == i.x:
                    if i.foodFlag:
                        i.isCatFood()
                    pygame.mixer.Sound.play(openSound)
                    i.setFlag(True)
                    mouseKeys.pop(keyState)
                    leng = len(mouseKeys)
                    keyList.pop(keyState)
                    if (leng == keyState):
                        keyState -= 1
                else:
                    pygame.mixer.Sound.play(invalidSound)

        screen.blit(out1, (screen_pos, 0))

        # cat animation
        if seconds < 10:
            screen.blit(cat1, (screen_pos, 0))
        elif seconds < 15 and seconds > 10:
            screen.blit(cat2, (screen_pos, 0))
        elif seconds < 25 and seconds > 15:
            screen.blit(cat3, (screen_pos, 0))
        elif seconds < 35 and seconds > 25:
            screen.blit(cat4, (screen_pos, 0))
        elif seconds < 40 and seconds > 35:
            screen.blit(cat5, (screen_pos, 0))
        screen.blit(keyUI, (0, 0))
        mouseKeys[keyState].draw()

        for j in keyList:
            j.draw()

        keyList[keyState].drawHighlight()

        # hides mouse cursor
        pygame.mouse.set_cursor(
            (8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
    elif gameState == 1:
        # calculate the time since some reference point (here the Unix Epoch)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # this also closes the while loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameState = 4
        screen.blit(introScene, (0, 0))

    elif gameState == 2:
        screen.blit(lose, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # this also closes the while loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    doorlist = []
                    keyList = []
                    mouseKeys = []
                    gameState = 0
                    t0 = t1
                    x = 1
                    soundState = True
                    resetTimer = True
                    loadFile()
    elif gameState == 3:  # gameOver State
        screen.blit(win, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # this also closes the while loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    doorlist = []
                    keyList = []
                    mouseKeys = []
                    gameState = 0
                    t0 = t1
                    x = 1
                    soundState = True
                    resetTimer = True
                    loadFile()
    elif gameState == 4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # this also closes the while loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    t0 = t1
                    gameState = 0

        screen.blit(tutorial, (0, 0))

    pygame.display.update()
    clock.tick(60)  # constant frame rate
