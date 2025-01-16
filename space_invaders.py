import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')  # Make sure to have an icon image
pygame.display.set_icon(icon)

# Player
player_char = "A"
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemy_char = "V"
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bullet_char = "|"
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Load and resize images
player_img = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img, (32, 32))  # Resize player image

enemy_img = pygame.image.load('enemy.png')
enemy_img = pygame.transform.scale(enemy_img, (32, 32))  # Resize enemy image

bullet_img = pygame.image.load('bullet.png')
bullet_img = pygame.transform.scale(bullet_img, (8, 16))  # Resize bullet image

# Button
button_font = pygame.font.Font('freesansbold.ttf', 32)
button_text = button_font.render('Play Again', True, (255, 255, 255))
button_rect = button_text.get_rect(center=(400, 300))

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance < 27

def show_play_button():
    screen.blit(button_text, button_rect)

def reset_game():
    global playerX, playerY, playerX_change, bulletX, bulletY, bullet_state, score_value, enemyX, enemyY
    playerX = 370
    playerY = 480
    playerX_change = 0
    bulletX = 0
    bulletY = 480
    bullet_state = "ready"
    score_value = 0
    for i in range(num_of_enemies):
        enemyX[i] = random.randint(0, 735)
        enemyY[i] = random.randint(50, 150)

# Game Loop
running = True
game_over = False
while running:
    # Clear the screen
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.5  # Slowed down by 50%
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.5  # Slowed down by 50%
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if button_rect.collidepoint(event.pos):
                game_over = False
                reset_game()

    if not game_over:
        # Player Movement
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy Movement
        for i in range(num_of_enemies):
            # Game Over
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                game_over = True
                break

            enemyX[i] += enemyX_change[i] * 0.5  # Slowed down by 50%
            if enemyX[i] <= 0:
                enemyX_change[i] = 2  # Slowed down by 50%
                enemyY[i] += enemyY_change[i] * 0.5  # Slowed down by 50%
            elif enemyX[i] >= 736:
                enemyX_change[i] = -2  # Slowed down by 50%
                enemyY[i] += enemyY_change[i] * 0.5  # Slowed down by 50%

            # Collision
            collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change * 0.5  # Slowed down by 50%
            if bulletY <= 0:
                bulletY = 480
                bullet_state = "ready"

        player(playerX, playerY)
        show_score(textX, textY)
    else:
        show_play_button()

    pygame.display.update() 