import pygame
from random import randint

windowHeight = 500
windowWidth = 1000

pygame.init()

son_jump = pygame.mixer.Sound("jump.wav")
music_theme = pygame.mixer.Sound("green_hill_zone.wav")
music_theme.play()

win = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("First Game")


x = -150      
y =  170
width = 50
height = 60
vel = 5
running = True
jumping = False
jumpValue = 30
jumpIntensity = 5
jumpCount = -30

walkRight = False
walkLeft = False
standing = True
sitting = False
sprinting = False
walkingAnimSpeed = 5
altWalk = -walkingAnimSpeed

win.blit(pygame.image.load('background_2.png'), (0, 0))

while running:

    if altWalk >=5:
        altWalk = -walkingAnimSpeed

    if sprinting:
        pygame.time.delay(1)
    else:
        pygame.time.delay(10)


    a = x
    b = y


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
        if not sitting:
            sitting = True
            y += 60

        walkLeft = False
        walkRight = False

    else:
        if sitting:
            y -= 60
        sitting = False

    if keys[pygame.K_LEFT] and not sitting:

        x -= vel
        walkLeft = True
        walkRight = False
        standing = False

    if keys[pygame.K_RIGHT] and not sitting:

        x += vel
        walkRight = True
        walkLeft = False
        standing = False

    if keys[pygame.K_UP]:
        if not jumping:
            jumping = True
            jumpCount = -jumpValue
            son_jump.play()

    if jumping and jumpCount<0:
        y -= jumpIntensity
        jumpCount += 1

    if jumping and jumpCount >= 0 and jumpCount < jumpValue:
        y += jumpIntensity
        jumpCount +=1

    if jumpCount >= jumpValue:
        jumping = False
        jumpCount = jumpValue

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        standing = True
        walkLeft = False
        walkRight = False

    if keys[pygame.K_l]:
        sprinting = True
    else:
        sprinting = False


    win.blit(pygame.image.load('background_2.jpg'), (0, 0))
   # win.fill((0, 0, 0))
   # pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))



    if walkRight and (not jumping and not sprinting):
        if altWalk < 0:
            win.blit(pygame.image.load('SONIKright.png'), (x, y))
        else:
            win.blit(pygame.image.load('SONIKstanding.png'), (x, y))
        altWalk += 1

    if walkLeft and (not jumping and not sprinting):
        if altWalk < 0:
            win.blit(pygame.image.load('SONIKleft.png'), (x, y))
        else:
            win.blit(pygame.image.load('SONIKstandingLeft.png'), (x, y))

        altWalk += 1

    if standing and (not jumping and not sitting):
        win.blit(pygame.image.load('SONIKstanding.png'), (x, y))

    if jumping and not sprinting:
        win.blit(pygame.image.load('SONIKjumping.png'), (x, y))

    if sprinting and walkRight:
        win.blit(pygame.image.load('SONIKsprint.png'), (x, y))

    elif sprinting and walkLeft:
        win.blit(pygame.image.load('SONIKsprint2.png'), (x, y))

    if sitting and not jumping and not walkRight and not walkLeft:
        win.blit(pygame.image.load('SONIKsitting.png'), (x, y))

 #   pygame.draw.rect(win, (0, 255, 0), (0, 450, 1000, 50))

    pygame.display.update()

    if x != a or y != b:
        print((x,y))