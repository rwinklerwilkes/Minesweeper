import Constants
import random
import math

__author__ = 'Rich'


class Board:
    def __init__(self,difficulty = 'medium'):
        self.diff = difficulty
        self.size = Constants.diff[difficulty]
        self.squares = self.create_squares()
        self.set_neigh()


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
                squares[row].append(Square(row,column))

        #last, we need to set the mines
        for i in mines:
            squares[i[0]][i[1]].mine = True

        return squares


    def set_neigh(self):
        for row in range(len(self.squares)):
            for col in range(len(self.squares)):
                n = self.neighbors(row,col)
                self.squares[row][col].neigh = len(n)


    def neighbors(self,row,col):
        s = self.squares
        neighbors = []
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if i<0 or i>=len(s):
                    continue
                elif j<0 or j>=len(s[i]):
                    continue
                elif i==row and j==col:
                    continue
                if s[i][j].mine:
                    neighbors.append(s[i][j])
        return neighbors

    def all_neighbors(self,row,col):
        neighbors = []
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if i<0 or i>=len(self.squares):
                    continue
                if j<0 or j>=len(self.squares[i]):
                    continue
                if not self.squares[i][j].down:
                    neighbors.append(self.squares[i][j])
        return neighbors

    def draw_neighbors(self,square):
        stack = [square]
        while len(stack) > 0:
            cur_sq = stack.pop()
            cur_sq.set_down()
            if cur_sq.neigh == 0:
                stack += self.all_neighbors(cur_sq.row,cur_sq.col)


    def get_square_at(self,x,y):
        x_val = int(math.floor(x/16))
        y_val = int(math.floor(y/16))
        return self.squares[y_val][x_val]


class Square:
    def __init__(self,row,col,is_down = False,is_mine=False,is_flagged=False,neigh=0,):
        #the size in pixels - this is the size of the image 16x16
        self.size = 16
        #whether the square has been clicked
        self.down = is_down
        #if the square is a mine
        self.mine = is_mine
        #if the user has flagged the square
        self.flagged = is_flagged
        self.img = Constants.img_square
        self.neigh = neigh
        self.row = row
        self.col = col

    def set_flag(self):
        if not self.down:
            self.flagged = not self.flagged
            self.img = (self.img + 1) % 2

    def get_img(self):
        return Constants.img[self.img]

    def set_down(self):
        self.down = True
        if not self.mine:
            self.img = Constants.img_down
        else:
            self.img = Constants.img_mine


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