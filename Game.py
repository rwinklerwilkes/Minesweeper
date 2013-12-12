__author__ = 'Rich'
import pygame
import GUI
import Board
import Constants

class Game:
    def __init__(self):
        self.fps = 30
        self.clock = pygame.time.Clock()
        self.board = Board.Board()
        self.gui = GUI.GUI()
    def draw(self):
        self.gui.redraw(self.board)

def main():
    pygame.init()
    g = Game()
    while True:
        g.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == Constants.LEFT:
                pass
        g.clock.tick(g.fps)

if __name__ == '__main__':
    main()