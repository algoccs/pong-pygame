from pygame import *
init()

SW, SH = 640, 480
FPS = 120

screen = display.set_mode((SW, SH))
display.set_caption('Pong')

class Character(sprite.Sprite):
    def __init__(self, img, cor_x, cor_y, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
        self.speed = speed

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

clock = time.Clock()
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)

quit()
