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
    def redraw(self,board):
        self.surface.fill(Constants.grey)
        sq = board.squares
        for row in range(len(sq)):
            for col in range(len(sq)):
                cur_sq = sq[row][col]
                top = row*16
                left = col*16
                self.surface.blit(pygame.image.load(cur_sq.img),(left,top))
                if cur_sq.neigh > 0 and not cur_sq.mine:
                    num_img = pygame.image.load(Constants.img[cur_sq.neigh])
                    self.surface.blit(num_img,(left+Constants.sq_num_offset,top+Constants.sq_num_offset))
        self.update()