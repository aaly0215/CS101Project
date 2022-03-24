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

    def place_boat(self, row = row, column = column) -> None:
        #pick a spot on current board
        row_choice = random.randint(1, row)
        col_choice = random.randint(1, column)
        print(row_choice)
        print(col_choice)
        boat_size = input('How long is the boat? ')
        boat_direction = input('Horizontal or Vertical? ').lower()
        if boat_direction == 'horizontal':            
            counter = 0
            for x in range(int(boat_size)):                
                self.board[int(row_choice )- 1][int(col_choice) - 1 + counter] = '0'
                counter += 1


        if boat_direction == 'vertical': 
            counter2 = 0           
            for x in range(int(boat_size)):
                self.board[int(row_choice )- 1 + counter2][int(col_choice) - 1] = '0'
                counter2 += 1
        
  




       