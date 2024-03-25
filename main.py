import pygame
import sys
from control_object import Target_cross as Target
from buildings import Main_building

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
fps = 60
# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")
timer = 0
target = Target(200, 200)
# Game loop
main_buiding = Main_building((100, 100, 50, 50), (255, 0, 0))
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse click coordinates
            if event.button == 1:
                click_x, click_y = pygame.mouse.get_pos()
                target.teleport(click_x, click_y)
                target.active = True
            elif event.button == 3:
                target.active = False

    # Update player position

    screen.fill((255, 255, 255))
    main_buiding.draw(screen)
    for unit in main_buiding.units_list:
        unit.move_towards_object(target, 4)
    target.draw(screen)
    if timer % 50 == 0:
        main_buiding.spawn_unit()
    # Update the display
    pygame.display.flip()
    timer += 1
