from boards import *


board1 = Board()
turns = 30

    
print('Welcome to Battleship Galactica!')
amt_ships = pick_int('How many ships do you want to fight? ')
for amt in range(amt_ships):
    board1.place_boat()
print(len(board1.coordinates))
#gameloop
while board1.hits < len(board1.coordinates) and turns > 0:
    print(board1.coordinates)
    board1.show_playboard()
    board1.shoot()
    turns -= 1
    print(board1.hits)
    board1.count_hits()
    
if board1.hits == len(board1.coordinates):
    print('You sank every fucking ship.')
    exit()
if turns <= 0:
    print('You ran out of turns, try again loser.')
    exit()