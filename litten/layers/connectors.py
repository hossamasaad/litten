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
            draw.line([p1, p2], fill="#000000", width=1)

        return image
    
    def output(self, image, layer1):
        _from = layer1.get_from()
        draw = ImageDraw.Draw(image)

        points1 = [(_from[0][0]     , _from[0][1] + 35),
                   (_from[0][0] + 20, _from[0][1] + 35),
                   (_from[0][0] + 15, _from[0][1] + 30),
                   (_from[0][0] + 20, _from[0][1] + 35),
                   (_from[0][0] + 15, _from[0][1] + 40)]
        
        points2 = [(_from[1][0]     , _from[1][1] - 35),
                   (_from[1][0] + 20, _from[1][1] - 35),
                   (_from[1][0] + 15, _from[1][1] - 30),
                   (_from[1][0] + 20, _from[1][1] - 35),
                   (_from[1][0] + 15, _from[1][1] - 40)]
        draw.line(points1, fill="#000000", width=2)
        draw.line(points2, fill="#000000", width=2)