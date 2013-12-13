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
                x,y = pygame.mouse.get_pos()
                sq = g.board.get_square_at(x,y)
                if sq.neigh==0 and not sq.mine:
                    g.board.draw_neighbors(sq)
                elif not sq.down:
                    sq.set_down()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == Constants.RIGHT:
                x,y = pygame.mouse.get_pos()
                sq = g.board.get_square_at(x,y)
                sq.set_flag()

        g.clock.tick(g.fps)


if __name__ == '__main__':
    main()