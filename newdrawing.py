import pygame
import celestialbody as celbd

background = pygame.image.load("gfx/window_bg-01.png")
star = pygame.image.load("gfx/star-01.png")
nebula = pygame.image.load("gfx/nebula_cloud-01.png")

class StarSprite(pygame.sprite.Sprite):
    def __init__(self, color, scale, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = star

        self.image = pygame.transform.scale(self.image, (scale, scale))

        fill(self.image, color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class NebulaSprite(pygame.sprite.Sprite):
    def __init__(self, scale, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = nebula

        self.image = pygame.transform.scale(self.image, (scale, scale))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def init(galaxy):
    pygame.init()
    screen = pygame.display.set_mode((galaxy.width, galaxy.height))
    clock = pygame.time.Clock()
    running = True

    star_sprites = pygame.sprite.Group()
    nebula_sprites = pygame.sprite.Group()

    zoom_level = 1

    while running:
        # Poll events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            zoom_level += 0.1
            zoom_level = round(zoom_level, 1)
            if zoom_level > 2:
                zoom_level = 2
        elif pressed[pygame.K_DOWN]:
            zoom_level -= 0.1
            zoom_level = round(zoom_level, 1)
            if zoom_level < 0.1:
                zoom_level = 0.1
        #print(zoom_level)

        # Simulation
        galaxy.simulate(clock.get_time(), 0.5)

        # Clear last frame
        screen.fill((24, 20, 36))
        #screen.blit(background, (0, 0))

        star_sprites.empty()
        nebula_sprites.empty()

        # Render
        for star in range(len(galaxy.star_list)):
            index_star = galaxy.star_list[star]
            StarSprite(pygame.Color(index_star.colour.red, index_star.colour.green, index_star.colour.blue), index_star.scale * 5, index_star.position.x, index_star.position.y).add(star_sprites)
        for nebula in range(len(galaxy.nebula_list)):
            index_nebula = galaxy.nebula_list[nebula]
            NebulaSprite(index_nebula.scale * 20, index_nebula.position.x, index_nebula.position.y).add(nebula_sprites)

        star_sprites.draw(screen)
        nebula_sprites.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))