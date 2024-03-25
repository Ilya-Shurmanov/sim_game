from typing import Tuple
import pygame
import random


class Line:
    def __init__(self,
                 line_qty: int,
                 start: Tuple[int, int] = (370, 370),
                 end: Tuple[int, int] = (400, 400),
                 color: Tuple[int, int, int] = (255, 0, 0),
                 thickness: int = 2
                 ) -> None:
        """Initialize a line.

        Args:
            start (Tuple[int, int]): The starting point of the line.
            end (Tuple[int, int]): The ending point of the line.
            color (Tuple[int, int, int]): The color of the line.
            thickness (int): The thickness of the line.
            name (str): The name of the line.
        """
        self.start = start
        self.end = end
        self.color = color
        self.thickness = thickness
        self.name = "line " + str(line_qty)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.Font(None, 12)
        self.rect = pygame.Rect(0, 0, 0, 0)

    def draw(self, surface):
        pygame.draw.line(surface,
                         self.color,
                         self.start,
                         self.end,
                         self.thickness)
        text_surface = self.font.render(self.name, True, self.text_color)
        surface.blit(text_surface, (self.start[0] + 20, self.start[1] + 20))

    def rand_move(self, x, y):
        delta_x = random.randint(-x, x)
        delta_y = random.randint(-y, y)
        if random.randint(0, 1) == 0:
            self.start = (self.start[0] + delta_x, self.start[1] + delta_y)
        else:
            self.end = (self.end[0] + delta_x, self.end[1] + delta_y)


class Circle():
    def __init__(self,
                 circle_center: Tuple[int, int],
                 circle_color: Tuple[int, int, int],
                 circle_radius: int,
                 border_width: int) -> None:
        """Initialize a circle.

        Args:
            circle_color (Tuple[int, int, int]): The color of the circle.
            circle_center (Tuple[int, int]): The center of the circle.
            circle_radius (int): The radius of the circle.
        """
        self.circle_color = circle_color
        self.circle_center = circle_center
        self.circle_radius = circle_radius
        self.border_width = border_width

    def draw(self, surface):
        pygame.draw.circle(surface,
                           self.circle_color,
                           self.circle_center,
                           self.circle_radius,
                           self.border_width)


