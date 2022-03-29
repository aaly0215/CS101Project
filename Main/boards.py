import random



def pick_int(question: str)-> int:
    while True:
        answer = input(question)   
        try:
            return int(answer)
        except ValueError:
            print('You have to pick a number!')
        


class Board:
    #class veri to lock in board size
    row = 9
    column = 10
    hits = 0
        
    def __init__(self, column = column, row = row) -> None:
        #automatically create new board with list comprehension
        self.board = [['O' for x in range(column)] for x in range(row)]
        self.coordinates = []
        

    def show_playboard(self) -> None:
        for b in self.board:
            print(*b)

    def place_boat(self, row = row, column = column) -> None:
        #picks a spot on current board
        row_choice = random.randint(1, row)
        col_choice = random.randint(1, column)        
        boat_size = random.randint(2, 7)
        boat_direction = random.choice(['horizontal', 'vertical'])
        if boat_direction == 'horizontal':
            if boat_size + col_choice <= row:
                print(f'There is a boat that is {boat_size} spaces long.')
                counter = 0            
                for x in range(int(boat_size)):   
                    self.coordinates.append([int(row_choice)- 1, int(col_choice) - 1 + counter])             
                    #self.board[int(row_choice )- 1][int(col_choice) - 1 + counter] = '*'
                    counter += 1
                    
            else:                
                self.place_boat()

        
        elif boat_direction == 'vertical':
            if boat_size + row_choice <= column:
                print(f'There is a boat that is {boat_size} spaces long.')
                counter2 = 0                
                for x in range(int(boat_size)):
                    self.coordinates.append([int(row_choice )- 1 + counter2, int(col_choice) - 1])
                    #self.board[int(row_choice )- 1 + counter2][int(col_choice) - 1] = '*'
                    counter2 += 1
                    
            else:                
                    self.place_boat()

    def shoot(self) -> None:
        while True:
            try:
                x = pick_int('Pick a row ')
                y = pick_int('Pick a column ')
                shot_coordinates = [x - 1, y - 1]
                if shot_coordinates in self.coordinates:
                    print('You hit my ship!')
                    self.board[x - 1][y - 1] = '*'
                    break
                else:
                    print('You missed!')
                    self.board[x - 1][y - 1] = 'X'
                    break
            except IndexError:
                print('You missed the ocean! ')

    def count_hits(self) -> None:
        hit_count = 0
        for hit_list in self.board:
            hit_count += hit_list.count('*')
        return hit_count
