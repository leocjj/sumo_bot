import pygame
import sumobot_utils

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sumo bots")

# Load the car images
robot_1 = pygame.image.load("./images/robot_blue_t.png")
robot_2 = pygame.image.load("./images/robot_red_t.png")

# Set up the cars' initial positions
car1_x = 50
car1_y = 50
car2_x = 700
car2_y = 50

# Set up the ground
ground_width = 600
ground_height = 400
ground_x = (WIDTH - ground_width) // 2
ground_y = (HEIGHT - ground_height) // 2

# Set up the clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_UP:
                car1_y -= 10
            elif event.key == pygame.K_DOWN:
                car1_y += 10
            elif event.key == pygame.K_LEFT:
                car1_x -= 10
            elif event.key == pygame.K_RIGHT:
                car1_x += 10
            elif event.key == pygame.K_w:
                car2_y -= 10
            elif event.key == pygame.K_s:
                car2_y += 10
            elif event.key == pygame.K_a:
                car2_x -= 10
            elif event.key == pygame.K_d:
                car2_x += 10

    # Draw the ground
    pygame.draw.rect(screen, (0, 255, 0), (ground_x, ground_y, ground_width, ground_height))

    # Draw the cars
    screen.blit(robot_1, (car1_x, car1_y))
    screen.blit(robot_2, (car2_x, car2_y))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)
