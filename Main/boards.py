import random

class Board:
    #class veri to lock in board size
    row = 9
    column = 10
    new_board = []
        
    def __init__(self, column = column, row = row) -> None:
        #automatically create new board with list comprehension
        self.board = [['O' for x in range(column)] for x in range(row)]

    def show_playboard(self) -> None:
        for b in self.board:
            print(*b)





board1 = Board()
board1.show_playboard()




    


        




       