import celestialbody as celbd
import spacemaths as smaths
import graphicsdefs as graphdefs
import wordlists
import newdrawing
import random
from tkinter import *
import screeninfo

def pop_galaxy(target: celbd.Galaxy):
        distanceFromCentre = 0

        for i in range(target.star_count):
            distanceFromCentre += random.randrange(1, 3) * (target.star_count * 0.0001)
            starAngle = random.randrange(-180, 180)
            new_star = celbd.Star(position=smaths.get_point_from_distance(target.width / 2, target.height / 2, distanceFromCentre, starAngle), colour=celbd.possible_colours[random.randint(0,len(celbd.possible_colours) - 1)], distanceFromCentre=distanceFromCentre, angle=starAngle, scale=random.uniform(0.5,2), index=i, name=wordlists.generate_word_from_syllables(1,3), parent_galaxy=target)
            target.star_list.append(new_star)
        for i in range(target.nebula_count):
            nebula_cloud_position = target.star_list[random.randint(0, target.star_count - 1)].position #smaths.Point(random.randint(0,target.width), random.randint(0,target.height))
            new_nebula_root = celbd.Nebula(position=nebula_cloud_position, scale=random.uniform(0.5,3), index=i)
            target.nebula_list.append(new_nebula_root)
            for new_nebula in range(random.randint(1,5)):
                new_nebula_offshoot = celbd.NebulaOffshoot(position=smaths.Point(nebula_cloud_position.x + random.randint(-16,16), nebula_cloud_position.y + random.randint(-16,16)), scale=random.uniform(0.5,2), index=i+new_nebula)
                target.nebula_list.append(new_nebula_offshoot)

def read_stars_from(galaxy: celbd.Galaxy):
    for star in range(len(galaxy.star_list)):
        index_star = galaxy.star_list[star]
        print("Star Index " + str(index_star.index))
        print("\n    Name: " + index_star.name)
        print("\n    Colour: #" + index_star.colour.convert_to_hex())
        print("\n    Position: x-axis = " + str(index_star.position.x) + "; y-axis = " + str(index_star.position.y))
        print("\n    Distance: " + str(index_star.distanceFromCentre))
        print("\n    Angle: " + str(index_star.angle))
        print("\n    Scale: " + str(index_star.scale) + "\n")
        #drawing.blit_star(window=window, star=index_star)
        #drawing.draw_star(colour=index_star.colour, position=index_star.position, size=index_star.scale)

def __main__():
    min_star_count = input("Minimum stars to generate (typically ~5,000,000,000): ")
    max_star_count = input("Maximum stars to generate (typically ~40,000,000,000): ")

    galaxy = celbd.Galaxy(star_count=random.randint(int(min_star_count), int(max_star_count)), star_list=[], nebula_count=random.randint(40,80), nebula_list=[], nebula_offshoot_list=[], width=screeninfo.screeninfo.get_monitors()[0].width, height=screeninfo.screeninfo.get_monitors()[0].height)

    pop_galaxy(galaxy)

    read_stars_from(galaxy)

    newdrawing.init(galaxy=galaxy)

__main__()