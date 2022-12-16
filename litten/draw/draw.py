import os
import sys

sys.path.append(os.path.realpath(''))
from litten.layers import *

import PIL.Image as Image
from PIL import ImageDraw, ImageFont

no_of_layers = 15
h = 320
w = (4 * no_of_layers) * 20

image = Image.new("RGB", (w, h), color = '#ffffff')

layer1 = InputLayer("Input", 0)
layer1.draw(image)

layer2 = Layer("Input", layer1.end)
layer2.draw(image)

layer3 = DenseLayer("Dense", layer2.end, 100)
layer3.draw(image)

layer4 = CNNLayer("Dense", layer3.end, 1024, (500, 500, 3))
layer4.draw(image)

layer5 = CNNLayer("Dense", layer4.end, 64, (250, 250, 3))
layer5.draw(image)


layer6 = PoolingLayer("Dense", layer5.end, 64, (75, 75, 3))
layer6.draw(image)

layer7 = ActivationLayer("Dense", layer6.end,)
layer7.draw(image)

layer8 = EmbeddingLayer("Dense", layer7.end,)
layer8.draw(image)

layer9 = RecurrentLayer("Dense", layer8.end, bi=True)
layer9.draw(image)

layer10 = RecurrentLayer("Dense", layer9.end, bi=False)
layer10.draw(image)

image.show()

"""
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import matplotlib.pyplot as plt

image = Image.new("RGB", (80, 360), color = '#ffffff')
draw = ImageDraw.Draw(image)

draw.rectangle((20, 180, 60, 140), fill = '#98c1d9', outline='#000000')
draw.ellipse  ((25, 145, 55, 175), fill = '#ffffff', outline='#000000')

image.show()
"""