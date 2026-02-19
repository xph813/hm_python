import pygame

from plane_sprite import *

class PlaneGame(object):
    """plane fight main game"""

    def __init__(self):

        print("initializing...")

        # 1. create a screen
        # SCREEN_RECT is a rectangle, but we need a tuple
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2. create a clock
        self.clock = pygame.time.Clock()

        # 3. call private method, to create sprite and its group
        self.__create_sprites()

        # 4. set timer for enemy planes
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

        # 5. set timer for fire
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)



    def __create_sprites(self):

        # create bgs and sprite group
        # bg1 = Background("./images/background.png")
        # bg2 = Background("./images/background.png")
        # bg2.rect.y = -bg2.rect.height

        # initialization should be encapsulated within the class
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # only create enemy group, because we create them in __event_handler
        self.enemy_group = pygame.sprite.Group()

        # create hero and its group
        # we need hero to detect collision,
        # so we need to set it as attribute
        # and we also need it to shoot
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)



    def start_game(self):

        print("start game!")

        while True:
            # 1. set fresh rate
            self.clock.tick(FPS)

            # 2. event listener
            self.__event_handler()

            # 3. collision detector
            self.__check_collide()

            # 4. update sprite group
            self.__update_sprites()

            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # official > third party > self

                # static method: class.method
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("enemy plane appears...")

                # 1. create enemy sprite
                enemy = Enemy()

                # 2. add it into enemy group
                self.enemy_group.add(enemy)

            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # if using event listener, we need to constantly press.
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("move right")

        # use key module: pygame.key.get_pressed()
        # not event module
        # we can press the button for a long time, and it can get all the press
        keys_pressed = pygame.key.get_pressed() # return a tuple
        # get the index of key pressed
        if keys_pressed[pygame.K_RIGHT]:
            # print("moving right")
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):

        # 1. bullet destroys enemy
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2. enemy destroys hero
        # pygame.sprite.spritecollide() return a list
        # 1> invincible version:
        # pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 2> if list is not empty, delete hero
        enemies= pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies):

            # 1.del hero
            self.hero.kill()

            # 2. end game
            PlaneGame.__game_over()


    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("game over...")
        pygame.quit()
        exit()



if __name__ == '__main__':

    # create game object
    game = PlaneGame()

    # start game
    game.start_game()



