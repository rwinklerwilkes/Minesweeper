import Constants
import random

__author__ = 'Rich'


class Board:
    def __init__(self,difficulty = 'medium'):
        self.diff = difficulty
        self.size = Constants.diff[difficulty]
        self.squares = self.create_squares()
    def create_squares(self):
        num_mines = Constants.mine[self.diff]
        s = self.size
        #size is the number of mines per row, which is also the number per column
        squares = []
        # need to pick num_mine squares to make into mines
        mines = pick_mines(num_mines,s)

        #this creates the array of squares
        for row in range(s):
            squares.append([])
            for column in range(s):
                squares[row].append(Square())

        #last, we need to set the mines
        for i in mines:
            squares[i[0]][i[1]].is_mine = True

        return squares

class Square:
    def __init__(self,is_down = False,is_mine=False,is_flagged=False):
        #the size in pixels - this is the size of the image 16x16
        self.size = 16
        self.down = is_down
        self.mine = is_mine
        self.flagged = is_flagged
        self.img = 'Images/square.png'
    def flag(self):
        self.flagged = not self.flagged

def pick_mines(num_mines,size):
    mines =[]
    row = [[i for i in range(size)] for j in range(size)]
    for i in range(num_mines):
        r = random.randint(0,len(row)-1)
        c = random.randint(0,len(row[r])-1)
        mines.append((r,row[r][c]))
        if len(row[r])==0:
            row.pop(r)
        row[r].pop(c)
    return mines