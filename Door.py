import pygame


class Door:
    def __init__(self, x, screen, rectx, recty, closedImg, openImg):
        self.closed = pygame.image.load(closedImg).convert_alpha()
        self.open = pygame.image.load(openImg).convert_alpha()
        self.rect = self.closed.get_rect(center=(rectx, recty))
        self.mask = pygame.mask.from_surface(self.closed)
        self.rectB = self.open.get_rect(center=(rectx, recty))
        self.maskB = pygame.mask.from_surface(self.open)
        self.flag = False
        self.screen = screen
        self.x = x

    def draw(self):
        if self.flag:
            self.screen.blit(self.open, self.rect)
        else:
            self.screen.blit(self.closed, self.rect)

    def setFlag(self, flag):
        self.flag = flag

    def changeXandY(self, rectx):
        self.rect = self.closed.get_rect(center=(rectx, 500))

    def changeXandYB(self, rectx):
        self.rect = self.open.get_rect(center=(rectx, 500))
