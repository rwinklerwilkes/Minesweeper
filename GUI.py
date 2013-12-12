import pygame
import Constants

__author__ = 'Rich'
class GUI:
    def __init__(self,difficulty = 'medium'):
        self.size = 16*Constants.diff[difficulty]
        self.surface = pygame.display.set_mode((self.size,self.size))
        self.surface.fill(Constants.grey)
        pygame.display.update()
    def update(self):
        pygame.display.update()
    def draw(self,image):
        self.surface.blit()