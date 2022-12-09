from cgi import test
import pygame
from sys import exit
from Door import *
from Key import *
from Player import *

# starts pygmae and instantiates all libraries


pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('FeedTheCat')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# conver() helps game run faster
cat_surface = pygame.image.load('graphics/cat.png').convert()
# ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Red')
keyUI = pygame.image.load('graphics/UI.png').convert_alpha()


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
doorlen = 5
x = 1

doorlist = []
keyList = []
mouseKeys = []

touching = False
posClick = any

rflag = False
lflag = False

# state
keyState = 0

# loads all door images from graphics
# x variable defines how many doors need to be loaded into the game
# A is closed door
# B is open door
while (x <= doorlen):
    file = 'graphics/Doors/Door' + str(x) + 'A.png'
    fileB = 'graphics/Doors/Door' + str(x) + 'B.png'
    door = Door(screen, rectx, recty, file, fileB)
    doorlist.append(door)

    keyFile = 'graphics/Keys/Key' + str(x) + '.png'
    keyHighlightFile = 'graphics/Keys/Key' + str(x) + 'H.png'
    key = Key(screen, keyFile, keyHighlightFile, rectx, recty)
    keyList.append(key)

    mouseFile = 'graphics/MouseKeys/Key' + str(x) + '.png'
    player = Player(mouseFile, screen)
    mouseKeys.append(player)
    x += 1


def addSpeed():
    print('yes')
    global screen_pos, rectx
    screen_pos += screen_change
    rectx += rect_change
    for i in doorlist:
        i.changeXandY(rectx)


# will never be false and must be broken from the inside
while True:
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
                screen_change = -15
                rect_change = -15
            elif event.key == pygame.K_LEFT:
                keyflag = True
                rflag = False
                lflag = True
                screen_change = 15
                rect_change = 15
            if event.key == pygame.K_UP:
                if (len(mouseKeys) - 1 == keyState):
                    keyState = 0
                else:
                    keyState += 1
                print(keyState)
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
                print(keyState)
        if event.type == pygame.MOUSEBUTTONUP:
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

    # collision
    for i in doorlist:
        # pos_in_mask = pos[0] - i.rect.x, pos[1] - i.rect.y
        # touching = i.rect.collidepoint(*pos) and i.mask.get_at(pos_in_mask)
        # if touching and pos == posClick:
        #
        i.draw()
        offsetX = i.rect.x - mouseKeys[keyState].keyRect.left
        offsetY = i.rect.y - mouseKeys[keyState].keyRect.top
        if mouseKeys[keyState].mask.overlap(i.mask, (offsetX, offsetY)) and pos == posClick:
            i.setFlag(True)

    screen.blit(text_surface, (350, 50))
    screen.blit(keyUI, (0, 0))
    mouseKeys[keyState].draw()

    for j in keyList:
        j.draw()

    # collision

    # hides mouse cursor
    pygame.mouse.set_cursor(
        (8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

    pygame.display.update()
    clock.tick(60)  # constant frame rate
