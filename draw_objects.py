from typing import Tuple
from main_object import Game_object
import pygame


class Line:
    def __init__(self,
                 start: Tuple[int, int],
                 end: Tuple[int, int],
                 color: Tuple[int, int, int],
                 thickness: int
                 ) -> None:
        """Initialize a line.

        """
        self.start = start
        self.end = end
        self.color = color
        self.thickness = thickness

    def draw(self, surface):
        pygame.draw.line(surface,
                         self.color,
                         self.start,
                         self.end,
                         self.thickness)


class Circle(Game_object):
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

    @property
    def coordinates(self) -> Tuple[int, int]:
        return self.circle_center

    def draw(self, surface) -> None:
        pygame.draw.circle(surface,
                           self.circle_color,
                           self.circle_center,
                           self.circle_radius,
                           self.border_width)


class Rectangle(Game_object):
    def __init__(self,
                 coord: Tuple[int, int, int, int],
                 color: Tuple[int, int, int],
                 border_width: int
                 ) -> None:
        """Initialize a rectangle.

        Args:
            color (Tuple[int, int, int]): The color of the rectangle.
            coordinates (Tuple[int, int, int, int]): The coordinates of the
                rectangle. x, y, width, height
        """
        self.color = color
        self.coord = coord
        self.border_width = border_width

    @property
    def coordinates(self) -> Tuple[int, int]:
        return (self.coord[0] + self.coord[2] // 2,
                self.coord[1] + self.coord[3] // 2)

    def draw(self, surface) -> None:
        pygame.draw.rect(surface,
                         self.color,
                         self.coord,
                         self.border_width)


class Cross:
    def __init__(self, color, x, y, size):
        self.color = color
        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen):
        pygame.draw.line(screen, self.color,
                         (self.x - self.size, self.y - self.size),
                         (self.x + self.size, self.y + self.size), 5)
        pygame.draw.line(screen, self.color,
                         (self.x - self.size, self.y + self.size),
                         (self.x + self.size, self.y - self.size), 5)

    @property
    def coordinates(self):
        return (self.x, self.y)


if __name__ == "__main__":
    import sys
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cross")
    # Game loop
    x = Cross((255, 0, 0), 400, 300, 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update player position

        screen.fill((255, 255, 255))
        x.draw(screen)
        # Update the display
        pygame.display.flip()
