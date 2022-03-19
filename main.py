# This is a beginner pygame tutorial that I tried to recreate my way.

# the original code is made by "freecodecamp.org"
# it might not be as optimized, but it's still a beginner project.


import pygame
import math
import random

pygame.init()

# personalization
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PurpleMoon Beta")
icon = pygame.image.load("moon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background1.png")

# player
playerImg = pygame.image.load("player.png")
playerX = 380
playerY = 500
playerX_update = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_update = []
enemyY_update = []
numEnemies = 10

for i in range(numEnemies):
    enemyImg.append(pygame.image.load("butterfly.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(10, 300))
    enemyX_update.append(0.5)
    enemyY_update.append(30)

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 500
bulletX_update = 0
bulletY_update = 3
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('coolvetica.otf', 36)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (189, 176, 208))
    screen.blit(score, (x, y))

# Game code
def player(x, y):
    screen.blit(playerImg, (x, y))  # means draw player


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))  # means draw enemy


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                fire_bullet(bulletX, bulletY)
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
    for i in range(numEnemies):
        enemyX[i] += enemyX_update[i]
        if enemyX[i] <= 0:
            enemyX_update[i] = 0.2
            enemyY[i] += enemyY_update[i]
        elif enemyX[i] >= 736:
            enemyX_update[i] = -0.2
            enemyY[i] += enemyY_update[i]

        # Collision firing
        coll = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if coll:
            bulletY = 500
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(10, 300)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    # bullet firing
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_update

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
