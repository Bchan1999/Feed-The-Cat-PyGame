from cgi import test
import pygame
from sys import exit

# starts pygmae and instantiates all libraries


class Door:
    def __init__(self, rectx, recty, img):
        self.img = pygame.image.load(img).convert_alpha()
        self.rect = self.img.get_rect(center=(rectx, recty))
        self.mask = pygame.mask.from_surface(self.img)

    def changeXandY(self, rectx):
        self.rect = self.img.get_rect(center=(rectx, 500))


pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('FeedTheCat')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# conver() helps game run faster
cat_surface = pygame.image.load('graphics/cat.png').convert()
# ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Red')

# Place Doors
#d1A = pygame.image.load('graphics/Door1A.png').convert_alpha()
d1B = pygame.image.load('graphics/Door1B.png').convert()


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


door = Door(rectx, recty, 'graphics/Door1A.png')
door2 = Door(rectx, recty, 'graphics/cuckooclock.png')

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
                screen_change = -8
                rect_change = -8
            elif event.key == pygame.K_LEFT:
                keyflag = True
                screen_change = 8
                rect_change = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                screen_change = 0
                rect_change = 0
                keyflag = False
            elif event.key == pygame.K_LEFT:
                screen_change = 0
                rect_change = 0
                keyflag = False

    if keyflag == True:
        screen_pos += screen_change
        rectx += rect_change
        door.changeXandY(rectx)

    if screen_pos >= screenLeftMax:
        screen_pos = screenLeftMax
    if screen_pos <= screenRightMax:
        screen_pos = screenRightMax

    #screen.blit(d1A, (screen_pos, 0))
    # screen.blit(ground_surface, (0, 300))

    pos = pygame.mouse.get_pos()
    pos_in_mask = pos[0] - door.rect.x, pos[1] - door.rect.y
    touching = door.rect.collidepoint(*pos) and door.mask.get_at(pos_in_mask)
    if touching:
        print('touch')

    screen.fill(pygame.Color('red') if touching else pygame.Color('green'))
    screen.blit(cat_surface, (screen_pos, 0))  # block image transfer
    screen.blit(door.img, door.rect)
    screen.blit(door2.img, door2.rect)

    screen.blit(text_surface, (350, 50))

    pygame.display.update()
    clock.tick(60)  # constant frame rate
