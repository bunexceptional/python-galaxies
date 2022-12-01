##################
## Matrix maths ##
##################

class Vec2:
    ''' Represents a 2-dimensional position in space '''
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def add(self, addend):
        ''' Add two 2D vectors, with the addend represented as a tuple '''
        self.x += addend[0]
        self.y += addend[0]
