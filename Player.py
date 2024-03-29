import pygame


class Player:
    def __init__(self,x, key, screen):
        self.key = pygame.image.load(key).convert_alpha()
        self.keyRect = self.key.get_rect(center=(300, 300))
        self.mask = pygame.mask.from_surface(self.key)
        self.screen = screen
        self.x = x

    def draw(self):
        if pygame.mouse.get_pos():
            self.keyRect.center = pygame.mouse.get_pos()  # update position
        self.screen.blit(self.key, self.keyRect)
