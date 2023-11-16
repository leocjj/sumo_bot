from os.path import join as path_join
from time import sleep
import pygame
from pygame.locals import *  # Optional; used for brevity.
from math import cos, sin, radians
import sumo_utils as su
import robot_code_1 

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((su.WIDTH, su.HEIGHT))
pygame.display.set_caption("Sumo bots")
clock = pygame.time.Clock()
dt = 0

# https://new.express.adobe.com/tools/remove-background
# fill the screen with a color to wipe away anything from last frame
background = pygame.image.load(path_join('images', "grass-background-1024x768.jpg")).convert()
dojo = pygame.image.load(path_join('images', "background_gray_blocks.jpg")).convert_alpha()
explosion1 = pygame.image.load(path_join('images', "explosion1_t.png")).convert_alpha()
explosion2 = pygame.image.load(path_join('images', "explosion2_t.png")).convert_alpha()
explosion3 = pygame.image.load(path_join('images', "explosion3_t.png")).convert_alpha()

def display_everything():
    screen.blit(background, (0, 0))
    screen.blit(dojo, (su.DOJO_X, su.DOJO_Y), (0, 0, su.DOJO_WIDTH, su.DOJO_HIGHT))
    screen.blit(r1.image, (r1.corner[0], r1.corner[1]))
    screen.blit(r2.image, (r2.corner[0], r2.corner[1]))
    #screen.blits([(explosion1, (0, 0)), (explosion2, (0, 0)), (explosion3, (0, 0))] )
    pygame.draw.circle(screen, "red", (su.WIDTH * 3 / 4,  su.HEIGHT / 2), 10)
    pygame.draw.circle(screen, "blue", (700,500), 10)

def display_explosion(bot):
    bot.rotate(1)
    # bot.zoom_in()
    w = r1.image.get_rect().width
    if i % 3 == 0:
        screen.blit(explosion1, (bot.corner[0], bot.corner[1]), (0, 0, w, w))
    elif i % 3 == 1:
        screen.blit(explosion2, (bot.corner[0], bot.corner[1]), (0, 0, w, w))
    else:
        screen.blit(explosion3, (bot.corner[0], bot.corner[1]), (0, 0, w, w))
    pygame.display.flip()
    dt = clock.tick(su.FPS) / su.GENERAL_SPEED
    sleep(0.1)


class bot():
    def __init__(self, img_file, x, y, rot):
        # Load the image with alpha transparency.
        self.image0 = pygame.image.load(path_join('images', img_file)).convert_alpha()
        #self.image0.set_colorkey(su.BLACK)
        # Create a copy of the image to be rotated.
        self.image = self.image0.copy()
        # Save initial parameters.
        self.init_x = x
        self.init_y = y
        self.init_rot = rot
        # Center of the bot, to be used for collision detection.
        self.x = x
        self.y = y
        self.center = (self.x, self.y)
        # Initial rotation.
        self.rot = rot
        self.rotate(self.rot - su.BOT_ANGULAR_SPEED)
        # Top-left corner of the bot, to be used for display image.
        self.corner = (self.x - su.BOT_OFFSET, self.y - su.BOT_OFFSET)

    def move(self, forward):
        if forward > 0:
            self.x += (su.BOT_LINEAR_SPEED * dt * cos(radians(self.rot)))
            self.y -= (su.BOT_LINEAR_SPEED * dt * sin(radians(self.rot)))
        elif forward < 0:
            self.x -= (su.BOT_LINEAR_SPEED * dt * cos(radians(self.rot)))
            self.y += (su.BOT_LINEAR_SPEED * dt * sin(radians(self.rot)))
        else:
            return
        self.center = (self.x, self.y)
        self.corner = (self.x - su.BOT_OFFSET, self.y - su.BOT_OFFSET)

    def rotate(self, rot):
        if rot > 0:
            self.rot = (self.rot + su.BOT_ANGULAR_SPEED) % 360
        elif rot < 0:
            self.rot = (self.rot - su.BOT_ANGULAR_SPEED) % 360
        else:
            return
        # Save the old center of the image.
        old_center = self.image.get_rect().center
        # Rotate the original image without modifying it.
        self.image = pygame.transform.rotate(self.image0, self.rot)
        # Update the center of the image because rotation changes the size of the image.
        self.x -= self.image.get_rect().center[0] - old_center[0]
        self.y -= self.image.get_rect().center[1] - old_center[1]
        self.center = (self.x, self.y)
        # Top-left corner of the bot, to be used for display image.
        self.corner = (self.x - su.BOT_OFFSET, self.y - su.BOT_OFFSET)

    def zoom_in(self):
        zoom = self.image.get_height() * su.BOT_IMPLOSION_FACTOR
        self.image = pygame.transform.scale(self.image, (zoom, zoom))
        self.center = (self.center[0] + su.BOT_OFFSET, self.center[1] + su.BOT_OFFSET)
        #self.rotate(self.rot)
 
    def impact(self, opponent):
        return su.calculate_impact(self.rot, self.center, opponent.center)
    
    def move_back(self, impact_factor, angle):
        if impact_factor:
            self.x += (impact_factor * su.BOT_LINEAR_SPEED * dt * cos(radians(angle)))
            self.y -= (impact_factor * su.BOT_LINEAR_SPEED * dt * sin(radians(angle)))
            self.center = (self.x, self.y)
            self.corner = (self.x - su.BOT_OFFSET, self.y - su.BOT_OFFSET)
    
    def reset(self):
        # Create a copy of the image to be rotated.
        self.image = self.image0.copy()
        # Center of the bot, to be used for collision detection.
        self.x = self.init_x
        self.y = self.init_y
        self.center = (self.x, self.y)
        # Initial rotation.
        self.rot = self.init_rot
        self.rotate(self.rot - su.BOT_ANGULAR_SPEED)
        # Top-left corner of the bot, to be used for display image.
        self.corner = (self.x - su.BOT_OFFSET, self.y - su.BOT_OFFSET)


r1 = bot("robot_red_t.png", su.WIDTH * 1 / 4, su.HEIGHT / 2, 0)
r2 = bot("robot_blue_t.png", su.WIDTH * 3 / 4, su.HEIGHT / 2, 180)

running = True
while running:
    # poll for events, pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw everything
    display_everything()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        r1.move(1)
    if keys[pygame.K_s]:
        r1.move(-1)
    if keys[pygame.K_a]:
        r1.rotate(1)
    if keys[pygame.K_d]:
        r1.rotate(-1)
    if keys[pygame.K_s]:
        r2.rotate(0)        
    if keys[pygame.K_UP]:
        r2.move(1)
    if keys[pygame.K_DOWN]:
        r2.move(-1)
    if keys[pygame.K_LEFT]:
        r2.rotate(1)
    if keys[pygame.K_RIGHT]:
        r2.rotate(-1)
    if keys[pygame.K_z]:
        r2.zoom_in()
    if keys[pygame.K_ESCAPE]:
        r1.reset()
        r2.reset()

    try:
        r1_move, r1_rotate = robot_code_1.code(r1.x, r1.y, r1.rot, r2.x, r2.y, r2.rot)
        if isinstance(r1_move, int) and r1_move in (-1, 0, 1) and isinstance(r1_rotate, int) and r1_rotate in (-1, 0, 1) :
            r1.move(r1_move)
            r1.rotate(r1_rotate)
    except:
        pass

    if su.collition(r1.center, r2.center):
        impact_factor_r1_on_r2 = r1.impact(r2)
        impact_factor_r2_on_r1 = r2.impact(r1)
        angle_r1_r2 = su.calculate_angle(r1.center, r2.center)
        angle_r2_r1 = su.calculate_angle(r2.center, r1.center)
        r2.move_back(impact_factor_r1_on_r2, angle_r1_r2)
        r1.move_back(impact_factor_r2_on_r1, angle_r2_r1)

    if r1.center[0] < su.DOJO_X or r1.center[0] > su.DOJO_X + su.DOJO_WIDTH or \
        r1.center[1] < su.DOJO_Y or r1.center[1] > su.DOJO_Y + su.DOJO_HIGHT:
            for i in range(50):
                display_everything()
                display_explosion(r1)
            r1.reset()
            r2.reset()

    if r2.center[0] < su.DOJO_X or r2.center[0] > su.DOJO_X + su.DOJO_WIDTH or \
        r2.center[1] < su.DOJO_Y or r2.center[1] > su.DOJO_Y + su.DOJO_HIGHT:
            for i in range(50):
                display_everything()
                display_explosion(r2)
            r1.reset()
            r2.reset()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(su.FPS) / su.GENERAL_SPEED
    #dt = clock.tick_busy_loop(60) / 1000

pygame.quit()