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


    def start(self):
        if self.rle == "":
            if self.board_start_mode == 2:
                return np.random.choice([self.dead, self.alive], self.size_of_board*self.size_of_board, p=[0.2, 0.8]).reshape(self.size_of_board,self.size_of_board)
            elif self.board_start_mode == 3:
                return np.random.choice([self.dead, self.alive], self.size_of_board*self.size_of_board, p=[0.8, 0.2]).reshape(self.size_of_board,self.size_of_board)
            elif self.board_start_mode == 4:
                self.pattern_position = (10,10)
                x, y = self.row_col("24bo11b$22bobo11b$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o14b$2o8bo3bob2o4bobo11b$10bo5bo7bo11b$11bo3bo20b$12b2o!")
                arr = self.transform_rle_to_matrix("24bo11b$22bobo11b$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o14b$2o8bo3bob2o4bobo11b$10bo5bo7bo11b$11bo3bo20b$12b2o!")
                return self.rle_to_board(arr,x,y)
            else:
                return np.random.choice([self.dead, self.alive], self.size_of_board*self.size_of_board, p=[0.5, 0.5]).reshape(self.size_of_board,self.size_of_board)
        else:
            x,y = self.row_col(self.rle)
            arr = self.transform_rle_to_matrix(self.rle)
            return self.rle_to_board(arr,x,y)

    def update(self):
        """ This method updates the board game by the rules of the game. Do a single iteration.
        Input None.
        Output None.
        """
        new_board = self.board.copy()
        born, survive = self.rule_read()
        for i in range(self.size_of_board):
            for j in range(self.size_of_board):
                if self.board[i][j] == 0:  # check if the cell is dead
                    sum = self.sum_num_8(i, j)
                    if str(int(sum/255)) in born:  # check if the cell can be born
                        new_board[i][j] = 255
                else:    # check if the cell is alive
                    sum = self.sum_num_8(i, j)
                    if str(int(sum / 255)) in survive:  # check if the cell can survive
                        pass
                    else:
                        new_board[i][j] = 0
        self.board = new_board.copy()




if __name__ == '__main__': 
