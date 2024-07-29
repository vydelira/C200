import pygame, sys

pygame.init()

screen = pygame.display.set_mode((400, 400))

while (1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#draws a rectangle on screen with color (r, g, b) at loc (x, y) of width w, height h.
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(10, 10, 30, 20)) #blue
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(40, 30, 30, 20)) #red 
    pygame.display.flip()
