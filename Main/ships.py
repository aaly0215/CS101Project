from boards import *

class Ship:
    def __init__(self, size) -> int:
        #define how long the ships are and which directions they will face
        self.size = size
        #i will set it to horizontal unless they change it
        self.orientation = 'horizontal'
        #where is the ship
        self.location = []

    def change_orientation(self):
        self.orientation = 'vertical'

    

