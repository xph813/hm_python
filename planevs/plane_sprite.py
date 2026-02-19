import random
import pygame
# official > third party > self


# define a constant for screen
SCREEN_RECT = pygame.Rect(0, 0, 480, 600)
# define fresh rate
FPS = 60

# define a timer for creating enemy planes
# why create a constant?
# because the name is easy to remember
# and there might be other event
CREATE_ENEMY_EVENT = pygame.USEREVENT

# hero fire event
# pygame.USEREVENT has been used
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """game sprite"""

    def __init__(self, image_name, speed=1):

        # 1. call parent's init
        super().__init__()

        # 2. define attributes
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # move vertically
        self.rect.y += self.speed

class Background(GameSprite):
    """background sprite"""
    def __init__(self, is_alt=False):

        # 1. call parent's method to create sprite(image/rect/speed)
        super().__init__("./images/background.png")

        # 2. determine if it's located above
        if is_alt:
            self.rect.y = -self.rect.height


    def update(self):

        # 1. call parent's method
        super().update()

        # 2. if it's out, set it up
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Enemy(GameSprite):
    """enemy sprite"""

    def __init__(self):

        # 1. call parent's method, and specify image
        super().__init__("./images/enemy1.png")

        # 2. specify speed
        self.speed = random.randint(1, 3)

        # 3. specify random positon
        self.rect.bottom = 0 # vertical

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


    def update(self):

        # 1. call parent's method, to fly vertically
        super().update()

        # 2. if it's going out of the screen, kill
        if self.rect.y >= SCREEN_RECT.height:

            # print("delete")

            # .kill will remove sprite from all sprites group.
            # which means it call __del__ .
            self.kill()


    def __del__(self):
        # print("enemy gone %s" % self.rect)
        pass


class Hero(GameSprite):
    """hero sprite"""

    def __init__(self):

        # 1. call parent method
        super().__init__("./images/me1.png", 0)

        # 2. set original position
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3. create bullets sprite group
        self.bullets = pygame.sprite.Group()


    def update(self):

        # hero moves horizontally
        self.rect.x += self.speed

        # determine it's out or not
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("fire...")

        # fire 3 bullets once a time
        for i in (1, 2, 3):

            # 1. create bullet sprite
            bullet = Bullet()

            # 2. set original position
            bullet.rect.bottom = self.rect.y - i * 20 # axis y
            bullet.rect.centerx = self.rect.centerx

            # 3. add bullet to the bullet sprite group
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """bullet sprite"""
    def __init__(self):
        # call parent's method
        # set pic and speed
        super().__init__("./images/bullet1.png", -2)

    def update(self):

        # call parent's method, and let it fly vertically
        super().update()

        # determine it's out or not
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("bullet destroyed")



