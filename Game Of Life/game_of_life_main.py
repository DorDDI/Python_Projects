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

    def sum_num_8(self,i,j):  # return the sum of the 8 cell around
        big = self.size_of_board - 1  # the end of the rows or columns
        if (i == 0) and (j == 0):  # if is in the left up corner
            return (self.board[i][j + 1] + self.board[i + 1][j + 1] + self.board[i + 1][j] + self.board[i + 1][big] + \
                    self.board[i][big] + self.board[big][big] + self.board[big][j] + self.board[big][j + 1])
        elif (i == 0) and (j == big):  # if is in the right up corner
            return (self.board[1][big] + self.board[1][big - 1] + self.board[i][big - 1] + self.board[big][big - 1] + \
                    self.board[big][big] + self.board[big][0] + self.board[1][0] + self.board[0][0])
        elif (i == big) and (j == 0):  # if is in the left down corner
            return (self.board[big - 1][0] + self.board[big - 1][1] + self.board[big][1] + self.board[0][1] + \
                    self.board[0][0] + self.board[0][big] + self.board[big][big] + self.board[big - 1][big])
        elif (i == big) and (j == big):  # if is in the right down corner
            return (self.board[big][big - 1] + self.board[big - 1][big - 1] + self.board[big - 1][big] + self.board[big - 1][0] + \
                    self.board[big][0] + self.board[0][0] + self.board[0][big] + self.board[0][big-1])
        elif i == 0:  # in the first row
            return (self.board[i][j - 1] + self.board[big][j - 1] + self.board[big][j] + self.board[big][j + 1] + \
                    self.board[i][j + 1] + self.board[i + 1][j + 1] + self.board[i + 1][j] + self.board[i + 1][j - 1])
        elif i == big:  # in the last row
            return (self.board[i][j - 1] + self.board[i - 1][j - 1] + self.board[i - 1][j] + self.board[i-1][j+1] + \
                    self.board[i][j + 1] + self.board[0][j + 1] + self.board[0][j] + self.board[0][j - 1])
        elif j == 0:  # in the first column
            return (self.board[i - 1][j] + self.board[i - 1][j + 1] + self.board[i][j + 1] + self.board[i + 1][j + 1] + \
                    self.board[i + 1][j] + self.board[i + 1][big] + self.board[i][big] + self.board[i - 1][big])
        elif j == big:  # in the last column
            return (self.board[i + 1][j] + self.board[i + 1][j - 1] + self.board[i][j - 1] + self.board[i - 1][j - 1] + \
                    self.board[i - 1][j] + self.board[i + 1][0] + self.board[i][0] + self.board[i - 1][0])
        else:  # in the middle
            return (self.board[i - 1][j - 1] + self.board[i - 1][j] + self.board[i - 1][j + 1] + self.board[i][j - 1] + \
                    self.board[i][j + 1] + self.board[i + 1][j - 1] + self.board[i + 1][j] + self.board[i + 1][j + 1])

    def save_board_to_file(self,file_name):
        """ This method saves the current state of the game to a file. You should use Matplotlib for this.
        Input img_name donates the file name. Is a string, for example file_name = '1000.png'
        Output a file with the name that donates filename.
        """
        plt.imshow(self.board)
        plt.imsave(file_name,self.board)

    def display_board(self):
        """ This method displays the current state of the game to the screen. You can use Matplotlib for this.
        Input None.
        Output a figure should be opened and display the board.
        """
        plt.imshow(self.board)
        plt.pause(0.01)
        plt.show()

    def return_board(self):
        """ This method returns a list of the board position. The board is a two-dimensional list that every
        cell donates if the cell is dead or alive. Dead will be donated with 0 while alive will be donated with 255.
        Input None.
        Output a list that holds the board with a size of size_of_board*size_of_board.
        """
        return self.board.tolist()




if __name__ == '__main__': 
