import random
import spacemaths as smaths
import graphicsdefs as graphdefs

possible_colours=[graphdefs.Colour3(255, 109, 22),graphdefs.Colour3(255, 196, 80),graphdefs.Colour3(164, 194, 255)]

class Body:
    ''' Base class for all celestial bodies, though the values don't seem to carry over to inheriting classes '''
    def __init__(self, position:smaths.Point):
        self.position = position

class Galaxy:
    ''' Galaxies define the star count and contain a list of every star and nebula '''
    def __init__(self, star_count:int, star_list, nebula_count:int, nebula_list, nebula_offshoot_list, width, height):
        self.star_count = star_count
        self.star_list = star_list
        self.nebula_count = nebula_count
        self.nebula_list = nebula_list
        self.nebula_offshoot_list = nebula_offshoot_list
        self.width = width
        self.height = height

    def simulate(self, tick, speed):
        for star in self.star_list:
            star.angle += tick * (speed / star.distanceFromCentre)
            star.position = smaths.get_point_from_distance(self.width / 2, self.height / 2, star.distanceFromCentre, star.angle)

class Star(Body):
    ''' Stars inherit from Body, but contain a scale, index, colour, and name '''
    def __init__(self, position:smaths.Point, distanceFromCentre, angle, colour:graphdefs.Colour3, scale:float, index:int, name:str, parent_galaxy:Galaxy, possible_colours=[graphdefs.Colour3(247, 109, 22),graphdefs.Colour3(242, 196, 80),graphdefs.Colour3(130, 176, 255)]):
        self.parent_galaxy = parent_galaxy
        self.position = position
        self.distanceFromCentre = distanceFromCentre
        self.angle = angle
        self.colour = colour
        self.scale = scale
        self.index = index
        self.name = name
        self.possible_colours = possible_colours

class Nebula(Body):
    ''' Nebulae inherit from Body, similarly to stars, but have fewer new properties '''
    def __init__(self, position:smaths.Point, scale:float, index:int):
        self.position = position
        self.scale = scale
        self.index = index
class NebulaOffshoot(Body):
    ''' Nebulae inherit from Body, similarly to stars, but have fewer new properties '''
    def __init__(self, position:smaths.Point, scale:float, index):
        self.position = position
        self.scale = scale
        self.index = index