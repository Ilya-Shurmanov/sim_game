from draw_objects import Rectangle
from mobs import Mob
from typing import Tuple
import pygame


class Main_building(Rectangle):
    def __init__(self,
                 coord: Tuple[int, int, int, int],
                 color: Tuple[int, int, int],
                 border_width: int = 0
                 ) -> None:
        """Initialize a rectangle.

        Args:
            color (Tuple[int, int, int]): The color of the rectangle.
            coordinates (Tuple[int, int, int, int]): The coordinates of the
                rectangle. x, y, width, height
        """
        super().__init__(coord, color, border_width)
        self.units_list = []
        self.color = color

    def draw(self, surface) -> None:
        pygame.draw.rect(surface,
                         self.color,
                         self.coord,
                         self.border_width)
        self.draw_units(surface)

    def spawn_unit(self) -> None:
        _unit = Mob(self.coordinates, self.color, 2, 0)
        self.units_list.append(_unit)

    def spawn_units(self, amount: int) -> None:
        for _ in range(amount):
            self.spawn_unit()

    def draw_units(self, surface) -> None:
        for unit in self.units_list:
            unit.draw(surface)
