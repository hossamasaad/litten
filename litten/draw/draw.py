import os
import sys

sys.path.append(os.path.realpath(''))
from litten.layers import *

import PIL.Image as Image
from PIL import ImageDraw, ImageFont

no_of_layers = 8
h = 320
w = (4 * no_of_layers) * 20

image = Image.new("RGB", (w, h), color = '#ffffff')

layer1 = InputLayer("Input", "(5,6)", 1)
layer2 = Layer("XD Layer",  2)
layer3 = DenseLayer("Dense", 3, 60)
layer4 = CNNLayer("CNN", 4)
layer5 = PoolingLayer("Pooling", 5)
layer6 = NormaliztionLayer("BatchNormalization", 6)
layer7 = ActivationLayer("BatchNormalization", 7)



layer1.draw(image, show_properties=True)
layer2.draw(image, show_properties=True)
layer3.draw(image, show_properties=False)
layer4.draw(image)
layer5.draw(image)
layer6.draw(image)
layer7.draw(image)

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