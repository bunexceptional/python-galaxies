##################
## Matrix maths ##
##################

from math import sin, cos, radians, pi

class Point:
    ''' Represents a 2-dimensional position in space '''
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def add(self, addend):
        ''' Add two 2D vectors, with the addend represented as a tuple '''
        self.x += addend[0]
        self.y += addend[0]

def get_point_from_distance(x0, y0, d, theta):
    theta_rad = pi/2 - radians(theta)
    return Point(x0 + d*cos(theta_rad), y0 + d*sin(theta_rad))