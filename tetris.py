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
        if new_x > 182 or new_x < 1:
            can_move = False
        if new_y > 422:
            can_move = False
        if can_move == True and board[(new_y) / 20][(new_x) / 20] != '*':
            can_move = False

        return can_move

    def move_square(self, board, canvas, x, y):
        ''' This function will move the square the x and y coordinates. '''
        canvas.move(self.handle, x, y)

    def get_coords(self, canvas):
        ''' This function will return the coordinates of the square. '''
        return canvas.bbox(self.handle)

    def get_handle(self, canvas):
        ''' This function will return the handle of the square. '''
        return self.handle

class Shapes:
    ''' The tetris board shapes. '''
    shapes = {"cyan" : [(0, 0), (1, 0), (2,0), (3,0)], 
              "yellow" : [(1, 0), (0, 0), (1, 1), (0, 1)],
              "blue" : [(0, 0), (1, 0), (2, 0), (2, 1)],
              "purple" : [(0, 0), (1, 0), (1, 1), (2, 0)]}
    def __init__(self, canvas, board):
        ''' Creates a random shape. '''
        self.location = (0, 0)
        self.squares = []
        shape_color = random.choice((Shapes.shapes).keys())
        self.color = shape_color
        coords = Shapes.shapes[shape_color]
        self.coords = coords
        for coord in coords:
            (x, y) = coord
            square = Squares(board, canvas, shape_color, 2 + (x * SIZE), \
                2 + (y * SIZE), 2 + (x * SIZE) + SIZE, \
                2 + (y * SIZE) + SIZE)
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
                board[(y1) / 20][(x1) / 20] = square.get_handle(canvas)
            return True
    

    def rotate(self, canvas, board):
        ''' Rotates the shape 90 degrees clockwise. '''
        #if self.can_rotate_shape():
        pivot = self.coords[1]
        (x_pivot, y_pivot) = pivot
        for i in range(len(self.coords)):
            if i != 1:
                (x, y) = self.coords[i]
                dx = x - x_pivot
                dy = y - y_pivot
                x_change = - dy - dx
                y_change = dx - dy

                self.coords[i] = (x + x_change, y + y_change)

                (self.squares[i]).move_square(board, canvas, x_change * 20, \
                    y_change * 20)





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
        self.root.geometry('201x467-1700+200')
        self.root.bind('<Key>', self.key_handler)
        self.level = StringVar()
        Label(self.root, textvariable=self.level, font=("Helvetica", 10, \
            "bold")).pack()
        self.level.set("Tetris")
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

        self.root.after(500, self.timer)
        # self.timer()
        self.root.mainloop()

        # TODO: Delete

        
    def timer(self):
        ''' This function is called every few seconds and causes the shape to 
        fall down by 20 units. '''
        new_shape = self.shape.move(0, 20, self.canvas, self.board)
        if new_shape:
            self.shape = Shapes(self.canvas, self.board)
        self.check_for_lines()
        self.root.after(250, self.timer)


    def check_for_lines(self):
        ''' This function will clear a line of the board if it is full. '''
        lst = []
        squares = []
        number_lines = 0
        fix_squares = 0
        for row in range(21, -1, -1):
            if '*' not in self.board[row]:
                self.clear_line(row)
                for i in range(row):
                    for j in range(10):
                        if self.board[i][j] != '*' and \
                        self.board[i][j] not in lst:
                            self.canvas.move(self.board[i][j], 0, \
                                20)
                            lst.append(self.board[i][j])
                            squares.append((self.board[i][j], i, j))
                            fix_squares += 1
        if fix_squares:
                for row in range(22):
                    for column in range(10):
                        self.board[row][column] = '*'
                for square in squares:
                    (handle, i, j) = square
                    self.board[i + 1][j] = handle
              

    def clear_line(self, row):
        ''' This function will clear all of the elements in the row that is 
        passed in. '''
        for i in range(10):
            self.canvas.delete(self.board[row][i])
            self.board[row][i] = '*'

    def key_handler(self, event):
        key = event.keysym
        if key == 'Left':
            self.shape.move(-20, 0, self.canvas, self.board)
        elif key == 'Right':
            self.shape.move(20, 0, self.canvas, self.board)
        elif key == 'Up':
            self.shape.rotate(self.canvas, self.board)
        
    def random_move(self):
        return random.choice(self.moves)
    
    def find_move(self):
        pass
    def solve(self, move):
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
