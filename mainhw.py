import pygame
import time
pygame.init()

screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("Sprite Animation")
clock = pygame.time.Clock()

image1 = pygame.image.load("image1.png")
image2 = pygame.image.load("image2.png")

image1 = pygame.transform.scale(image1, (150,150))
image2 = pygame.transform.scale(image2, (150,150))

x = 300
y = 200
speed = 5
frame = 0
walk_index = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_LEFT]:
        x -= speed
        moving = True
    if keys[pygame.K_RIGHT]:
        x += speed
        moving = True
    if keys[pygame.K_UP]:
        y -= speed
        moving = True
    if keys[pygame.K_DOWN]:
        y += speed
        moving = True

    if moving:
        frame += 1
        if frame > 10:
            walk_index += 1
            frame = 0
            if walk_index > 1:
                walk_index = 0

        if walk_index == 0:
            player = image1
        else:
            player = image2
    else:
        player = image1
        frame = 0
        walk_index = 0

    screen.fill((200,220,255))
    screen.blit(player, (x,y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()