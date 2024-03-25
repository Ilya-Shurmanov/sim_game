from typing import Tuple
import math
import random

from draw_objects import Circle


class Mob(Circle):
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
        super().__init__(circle_center,
                         circle_color,
                         circle_radius,
                         border_width)

    def move(self, x, y):
        circle_center_x, circle_center_y = self.circle_center
        self.circle_center = (circle_center_x + x,
                              circle_center_y + y)

    def teleport(self, x, y):
        self.circle_center = (x, y)

    def random_move(self):
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)
        self.move(x, y)

    def move_towards_object(self, obj, step):
        if obj.coordinates:
            object_x, object_y = self.coordinates
            target_x, target_y = obj.coordinates
            # print(object_x, object_y, target_x, target_y)
            direction = math.atan2(target_y - object_y, target_x - object_x)
            new_x = object_x + step * math.cos(direction)
            new_y = object_y + step * math.sin(direction)
            # print(new_x, new_y)
            self.circle_center = (int(new_x), int(new_y))

    def move_towards_coords(self, coord_x, coord_y, step):
        object_x, object_y = self.coordinates

        # print(object_x, object_y, target_x, target_y)
        direction = math.atan2(coord_y - object_y, coord_x - object_x)
        new_x = object_x + step * math.cos(direction)
        new_y = object_y + step * math.sin(direction)
        # print(new_x, new_y)
        self.circle_center = (int(new_x), int(new_y))
