from pygame import *
from random import randint
win_width = 700
win_height = 500
lost = 0
score = 0

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

back =(200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60



class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
    def update(self):
        keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed





class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_height - 80)
            self.rect.y = 0
            self.speed = randint(1, 2)
            lost = lost + 1



poketka = ('pixil-frame-0.png', 50, 250, 10, 50, 5)
poketka1 = ('pixil-frame-0.png', 650, 250, 10, 50, 5)
ball = ('pixil-frame-0(1).png', 350, 250, 10, 10, 5 )
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0, 0))
        poketka.update()
        poketka1.update()
        ball.update()

        poketka.reset()
        poketka1.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)