import game_of_life_interface
import numpy as np
import matplotlib.pyplot as plt


class GameOfLife(game_of_life_interface.GameOfLife):  

def __init__(self, size_of_board, board_start_mode, rules, rle="", pattern_position=(0, 0)):
        """ init method for class GameOfLife.
        Input size_of_board donates the size of the board, is an integer bigger than 9 and smaller than 1000.
        board_start_mode donates the starting position options, please refer to the added PDF file. Is an integer.
        rules donates the rules of the game. Is a string
        rle: is a str[optional]. the coding for a pattern, if there is an rle coding than the board_start_mode is overlooked,
             if there isn't an rle, than use the board_start_mode.
        pattern_position: is a tuple of two integers (x,y). the upper left position of the pattern on the board,
                          only used if in rle mode.
        Output None.
        """
        self.size_of_board = size_of_board
        self.board_start_mode = board_start_mode
        self.rules = rules
        self.rle = rle
        self.pattern_position = pattern_position
        self.dead = 0
        self.alive = 255
        self.board = self.start()  # start new matrix to board





if __name__ == '__main__': 
