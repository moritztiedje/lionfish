from src.main.constants import HEXAGON_FIELD_WIDTH, HEXAGON_FIELD_HEIGHT, SQUARE_FIELD_WIDTH, SQUARE_FIELD_HEIGHT


class Image:
    def __init__(self, width, height, sprite):
        """
        :type width: int
        :type height: int
        :type sprite: pygame.Surface
        """
        self.width = width
        self.height = height
        self.sprite = sprite


class HexFieldImage(Image):
    def __init__(self, sprite):
        super().__init__(HEXAGON_FIELD_WIDTH, HEXAGON_FIELD_HEIGHT, sprite)


class SquareFieldImage(Image):
    def __init__(self, sprite):
        super().__init__(SQUARE_FIELD_WIDTH, SQUARE_FIELD_HEIGHT, sprite)
