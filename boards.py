class Board:
    #class veri to lock in board size
    row = 9
    column = 10
        
    def __init__(self) -> None:
        pass

    def make_board(self, row = row, column = column) -> None:
        print('    [A] [B] [C] [D] [E] [F] [G] [H] [I] [J]')
        vert = 1
        for x in range(row):
            print(f'[{vert}] ' + '|  |' * column)
            vert += 1
board1 = Board()
board1.make_board()


        




        
