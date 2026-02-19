import pygame
from plnvs_sprite import *


class PlaneGame:

    def __init__(self):
        
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

        self.bg1 = Background()
        self.bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(self.bg1, self.bg2)

        self.enemy_group = pygame.sprite.Group()
        
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    
    # 创建精灵
    def __create_sprites(self):
        pass

    # 事件监听
    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:

                self.hero.fire()
        
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif key_list[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    # 更新精灵组
    def __update_sprites(self):

        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 碰撞检测
    def __check_collide(self):

        # 子弹与敌机相撞
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 英雄与敌机相撞
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies):

            self.hero.kill()

            self.__game_over()

    # 结束游戏
    @staticmethod
    def __game_over():

        pygame.quit()

        quit()
    
    def start_game(self):

        print('game starts.')
        while True:

            self.clock.tick(FPS)

            # 1. 事件监听
            self.__event_handler()

            # 2. 碰撞检测
            self.__check_collide()

            # 3. 更新精灵组
            self.__update_sprites()
            
            pygame.display.update()


if __name__ == '__main__':
    
    game = PlaneGame()

    game.start_game()