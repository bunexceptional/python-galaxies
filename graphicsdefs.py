##############################
## Graphics related classes ##
##############################

class Colour3: 
    ''' Defines an RGB colour '''
    def __init__(self, red:bytes, green:bytes, blue:bytes):
        self.red = red
        self.green = green
        self.blue = blue
    def convert_to_hex(self): 
        ''' Converts the RGB value of a Colour3 to a hexadecimal string excluding the '#' symbol. '''
        return '%02x%02x%02x' % (self.red, self.green, self.blue)
class Colour2: 
    ''' Defines an IA (intensity/alpha) colour '''
    def __init__(self, intensity:bytes, alpha:bytes):
        self.intensity = intensity
        self.alpha = alpha 