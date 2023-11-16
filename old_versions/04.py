import pygame
from pygame.locals import *  # Optional; used for brevity.

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1024, 762))
clock = pygame.time.Clock()
FPS = 60
SPEED = 1000
W = screen.get_width()
H = screen.get_height()
ROBOT_OFFSET = 50
running = True
dt = 0

player1_pos = pygame.Vector2(W * 1 / 4 - ROBOT_OFFSET, H / 2 - ROBOT_OFFSET)
player2_pos = pygame.Vector2(W * 3 / 4 - ROBOT_OFFSET, H / 2 - ROBOT_OFFSET)
# https://new.express.adobe.com/tools/remove-background
# fill the screen with a color to wipe away anything from last frame
background = pygame.image.load("images/background_gray_blocks.jpg").convert()
robot_1 = pygame.image.load("images/robot_red_t.png").convert_alpha()
robot_2 = pygame.image.load("images/robot_blue_t.png").convert_alpha()
r2 = robot_2.copy()
r2_rot = 0

while running:
    # poll for events, pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(robot_1, player1_pos)
    screen.blit(r2, player2_pos)
    #pygame.draw.circle(screen, "red", player1_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        r2_rot -= dt*100
        print(r2_rot)
        r_2 = pygame.transform.rotate(robot_2, r2_rot)
    if keys[pygame.K_s]:
        player1_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player1_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player1_pos.x += 300 * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player2_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player2_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player2_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(FPS) / SPEED
    #dt = clock.tick_busy_loop(60) / 1000

pygame.quit()