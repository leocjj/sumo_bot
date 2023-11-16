from os.path import join as path_join
from time import sleep
import pygame
from pygame.locals import *  # Optional; used for brevity.
from math import cos, sin, radians
import sumo_utils as su
import player1
import player2

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((su.WIDTH, su.HEIGHT))
pygame.display.set_caption("Sumo bots")
clock = pygame.time.Clock()
dt = 0
DEBUG_MODE = 0

# https://new.express.adobe.com/tools/remove-background
# fill the screen with a color to wipe away anything from last frame
background = pygame.image.load(path_join('images', "background.jpg")).convert()
dojo = pygame.image.load(path_join('images', "background_dojo.jpg")).convert_alpha()
explosion1 = pygame.image.load(path_join('images', "explosion1.png")).convert_alpha()
explosion2 = pygame.image.load(path_join('images', "explosion2.png")).convert_alpha()
explosion3 = pygame.image.load(path_join('images', "explosion3.png")).convert_alpha()


def display_everything():
    player1_score = font.render(str(r1.score), True, su.RGB_GREEN, su.RGB_BLACK)
    player1_score_rect = player1_score.get_rect() 
    player1_score_rect.center = (su.WIDTH * 1 // 4 , (su.HEIGHT - su.DOJO_HIGHT) // 4)
    player2_score = font.render(str(r2.score), True, su.RGB_GREEN, su.RGB_BLACK)
    player2_score_rect = player1_score.get_rect() 
    player2_score_rect.center = (su.WIDTH * 3 // 4 , (su.HEIGHT - su.DOJO_HIGHT) // 4)
    screen.blit(background, (0, 0))
    screen.blit(dojo, (su.DOJO_X, su.DOJO_Y), (0, 0, su.DOJO_WIDTH, su.DOJO_HIGHT))
    screen.blit(r1.image, (r1.corner[0], r1.corner[1]))
    screen.blit(r2.image, (r2.corner[0], r2.corner[1]))
    screen.blit(title, title_rect)
    screen.blit(player1_score, player1_score_rect)
    screen.blit(player2_score, player2_score_rect)

def display_explosion(bot):
    bot.rotate(1)
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
        self.score = 0

    def move(self, forward):
        """ This function is called to move the bot forward or backward. """
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
        """ This function is called to rotate the bot CW or CCW. """
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

    def impact(self, opponent):
        return su.calculate_impact(self.rot, self.center, opponent.center)
    
    def move_back(self, impact_factor, angle):
        """ This function is called when the bot collides with the other bot. """
        if impact_factor:
            self.x += (impact_factor * su.BOT_LINEAR_SPEED * dt * cos(radians(angle)))
            self.y -= (impact_factor * su.BOT_LINEAR_SPEED * dt * sin(radians(angle)))
            self.center = (self.x, self.y)
            self.corner = (self.x - su.BOT_OFFSET, self.y - su.BOT_OFFSET)
    
    def reset(self):
        """ This function is called when a bot falls out of the dojo. """
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


# Select the color for each bot. If the same color is selected, player 2 will use the secundary color.
if player1.PRIMARY_COLOR == player2.PRIMARY_COLOR:
    player2_color = player2.SECUNDARY_COLOR
else:
    player2_color = player2.PRIMARY_COLOR

# create a font object.
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object for the main title.
title = font.render('Sumo bots', True, su.RGB_GREEN, su.RGB_BLACK)
# create a rectangular object for the text surface object
title_rect = title.get_rect() 
# Set the center of the rectangular object.
title_rect.center = (su.WIDTH // 2, (su.HEIGHT - su.DOJO_HIGHT) // 4)

# Create the bots.
r1 = bot(player1.PRIMARY_COLOR, su.WIDTH * 1 / 4, su.HEIGHT / 2, 0)
r2 = bot(player2_color, su.WIDTH * 3 / 4, su.HEIGHT / 2, 180)

running = True
while running:
    # poll for events, pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw everything
    display_everything()

    keys = pygame.key.get_pressed()
    if DEBUG_MODE in (2, 3, 4):
        # Player 1 (left): w-a-s-d
        if keys[pygame.K_w]:
            r1.move(1)
        if keys[pygame.K_s]:
            r1.move(-1)
        if keys[pygame.K_a]:
            r1.rotate(1)
        if keys[pygame.K_d]:
            r1.rotate(-1)
    if DEBUG_MODE in (1, 3, 4):
        # Player 2 (right): up-down-left-right
        if keys[pygame.K_UP]:
            r2.move(1)
        if keys[pygame.K_DOWN]:
            r2.move(-1)
        if keys[pygame.K_LEFT]:
            r2.rotate(1)
        if keys[pygame.K_RIGHT]:
            r2.rotate(-1)
    if keys[pygame.K_ESCAPE]:
        r1.reset()
        r2.reset()
        r1.score = 0
        r2.score = 0

    if DEBUG_MODE in (0, 1, 3):
        # Player 1 (left) autonomous code
        try:
            r1_move, r1_rotate = player1.move_bot(r1.x, r1.y, r1.rot, r2.x, r2.y, r2.rot)
            if isinstance(r1_move, int) and r1_move in (-1, 0, 1):
                r1.move(r1_move)
            if isinstance(r1_rotate, int) and r1_rotate in (-1, 0, 1) :
                r1.rotate(r1_rotate)
        except:
            pass

    if DEBUG_MODE in (0, 2, 3):
        # Player 2 (right) autonomous code
        try:
            r2_move, r2_rotate = player2.move_bot(r1.x, r1.y, r1.rot, r2.x, r2.y, r2.rot)
            if isinstance(r2_move, int) and r2_move in (-1, 0, 1):
                r2.move(r2_move)
            if isinstance(r2_rotate, int) and r2_rotate in (-1, 0, 1):
                r2.rotate(r2_rotate)
        except:
            pass

    # Check for collision between bots. If there is a collision, move the bots back.
    if su.collition(r1.center, r2.center):
        impact_factor_r1_on_r2 = r1.impact(r2)
        impact_factor_r2_on_r1 = r2.impact(r1)
        angle_r1_r2 = su.calculate_angle(r1.center, r2.center)
        angle_r2_r1 = su.calculate_angle(r2.center, r1.center)
        r2.move_back(impact_factor_r1_on_r2, angle_r1_r2)
        r1.move_back(impact_factor_r2_on_r1, angle_r2_r1)

    # If bot of player 1 falls out of the dojo, explode and reset both bots.
    if r1.center[0] < su.DOJO_X or r1.center[0] > su.DOJO_X + su.DOJO_WIDTH or \
        r1.center[1] < su.DOJO_Y or r1.center[1] > su.DOJO_Y + su.DOJO_HIGHT:
            for i in range(su.EXPLOSION_TIME):
                display_everything()
                display_explosion(r1)
            r1.reset()
            r2.reset()
            r2.score += 1

    # If bot of player 2 falls out of the dojo, explode and reset both bots.
    if r2.center[0] < su.DOJO_X or r2.center[0] > su.DOJO_X + su.DOJO_WIDTH or \
        r2.center[1] < su.DOJO_Y or r2.center[1] > su.DOJO_Y + su.DOJO_HIGHT:
            for i in range(su.EXPLOSION_TIME):
                display_everything()
                display_explosion(r2)
            r1.reset()
            r2.reset()
            r1.score += 1

    # flip() the display to put your work on screen
    pygame.display.flip()

    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(su.FPS) / su.GENERAL_SPEED

pygame.quit()