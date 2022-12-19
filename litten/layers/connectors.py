import math
from PIL import ImageDraw

class Connector:
    def __init__(self) -> None:
        pass

    def connect(self, image, layer1, layer2):
        _from = layer1.get_from()
        _to   = layer2.get_to()

        draw = ImageDraw.Draw(image)
        # [(x, y), (x, y)]
        for p1, p2 in zip(_from, _to):
            draw.line([p1, p2], fill="#000000")

        return image