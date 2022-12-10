import pygame


class Key:
    def __init__(self, x,  screen, keyImg, keyHighlight, rectx, recty):
        self.keyImg = pygame.image.load(keyImg).convert_alpha()
        self.keyHighlight = pygame.image.load(keyHighlight).convert_alpha()
        self.screen = screen
        self.x = x

    def draw(self):
        self.screen.blit(self.keyImg, (0, 0))

    def drawHighlight(self):
        self.screen.blit(self.keyHighlight, (0, 0))
