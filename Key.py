import pygame


class Key:
    def __init__(self, screen, keyImg, keyHighlight, rectx, recty):
        self.keyImg = pygame.image.load(keyImg).convert_alpha()
        self.keyHighlight = pygame.image.load(keyHighlight).convert_alpha
        self.screen = screen

    def draw(self):
        self.screen.blit(self.keyImg, (0, 0))
