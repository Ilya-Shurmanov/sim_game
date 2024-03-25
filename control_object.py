from draw_objects import Cross


class Target_cross(Cross):
    def __init__(self, x, y, color=(255, 0, 0),  size=10):
        super().__init__(color, x, y, size)
        self.active = False

    def teleport(self, x, y):
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        if self.active:
            return (self.x, self.y)

    def draw(self, screen):
        if self.active:
            super().draw(screen)