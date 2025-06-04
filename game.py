from pygame import *
init()

SW, SH = 640, 480
FPS = 120
PLAYER_IMG = 'paddle.png'

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

class Player(Character):
    def update_p1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= SH - self.height:
            self.rect.y += self.speed

    def update_p2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= SH - self.height:
            self.rect.y += self.speed

player_1 = Player('paddle.png', 0, 100, 40, 100, 5)
player_2 = Player('paddle2.png', SW -40, 100, 40, 100, 5)

clock = time.Clock()
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    screen.fill((100, 40, 150))
    player_1.reset()
    player_1.update_p1()
    player_2.reset()
    player_2.update_p2()

    display.update()
    clock.tick(FPS)

quit()
