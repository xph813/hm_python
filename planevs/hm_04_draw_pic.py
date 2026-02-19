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
pygame.display.update()

# game infinite loop
while True:

    pass


pygame.quit()