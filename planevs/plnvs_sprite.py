import random
import pygame

FPS = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):

        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):

        super().__init__('./images/background.png', speed=1)

        if is_alt:
            self.rect.bottom = 0
    
    def update(self):

        super().update()

        if self.rect.y > SCREEN_RECT.height:
            self.rect.bottom = 0


class Enemy(GameSprite):

    def __init__(self):

        super().__init__('./images/enemy1.png')

        # 1. 设置随机速度
        self.speed = random.randint(1, 3)

        # 2. 设置随机位置
        max_x = SCREEN_RECT.width - self.rect.width

        self.rect.x = random.randint(0, max_x)
        self.rect.bottom = 0

    
    def update(self):

        super().update()

        if self.rect.y > SCREEN_RECT.height:

            self.kill()

    def __del__(self):

        # print(f'delete at {self.rect}')
        pass

class Hero(GameSprite):

    def __init__(self):

        super().__init__('./images/me1.png', speed=0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - 120

        self.bullets = pygame.sprite.Group()

    def update(self):
        
        self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        
        for i in [1, 2, 3]:

            bullet = Bullet()

            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - 20 * i

            self.bullets.add(bullet)


class Bullet(GameSprite):

    def __init__(self):

        super().__init__('./images/bullet1.png', speed=-2)
    
    def update(self):

        super().update()

        if self.rect.bottom < 0:
            self.kill()