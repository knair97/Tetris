'''
This program will launch a game of tetris.
'''

import time
import random

class Tetris_Game:
    ''' Play the game of tetris. '''
    def __init__(self):
        ''' This is the constructor for the tetris board and will initialize an 
        empty board. '''

        # The board is represented as a list of lists. Empty boxes are marked 
        # with '*' and filled boxes are marked with 'X'. 
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

    def make_move(self):
        player_board = Tetris_Player(self.board)
    def solve(self, move):
        pass
    def print_move(self):
        print 'Next move: '
        print self.random_move()
        print '\n'
    def clear_line(self):
        pass
    def print_board(self):
        ''' This function will print out the current state of the board. '''
        for i in range(10):
            for j in range(20):
                print self.board[i][j],
            print '\n'

if __name__ == '__main__':
    tetris = Tetris_Game()

    while True:
        tetris.print_move()
        tetris.print_board()
        move = tetris.make_move()
        tetris.solve(move)
        print '\n', '\n'
        print 'Calculating next move ...'
        time.sleep(5)
