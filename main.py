# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame
import random

pygame.init()

# personalization
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PurpleMoon Beta")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background1.png")

# player
playerImg = pygame.image.load("player.png")
playerX = 380
playerY = 500
playerX_update = 0

# enemy
enemyImg = pygame.image.load("butterfly.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(10, 150)
enemyX_update = 0.2
enemyY_update = 20

# enemy 2
enemyA = random.randint(0, 736)
enemyB = random.randint(10, 150)
enemyA_update = 0.2
enemyB_update = 20


# Game code
def player(x, y):
    screen.blit(playerImg, (x, y))  # means draw player


def enemy(x, y):
    screen.blit(enemyImg, (x, y))  # means draw enemy


# Game loop
running = True

# Press the green button in the gutter to run the script.
while running:
    screen.fill((119, 77, 142))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed seeing if its <- or ->
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_update = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_update = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_update = 0

    # limit player icon to the window size
    playerX += playerX_update
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # limit the enemy icon to window size
    enemyX += enemyX_update
    if enemyX <= 0:
        enemyX_update = 0.2
        enemyY += enemyY_update
    elif enemyX >= 736:
        enemyX_update = -0.2
        enemyY += enemyY_update

# second enemy movement control
    enemyA += enemyA_update
    if enemyA <= 0:
        enemyA_update = 0.2
        enemyB += enemyB_update
    elif enemyA >= 736:
        enemyA_update = -0.2
        enemyB += enemyB_update

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    enemy(enemyA, enemyB)
    pygame.display.update()
