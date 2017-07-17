'''
This program will launch a game of tetris.
'''

import time
import random

from Tkinter import *

root = Tk()
root.geometry('200x400-1700+200') 
canvas = Canvas(root, width=200, height=400) 
canvas.pack() 
SIZE = 20

class Shapes:
    ''' The tetris board shapes. '''
    shapes = {"cyan" : [(1, 1), (2, 1), (3, 1), (4, 1)],
              "yellow" : [(1, 2), (1, 1), (2, 2), (2, 1)]}
    def __init__(self):
        ''' Creates a random shape. '''
        self.squares = []
        shape_color = random.choice((Shapes.shapes).keys())
        coords = Shapes.shapes[shape_color]
        for coord in coords:
            (x, y) = coord
            square = canvas.create_rectangle(x * SIZE, y * SIZE, \
                (x * SIZE) + SIZE, (y * SIZE) + SIZE, \
                fill=shape_color, outline='black')

    def move(self):
        ''' Moves the shape down one block. '''
        pass
    def rotate(self):
        ''' Rotates the shape 90 degrees clockwise. '''
        pass


class Tetris_Game:
    ''' Play the game of tetris. '''
    def __init__(self):
        ''' This is the constructor for the tetris board and will initialize an 
        empty board. '''

        # The board is represented as a list of lists. Empty boxes are marked 
        # with '*' and filled boxes are marked with 'X'. 
        # The board has 20 columns and 10 rows. The row is the first index in 
        # the list and the column is the second index. 
        row = ['*'] * 20
        board = []
        for i in range(10):
            board.append(row[:])
        self.board = board
        self.score = 0

        # There are four possible kinds of blocks
        self.moves = ['X X \nX X', 'X X \n  X X', '    X \nX X X', 'X\nX\nX\nX']

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



tetris = Tetris_Game()
shapes = Shapes()

root.mainloop()
