# python-galaxies
I though generating stars was an interesting idea, so I made it with python

## How it works
The actual code is a bit confusing (I have more experience with C/C++ and Java-style coding than Python), so I'll take some time to explain how it all works.
There is a module called `celestialbody.py` that contains classes describing celestial bodies. The `Galaxy` class is used to define the number of stars and contain them in a galaxy. The `Star` class, however, is used to define the `colour`, `position`, `scale`, `id`, `name`, etc. of a star.

Modules like `graphicsdefs` and `spacemaths` just contain classes that represent things like colour (in RGB and IA format) or a 2d vector, while modules like `wordlists` contain dictionaries that the program can pull from and execute functions on.

The `drawing` module uses Pyglet to quickly draw stars as sprites in a window. I was originally considering using `turtle`, but that method was too slow and clunky for this project.

The result is a nice looking window that contains stars at randomized positions and labels with their names

## Depenencies
This programme depends on:
* Pyglet

`pip3 install pyglet`
* NumPy

`pip3 install numpy`
* SimpleAudio

`pip3 install simpleaudio`
* PyOgg

`pip3 install pyogg`

Without these dependencies, you will not be able to use this programme.

## Known issues & incomplete features
* Gravity has no effect on generation, so stars are distributed randomly and the galaxy has no centre.
* Stars are completely static. they do not move, rotate, change brightness/colour, etc. after they are generated.
* Star colour is not based on size or lifetime like in real life.
* Stars have no lifetime and new ones are not created after generating a galaxy.
* There has not yet been any succesful implementation of dynamic audio (sounds for hovering over stars, moving the mouse pointer, ambient background noise, etc.)
* Star sprites are not labeled with their names because there is no way to store data in a sprite such as which star and label it corresponds to. (this is more a limitation of Pyglet than something this project can easily fix)
* Nebulae do not accurately represent the varieties seen in real life and do not have colour variation.
