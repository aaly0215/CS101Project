from boards import *
from ships import *

board1 = Board()
ship1 = board1.place_boat()

board1.show_playboard()
print(board1.coordinates)
    