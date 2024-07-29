import sys, pygame

pygame.init()

size = width, height = 320, 240
black = 0, 0, 0
screen = pygame.display.set_mode(size)

star1 = pygame.image.load("c:\\python\\star1.png")
star1rect = star1.get_rect()
speed = [1, 1]

star2 = pygame.image.load("c:\\python\\star2.png")
star2rect = star2.get_rect()

#explicitly putting star location into second star
star2rect.x = 40
star2rect.y = 200
speed2 = [1, 1]


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.key.get_pressed()[pygame.K_1]:
            print("1 pressed")
        elif pygame.key.get_pressed()[pygame.K_UP]:
            print("Up Arrow Pressed")
            speed = [speed[0] + 1, speed[1] + 1]
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            print("Down Arrow Pressed")
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            print("Left Arrow Pressed")
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            print("Right Arrow Pressed")
        elif pygame.key.get_pressed()[pygame.K_m]:
            print("OMG you pressed the m key")
     

    star1rect = star1rect.move(speed)
    star2rect = star2rect.move(speed2)

    
    #displays (x, y) of star1
    print("({0}, {1})".format(star1rect.x, star1rect.y))


    if star1rect.left < 0 or star1rect.right > width:
        speed[0] = -speed[0]
    if star2rect.left < 0 or star2rect.right > width:
        speed2[0] = -speed2[0]
    if star1rect.top < 0 or star1rect.bottom > height:
        speed[1] = -speed[1]
    if star2rect.top < 0 or star2rect.bottom > height:
        speed2[1] = -speed2[1]

#
# If objects collide make their increments opposite
#
    if star1rect.colliderect(star2rect):
        speed[0] = -speed[0]
        speed[1] = -speed[1]
        speed2[0] = -speed[0]
        speed2[1] = -speed[1]

    pygame.time.delay(80)

    screen.fill(black)

    screen.blit(star1, star1rect)
    screen.blit(star2, star2rect)

#render screen
    pygame.display.flip() 