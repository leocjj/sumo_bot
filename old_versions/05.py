import pygame
from pygame.locals import *  # Optional; used for brevity.
from dataclasses import dataclass
import sumo_utils as su

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((su.WIDTH, su.HEIGHT))
pygame.display.set_caption("Sumo bots")
clock = pygame.time.Clock()
dt = 0

# https://new.express.adobe.com/tools/remove-background
# fill the screen with a color to wipe away anything from last frame
background = pygame.image.load("images/grass-background-1024x768.jpg").convert()
dojo = pygame.image.load("images/background_gray_blocks.jpg").convert_alpha()
robot_img_1 = pygame.image.load("images/robot_red_t.png").convert_alpha()
robot_img_2 = pygame.image.load("images/robot_blue_t.png").convert_alpha()
r1 = robot_img_1.copy()
r2 = robot_img_2.copy()

@dataclass
class coord():
    x: int
    y: int
    rot: int

r1_coord = coord(su.WIDTH * 1 / 4 - su.BOT_OFFSET, su.HEIGHT / 2 - su.BOT_OFFSET, 0)
r2_coord = coord(su.WIDTH * 3 / 4 - su.BOT_OFFSET, su.HEIGHT / 2 - su.BOT_OFFSET, 0)

running = True
while running:
    # poll for events, pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(dojo, (su.DOJO_X, su.DOJO_Y), (0, 0, su.DOJO_WIDTH, su.DOJO_HIGHT))
    screen.blit(r1, (r1_coord.x, r1_coord.y))
    screen.blit(r2, (r2_coord.x, r2_coord.y))
    #pygame.draw.circle(screen, "red", player1_pos, 40)

    r1_coord.rot = (r1_coord.rot + su.BOT_ANGULAR_SPEED) % 360
    r1 = pygame.transform.rotate(robot_img_1, r1_coord.rot)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        r2_coord.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        r2_coord.y += 300 * dt
    if keys[pygame.K_LEFT]:
        r2_coord.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        r2_coord.x += 300 * dt
    if keys[pygame.K_w]:
        rect = r2.get_rect()
        old_center = rect.center
        r2_coord.rot = (r2_coord.rot + su.BOT_ANGULAR_SPEED) % 360
        r2 = pygame.transform.rotate(robot_img_2, r2_coord.rot)
        r2_coord.x -= r2.get_rect().center[0] - old_center[0]
        r2_coord.y -= r2.get_rect().center[1] - old_center[1]

    # flip() the display to put your work on screen
    pygame.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(su.FPS) / su.GENERAL_SPEED
    #dt = clock.tick_busy_loop(60) / 1000

pygame.quit()