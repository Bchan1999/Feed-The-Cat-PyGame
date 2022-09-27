from cgi import test
import pygame
from sys import exit

# starts pygmae and instantiates all libraries
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# conver() helps game run faster
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Red')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surf = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
# get_rect takes a surface and draws a rectangle around it
player_rect = player_surf.get_rect(midbottom=(80, 300))

# will never be false and must be broken from the inside
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # this also closes the while loop

    screen.blit(sky_surface, (0, 0))  # block image transfer
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    snail_x_pos -= 5
    if snail_x_pos == -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)  # constant frame rate
