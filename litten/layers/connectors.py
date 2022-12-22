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
            draw.line([p1, p2], fill="#000000", width=5)

        return image
    
    def output(self, image, layer1):
        _from = layer1.get_from()
        draw = ImageDraw.Draw(image)

        points1 = [(_from[0][0]      , _from[0][1] + 350),
                   (_from[0][0] + 200, _from[0][1] + 350),
                   (_from[0][0] + 150, _from[0][1] + 300),
                   (_from[0][0] + 200, _from[0][1] + 350),
                   (_from[0][0] + 150, _from[0][1] + 400)]
        
        points2 = [(_from[1][0]     , _from[1][1] - 350),
                   (_from[1][0] + 200, _from[1][1] - 350),
                   (_from[1][0] + 150, _from[1][1] - 300),
                   (_from[1][0] + 200, _from[1][1] - 350),
                   (_from[1][0] + 150, _from[1][1] - 400)]
        draw.line(points1, fill="#000000", width=5)
        draw.line(points2, fill="#000000", width=5)