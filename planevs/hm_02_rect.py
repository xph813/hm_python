import pygame

# 矩形对象
hero_rect = pygame.Rect(100, 500, 120, 125)

print("hero's origin %d %d" % (hero_rect.x, hero_rect.y))
print("hero's size %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)

