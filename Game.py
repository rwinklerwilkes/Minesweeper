__author__ = 'Rich'
import pygame
import GUI
import Board
import Constants

class Game:
    def __init__(self):
        self.fps = 30
        self.clock = pygame.time.Clock()
        self.gui = GUI.GUI()
        self.board = Board.Board()

def main():
    pygame.init()
    g = Game()
    while True:
        pass

if __name__ == '__main__':
    main()