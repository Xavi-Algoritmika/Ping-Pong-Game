# It's the Ping Pong Game!
# All Algoritmika students must Pong...
# Constructed on 26 Febuary 2025, 7 to 9 PM

from pygame import *
bg_color   = (200,255,255)
win_width  = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(bg_color)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, image_width, image_height):
        super().__init__()
        self.image  = transform.scale(image.load(player_image),(image_width, image_height)) # image size
        self.speed  = player_speed                         # max speed
        self.rect   = self.image.get_rect()                # some pygame movement black magic idk
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):                                      #      Player 2
        keys = key.get_pressed()
        if keys[K_UP]   and self.rect.y >= 5:                #   pad goes up
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y <= win_height - 155: # pad goes down
            self.rect.y +=self.speed

    def update_l(self):                                      #      Player 1
        keys = key.get_pressed()
        if keys[K_w]   and self.rect.y >= 5:                 #   pad goes up
            self.rect.y -=self.speed
        if keys[K_s]   and self.rect.y <= win_height - 155:  # pad goes down
            self.rect.y +=self.speed

game   = True
finish = False
clock  = time.Clock()
FPS    = 60

pad_1  = Player('racket.png', 30, 200, 4, 50, 150)
pad_2  = Player('racket.png', 520, 200, 4, 50, 150)
ball   = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

speed_x= 3
speed_y= 3

font.init()
font  = font.Font(None, 35)
lose1 = font.render('[Player 1 Lose]', True, (180,0,0))
lose2 = font.render('[Player 2 Lose]', True, (180,0,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(bg_color)
        pad_1.update_l()
        pad_2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        pad_1.reset()
        pad_2.reset()
        ball.reset()

        if ball.rect.y <= 0 or ball.rect.y >= win_height - 30:                      # wall collider
            speed_y *= -1

        if ball.rect.colliderect(pad_1.rect) or ball.rect.colliderect(pad_2.rect):  # pad colider
            speed_x *= -1

        #if ball.rect.x <= -25 or ball.rect.x >= win_width - 25:                    # General game stop [unused]
        #    finish = True

        if ball.rect.x <= -25:                                                      # Lose for left player
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x >= win_width - 25:                                           # Lose for left player
            finish = True
            window.blit(lose2, (200,200))

    display.update()
    clock.tick(FPS)