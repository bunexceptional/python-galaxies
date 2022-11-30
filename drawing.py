import pyglet
import graphicsdefs as graphdefs
import spacemaths as smaths
import celestialbody as celbd
import pyogg
import simpleaudio as sa
import numpy as np
import time
from tkinter import *

def init_pyglet(galaxy:celbd.Galaxy):
    window = pyglet.window.Window()
    label = pyglet.text.Label('ViewSpace',
                          font_name='Verdana',
                          font_size=12,
                          x=window.width//2, y=window.height-25,
                          anchor_x='center', anchor_y='top')
    
    bg_image = pyglet.resource.image("gfx/window_bg-01.png")

    star_image = pyglet.image.load("gfx/star-01.png")
    star_image.anchor_x = star_image.width // 2
    star_image.anchor_y = star_image.height // 2

    star_batch = pyglet.graphics.Batch()
    star_sprites = []
    star_labels = []

    for star in range(len(galaxy.star_list)):
        index_star = galaxy.star_list[star]
        new_sprite = pyglet.sprite.Sprite(star_image, x=index_star.position.x, y=index_star.position.y, batch=star_batch, z=index_star.scale * 100)
        new_sprite.update(scale=index_star.scale * 0.025)
        new_sprite.color = (index_star.colour.red, index_star.colour.green, index_star.colour.blue)
        star_sprites.append(new_sprite)
        #new_label = pyglet.text.Label(index_star.name, font_name='Verdana', font_size=6, x=index_star.position.x, y=index_star.position.y - 2, anchor_x='center', anchor_y='top', batch=star_batch)
        #star_labels.append(new_label)
        

    for star_sprite in range(len(star_sprites)):
        index_sprite = star_sprites[star_sprite]
    
    mouse_move_sound = pyglet.resource.media('sound/mouse_move_alt.ogg', streaming=False)

    @window.event
    def on_draw():
        window.clear()
        bg_image.blit(0,0)
        star_batch.draw()
        label.draw()
    @window.event
    def on_mouse_motion(x, y, dx, dy):
        #mouse_move_sound.
        #mouse_move_sound.play()
        #time.sleep(0.5)
        #sine = pyglet.media.synthesis.Triangle(0.5, frequency=440, sample_rate=44800)
        #sine.play()
        #adsr = pyglet.media.synthesis.ADSREnvelope(attack=0.05, decay=0.2, release=0.1)
        #saw = pyglet.media.synthesis.Sine(duration=4, frequency=600, envelope=adsr)
        #saw.play()
        #time.sleep(5)
        for star_sprite in range(len(star_sprites)):
            index_sprite = star_sprites[star_sprite]
            #index_sprite.update(x=dx + index_sprite.x,y=dy + index_sprite.y)

    #@window.event
    #def on_mouse_scroll(x, y, scroll_x, scroll_y):
        #scroll_level = 0; scroll_level += scroll_y
        #for star_sprite in range(len(star_sprites)):
            #index_sprite = star_sprites[star_sprite]
            #index_sprite.update(scale=index_sprite.scale + scroll_level)
            #print(str(scroll_y))

    pyglet.app.run()

def blit_star(window, star:celbd.Star):
    star_image = pyglet.resource.image("gfx/star-01.png")
    @window.event
    def on_draw():
        star_image.blit(star.position.x, star.position.y)


#def draw_star(colour:graphdefs.Colour3, position:smaths.Vec2, size:float):
    # Turtle method (we don't use this because it's slow.)
    # t = Turtle()
    # t.color("#" + str(colour.convert_to_hex()))
    # t.setx(position.x)
    # t.sety(position.y)
    # t.begin_fill()
    # t.dot(size)
    # t.end_fill()