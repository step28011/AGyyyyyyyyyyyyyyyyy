from pygame import *
from random import randint
win_width = 700
win_height = 500
score = 0

xD = 100
Y = 100


font.init()
font2 =  font.Font(None, 50)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

back = transform.scale(image.load("pppppppppppppp.jpg"), (win_width, win_height))
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))


game = True
finish = False
clock = time.Clock()
FPS = 60

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
    def set_size(self, player_image,player_x, player_y, x, y):
        self.image = transform.scale(image.load(player_image), (player_x, player_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
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

poketka = Player('pixil-frame-03.png', 50, 250, 100, 100, 5)
poketka1 = Player('pixil-frame-04.png', 600, 250, 100, 100, 5)
ball = GameSprite('pixil-frame-0.png', 350, 250, 50, 50, 5 )
lose1 = GameSprite('pixil-frame-02.png', 350, 250, 200, 200, 0 )
lose2 = GameSprite('pixil-frame-01.png', 350, 250, 200, 200, 0 )
m_x = -4
m_y = 2
while game:
    if score > 15 and score < 30:
        if m_x >=0 :
            m_x+=0.005
        else:
            m_x-=0.01
    if score > 30 and score < 45:
        if m_x >=0 :
            m_x+=0.01
        else:
            m_x-=0.01
    if score > 45 and score < 60:
        if m_x >=0 :
            m_x+=0.01
        else:
            m_x-=0.01
    if score > 60 and score < 75:
        if m_x >=0 :
            m_x+=0.01
        else:
            m_x-=0.01
    if score > 75 and score < 90:
        if m_x >=0 :
            m_x+=0.01
        else:
            m_x-=0.01
    if score > 90 and score < 105:
        if m_x >=0 :
            m_x+=0.01
        else:
            m_x-=0.01
    if score > 105 and score < 120:
        if m_x >=0 :
            m_x+=0.01
        else:
            m_x-=0.01
    if score > 120 and score < 135:
        if m_x >=0 :
            m_x+=0.01
        else:
            m_x-=0.01
    if score > 135 and score < 150:
        if m_x >=0 :
            m_x+=0.01
        else:
            m_x-=0.01
    if score > 150 and score < 555:
        if m_x >=0 :
            m_x+=0.01
        else:
            m_x-=0.01        
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(back,(0, 0))
        text = font2.render('Счёт:' + str(score), 1,(0, 255, 0))
        window.blit(text, (10, 20))    
        poketka.update()
        poketka1.update_r()
        ball.rect.x += m_x
        ball.rect.y += m_y
        
        ball.reset()
        
        poketka.reset()
        poketka1.reset()
        display.update()
        if sprite.collide_rect(ball,poketka) or sprite.collide_rect(ball,poketka1):
            score+=1
            m_x*=-1
            ball.rect.x += m_x*5
        if ball.rect.y <= 5 or ball.rect.y >= 450:
            m_y *= -1
        
    if ball.rect.x <= 0:
        lose1.reset()
        finish =True
    if ball.rect.x >= 700:
        lose2.reset()
        finish = True  
    display.update()
   
    clock.tick(FPS)