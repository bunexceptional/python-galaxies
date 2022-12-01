import spacemaths as smaths
import graphicsdefs as graphdefs

possible_colours=[graphdefs.Colour3(247, 109, 22),graphdefs.Colour3(242, 196, 80),graphdefs.Colour3(164, 194, 245)]

class Body:
    ''' Base class for all celestial bodies, though the values don't seem to carry over to inheriting classes '''
    def __init__(self, position:smaths.Vec2):
        self.position = position

class Galaxy:
    ''' Galaxies define the star count and contain a list of every star and nebula '''
    def __init__(self, star_count:int, star_list, nebula_count:int, nebula_list, nebula_offshoot_list):
        self.star_count = star_count
        self.star_list = star_list
        self.nebula_count = nebula_count
        self.nebula_list = nebula_list
        self.nebula_offshoot_list = nebula_offshoot_list

class Star(Body):
    ''' Stars inherit from Body, but contain a scale, index, colour, and name '''
    def __init__(self, position:smaths.Vec2, colour:graphdefs.Colour3, scale:float, index:int, name:str, parent_galaxy:Galaxy, possible_colours=[graphdefs.Colour3(247, 109, 22),graphdefs.Colour3(242, 196, 80),graphdefs.Colour3(130, 176, 255)]):
        self.parent_galaxy = parent_galaxy
        self.position = position
        self.colour = colour
        self.scale = scale
        self.index = index
        self.name = name
        self.possible_colours = possible_colours

class Nebula(Body):
    ''' Nebulae inherit from Body, similarly to stars, but have fewer new properties '''
    def __init__(self, position:smaths.Vec2, scale:float, index:int):
        self.position = position
        self.scale = scale
        self.index = index
class NebulaOffshoot(Body):
    ''' Nebulae inherit from Body, similarly to stars, but have fewer new properties '''
    def __init__(self, position:smaths.Vec2, scale:float, index):
        self.position = position
        self.scale = scale
        self.index = index