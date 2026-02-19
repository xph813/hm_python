import pygame

pygame.init()

# create a window
# .set_mode returns a screen object
screen = pygame.display.set_mode((480, 700))

# draw bkg pic
# 1> load
bg = pygame.image.load("./images/background.png")
# 2> blit to draw
screen.blit(bg, (0, 0))
# 3> update
# pygame.display.update()

# draw hero's plane
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
# pygame.display.update()

# create a clock object
clock = pygame.time.Clock()

# 1. define rect to record plane's position
hero_rect = pygame.Rect(150, 300, 102, 126)

# game infinite loop

while True:

    # specify frequency inside the loop
    clock.tick(60)

    # capture event
    # we need to put it in the loop
    event_list = pygame.event.get()
    if len(event_list) > 0:
            print(event_list)

    # 2. modify plane's position
    hero_rect.y -= 1

    # determine position
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3. blit
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4. update
    pygame.display.update()
    pass

pygame.quit()