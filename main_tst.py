import pygame
import sys
from mobs import Mob
from draw_objects import Rectangle
# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
fps = 30
# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")


# Game loop

mob = Mob(circle_center=(200, 200),
          circle_color=(255, 0, 0),
          circle_radius=2,
          border_width=0)
mob_enemy = Mob(circle_center=(100, 100),
                circle_color=(0, 255, 0),
                circle_radius=5,
                border_width=0)

target = Mob(circle_center=(200, 400),
             circle_color=(0, 0, 255),
             circle_radius=5,
             border_width=0)
building = Rectangle((50, 50, 20, 50), (255, 0, 0), 0)
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse click coordinates
            click_x, click_y = pygame.mouse.get_pos()
            target.teleport(click_x, click_y)

    # Update player position
    screen.fill((255, 255, 255))
    mob.draw(screen)
    # print("mob", mob.coordinates)
    mob_enemy.draw(screen)
    building.draw(screen)
    # print("enemy", mob_enemy.coordinates)
    mob_enemy.move_towards_object(target, 7)
    mob.move_towards_object(mob_enemy, 5)
    # print("mob after step ", mob.coordinates)
    # Update the display
    pygame.display.flip()
