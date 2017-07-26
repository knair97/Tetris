'''
This program will launch a game of tetris.
'''

import time
import random

from Tkinter import *

SIZE = 20

'''
Coordinates:
x0 = 2
y0 = 2
x1 = 201
y1 = 375
'''
class Squares:
    ''' The squares that make up the tetris board shapes. '''
    def __init__(self, board, canvas, color, x1, y1, x2, y2):
        ''' Creates a square at the given location. '''
        self.handle = canvas.create_rectangle(x1, y1, x2, y2, fill=color, \
            outline='black')
        self.location = (x1, y1)
    def can_move_square(self, board, canvas, x, y):
        ''' This function will check if the square can be moved to the desired
        location by checking the state of the board. '''
        (x1, y1, x2, y2) = canvas.bbox(self.handle)
        new_x = x1 + x
        new_y = y1 + y
        can_move = True
        if new_x > 182:
            can_move = False
        if new_y > 422:
            can_move = False
        if can_move == True and board[(new_y + y) / 20][(new_x + x) / 20] != '*':
            can_move = False

        return can_move

    def move_square(self, board, canvas, x, y):
        ''' This function will move the square to the x and y coordinates. '''
        canvas.move(self.handle, x, y)

    def get_coords(self, canvas):
        ''' This function will return the coordinates of the square. '''
        return canvas.bbox(self.handle)

    def get_handle(self, canvas):
        ''' This function will return the handle of the square. '''
        return self.handle

class Shapes:
    ''' The tetris board shapes. '''
    shapes = {"cyan" : [(1, 1), (2, 1), (3, 1), (4, 1)],
              "yellow" : [(1, 2), (1, 1), (2, 2), (2, 1)]}
    def __init__(self, canvas, board):
        ''' Creates a random shape. '''
        self.location = (0, 0)
        self.squares = []
        shape_color = random.choice((Shapes.shapes).keys())
        coords = Shapes.shapes[shape_color]
        for coord in coords:
            (x, y) = coord
            square = Squares(board, canvas, shape_color, 40 + (x * SIZE), \
                40 + (y * SIZE), (x * SIZE) + SIZE + 40, (y * SIZE) + SIZE + 40)
            self.squares.append(square)

    def can_move_shape(self, x, y, canvas, board):
        ''' This function will check if the current shape can be moved to the 
        desired position. '''
        can_move = True
        for square in self.squares:
            if not square.can_move_square(board, canvas, x, y):
                can_move = False


        return can_move

    def move(self, x, y, canvas, board):
        ''' Moves the shape given the x and y distance. '''
        if self.can_move_shape(x, y, canvas, board):
            for square in self.squares:
                square.move_square(board, canvas, x, y)
            return False

        else:            
            for square in self.squares:
                (x1, y1, x2, y2) = square.get_coords(canvas)
                board[(y1 + y) / 20][(x1 + x) / 20] = square.get_handle(canvas)
            return True
    def rotate(self):
        ''' Rotates the shape 90 degrees clockwise. '''
        pass


class Tetris_Game:
    ''' Play the game of tetris. '''
    def __init__(self):
        ''' This is the constructor for the tetris board and will initialize a 
        board with a shape. '''

        '''
        The width of the board is 20 units * 10. The height of the board is 22 
        units. 
        '''

        self.root = Tk()
        self.root.title("Tetris")
        self.root.geometry('201x467') #-1700+200')
        self.root.bind('<Key>', self.key_handler)
        self.level = StringVar()
        Label(self.root, textvariable=self.level, font=("Helvetica", 10, \
            "bold")).pack()
        self.level.set("Level : 1")
        self.canvas = Canvas(self.root, width=201, height=467) 
        self.canvas.pack() 

        ''' Keep track of the state of the board by having a list of lists. 
        This list will only be used to determine which spaces are used and which
        spaces are free. '''
        self.board = []
        lst = []
        for i in range(10):
            lst.append('*')
        for i in range(22):
            self.board.append(lst[:])

        self.shape = Shapes(self.canvas, self.board)

        # r = self.canvas.create_rectangle(2, 2, 202, 442, fill='red', outline='black')



        self.root.after(1000, self.timer)
        #self.timer()
        self.root.mainloop()

        # TODO: Delete

        
    def timer(self):
        ''' This function is called every few seconds and causes the shape to 
        fall down by 20 units. '''
        new_shape = self.shape.move(0, 20, self.canvas, self.board)
        if new_shape:
            self.shape = Shapes(self.canvas, self.board)

        self.root.after(1000, self.timer)

    def key_handler(self, event):
        print 'Hello'
        
    def random_move(self):
        return random.choice(self.moves)
    def make_move(self, move, piece):
        ''' The move argument passed in is an integer that represents the column
        where the left most corner of the piece will be placed. '''
        # If this is a square piece
        if piece == 'X X \nX X':
            valid_move = False
            for i in range(9, -1, -1):
                # Check if there is enough space for a square piece
                if self.board[i][move] == '*' and \
                self.board[i][move + 1] == '*' and \
                self.board[i - 1][move] == '*' and \
                self.board[i - 1][move + 1] == '*':
                    # Add the square piece
                    self.board[i][move] = 'X'
                    self.board[i][move + 1] = 'X'
                    self.board[i - 1][move] = 'X'
                    self.board[i - 1][move + 1] = 'X'
                    valid_move = True
                    break

        if piece == 'X X \n  X X':
            valid_move = False
            for i in range(8, -1, -1):
                # Check if there is enough space for a z piece
                if self.board[i][move] == '*' and \
                self.board[i][move + 1] == '*' and \
                self.board[i + 1][move + 1] == '*' and \
                self.board[i + 1][move + 2] == '*':
                    # Add the z piece
                    self.board[i][move] = 'X'
                    self.board[i][move + 1] = 'X'
                    self.board[i + 1][move + 1] = 'X'
                    self.board[i + 1][move + 2] = 'X'
                    valid_move = True
                    break
        if piece == '    X \nX X X':
            pass

        if not valid_move:
            print 'Not a valid move. Try again.'
        return valid_move
    def find_move(self):
        pass
    def solve(self, move):
        pass
    def clear_line(self):
        pass
    def get_score(self, board):
        ''' This function will return the score of the board state passed in. 
        '''
        # Get a list of possible moves and then calculate the board score for
        # each of the moves. The list will be a list of board states. 
        # 1) Embedded hole penalty
        # 2) Height penalty
        # 3) Line reward
        # 4) Column reward
        # 5) Column penalty
        # 6) Double column penalty
        pass
    def get_moves(self, piece):
        ''' This function returns a list of possible moves given a piece. '''
        # Hard code the four cases for the four different pieces. However, once
        # rotating pieces is allowed, come up with a better way. 
        moves = []
        if piece == 'X X \nX X':
            for i in range(19):
                for j in range(19):
                    board = self.board
                    board[i][j] = 'X'
                    board[i][j + 1] = 'X'
                    board[i + 1][j] = 'X'
                    board[i + 1][j + 1] = 'X'
                    self.print_board(board)

    def print_board(self, board):
        ''' This function will print out the current state of the board. '''
        for i in range(10):
            for j in range(20):
                print board[i][j],
            print '\n'


if __name__ == '__main__':
    tetris = Tetris_Game()
