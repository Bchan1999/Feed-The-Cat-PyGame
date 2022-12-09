import pygame


class Player:
    def __init__(self, key, screen):
        self.key = pygame.image.load(key).convert_alpha()
        self.keyRect = self.key.get_rect(center=(0, 0))
        self.mask = pygame.mask.from_surface(self.key)
        self.screen = screen

    def draw(self):
        if pygame.mouse.get_pos():
            self.keyRect.center = pygame.mouse.get_pos()  # update position
            self.screen.blit(self.key, self.keyRect.center)
