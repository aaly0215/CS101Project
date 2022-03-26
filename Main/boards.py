import random

class Board:
    #class veri to lock in board size
    row = 9
    column = 10
    new_board = []
        
    def __init__(self, column = column, row = row) -> None:
        #automatically create new board with list comprehension
        self.board = [['O' for x in range(column)] for x in range(row)]
        self.coordinates = []

    def show_playboard(self) -> None:
        for b in self.board:
            print(*b)

    def place_boat(self, row = row, column = column) -> None:
        #pick a spot on current board
        row_choice = random.randint(1, row)
        col_choice = random.randint(1, column)
        print(row_choice)
        print(col_choice)
        boat_size = random.randint(2, 7)
        boat_direction = random.choice(['horizontal', 'vertical'])
        if boat_direction == 'horizontal':
            if boat_size + col_choice <= row:
                counter = 0
                for x in range(int(boat_size)):   
                    self.coordinates.append([int(row_choice)- 1, int(col_choice) - 1 + counter])             
                    self.board[int(row_choice )- 1][int(col_choice) - 1 + counter] = '0'
                    counter += 1
                    
            else:
                print('This boat went out of bounds!')
                self.place_boat()

        
        elif boat_direction == 'vertical':
            if boat_size + row_choice <= column:
                counter2 = 0           
                for x in range(int(boat_size)):
                    self.coordinates.append([int(row_choice )- 1 + counter2, int(col_choice) - 1])
                    self.board[int(row_choice )- 1 + counter2][int(col_choice) - 1] = '0'
                    counter2 += 1
                    
            else:
                    print('This boat went out of bounds!')
                    self.place_boat()
        else:
            print('You need to pick Horizontal or Vertical.')
        
  




       