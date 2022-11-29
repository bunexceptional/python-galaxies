# python-galaxies
I though generating stars was an interesting idea, so I made it with python
## How it works
The actual code is a bit confusing (I have more experience with C/C++ and Java-style coding than Python), so I'll take some time to explain how it all works.
There is a module called `celestialbody.py` that contains classes describing celestial bodies. The `Galaxy` class is used to define the number of stars and contain them in a galaxy. The `Star` class, however, is used to define the `colour`, `position`, `scale`, `id`, `name`, etc. of a star.
Modules like `graphicsdefs` and `spacemaths` just contain classes that represent things like colour (in RGB and IA format) or a 2d vector, while modules like `wordlists` contain dictionaries that the program can pull from and execute functions on.
The `drawing` module uses Pyglet to quickly draw stars as sprites in a window. I was originally considering using `turtle`, but that method was too slow and clunky for this project.
The result is a nice looking window that contains stars at randomized positions and labels with their names
