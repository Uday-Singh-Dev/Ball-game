import pygame
import random

# global variables
score = 0
dash = False
dash_start = 0  # Timestamp when dash started
dash_cooldown = 500  # Cooldown in milliseconds (1 second)
dash_duration = 100   # Dash lasts 200 ms

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Objects*****************************************************************************************
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game")

player = pygame.Rect((300, 250, 50, 50))
player_pos = [float(player.x), float(player.y)]  # Track position with floats

coin_radius = 25
coin_center = (random.randint(coin_radius, SCREEN_WIDTH - coin_radius),
               random.randint(coin_radius, SCREEN_HEIGHT - coin_radius))

font = pygame.font.Font(None, 36)

# FUNCTIONS****************************************************************************************

def movement(speed):
    global dash, dash_start
    keys = pygame.key.get_pressed()
    shift = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

    now = pygame.time.get_ticks()

    # Start dash if shift is pressed, not already dashing, and cooldown passed
    if shift and not dash and (now - dash_start > dash_cooldown):
        dash = True
        dash_start = now

    # End dash after dash_duration
    if dash and (now - dash_start > dash_duration):
        dash = False

    # Get movement keys
    left = keys[pygame.K_a]
    right = keys[pygame.K_d]
    up = keys[pygame.K_w]
    down = keys[pygame.K_s]

    # Normalize speed when moving diagonally
    if (left or right) and (up or down):
        norm_speed = speed / (2 ** 0.5)
    else:
        norm_speed = speed

    # Apply dash multiplier if dashing
    current_speed = norm_speed * 5 if dash else norm_speed

    # Move player
    if left:
        player_pos[0] -= current_speed
    if right:
        player_pos[0] += current_speed
    if up:
        player_pos[1] -= current_speed
    if down:
        player_pos[1] += current_speed

    # Update player rect with new position
    player.x = int(player_pos[0])
    player.y = int(player_pos[1])

def collision():
    global score, coin_center
    coin_x, coin_y = coin_center
    # Define hitbox of the coin
    hitbox_left = coin_x - coin_radius
    hitbox_right = coin_x + coin_radius
    hitbox_up = coin_y - coin_radius
    hitbox_down = coin_y + coin_radius

    # Check if player rectangle overlaps this hitbox
    if (player.right > hitbox_left and
        player.left < hitbox_right and
        player.bottom > hitbox_up and
        player.top < hitbox_down):
        # Teleports coin to new location
        coin_center = (random.randint(coin_radius, SCREEN_WIDTH - coin_radius),
                       random.randint(coin_radius, SCREEN_HEIGHT - coin_radius))
        score += 1

def score_update():
    score_label = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_label, (10, 10))

def boundary():
    # Keep player inside screen boundaries
    if player_pos[0] <= 0:
        player_pos[0] = 0
        player.x = 0
    if player_pos[1] <= 0:
        player_pos[1] = 0
        player.y = 0
    if player_pos[0] >= SCREEN_WIDTH - player.width:
        player_pos[0] = SCREEN_WIDTH - player.width
        player.x = SCREEN_WIDTH - player.width
    if player_pos[1] >= SCREEN_HEIGHT - player.height:
        player_pos[1] = SCREEN_HEIGHT - player.height
        player.y = SCREEN_HEIGHT - player.height

# MAINLOOP*****************************************************************************************

run = True
while run:
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 0), coin_center, coin_radius)
    pygame.draw.rect(screen, (255, 20, 100), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    movement(0.3)
    boundary()
    collision()
    score_update()
    pygame.display.update()

pygame.quit()
