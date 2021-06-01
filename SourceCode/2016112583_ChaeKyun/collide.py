import pygame as p

p.init()
win = p.display.set_mode((1000, 700))
p.display.set_caption('Pixel Perfect Collision')

FPS = 120
clock = p.time.Clock()


class Star(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self):
        win.blit(self.image, (self.x, self.y))

obstacle = p.image.load('SourceCode/Image/Catus.png').convert_alpha()
obstacle = p.transform.scale(obstacle, (100, 100))
obstacle_mask = p.mask.from_surface(obstacle)
bullet1 = p.image.load('SourceCode/Image/DesertLV1Car.png').convert_alpha()
bullet1 = p.transform.scale(bullet1, (75,75))
bullet2 = p.image.load('SourceCode/Image/bullet.png').convert_alpha()
bullet2 = p.transform.scale(bullet2, (75,75))

bullet_mask = p.mask.from_surface(bullet1)

ox = 160
oy = 50

bullet = Star(100, 100, bullet1)

run = True
while run:
    clock.tick(FPS)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    bullet.x, bullet.y = p.mouse.get_pos()

    offset = (int(bullet.x - ox), int(bullet.y - oy))
    collision = obstacle_mask.overlap(bullet_mask, offset)

    if collision:
        bullet.image = bullet1

    else:
        bullet.image = bullet2
    #DRAW
    win.fill((0,0,0))
    win.blit(obstacle, (ox, oy))
    bullet.draw()

    p.display.update()

