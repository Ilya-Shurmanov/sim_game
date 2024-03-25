class Game_object():
    def __init__(self):
        self._coordinates = (0, 0)

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates
