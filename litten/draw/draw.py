import os
import sys

sys.path.append(os.path.realpath(''))

from litten.layers import *
from palettes import *
from PIL import ImageDraw, ImageFont
import PIL.Image as Image


no_of_layers = 20
h = 320
w = (4 * no_of_layers) * 20
palette = Default

image = Image.new("RGB", (w, h), color = '#ffffff')


c = Connector()

layer1 = InputLayer("Input", 0, palette)
layer1.draw(image)

layer2 = Layer("Input", layer1.end, palette)
layer2.draw(image)

c.connect(image, layer1, layer2)

layer3 = DenseLayer("Dense", layer2.end, palette, 100)
layer3.draw(image)

c.connect(image, layer2, layer3)

layer4 = ConvLayer("Dense", layer3.end, palette, 1024, (500, 500, 3))
layer4.draw(image)
c.connect(image, layer3, layer4)

layer5 = ConvLayer("Dense", layer4.end, palette, 64, (250, 250, 3))
layer5.draw(image)
c.connect(image, layer4, layer5)

layer6 = PoolingLayer("Dense", layer5.end, palette, 64, (75, 75, 3))
layer6.draw(image)
c.connect(image, layer5, layer6)

layer7 = EmbeddingLayer("Dense", layer6.end, palette)
layer7.draw(image)
c.connect(image, layer6, layer7)

layer8 = ActivationLayer("Dense", layer7.end, palette)
layer8.draw(image)
c.connect(image, layer7, layer8)

layer9 = RecurrentLayer("Dense", layer8.end, palette, bi=True)
layer9.draw(image)
c.connect(image, layer8, layer9)

layer10 = RecurrentLayer("Dense", layer9.end, palette, bi=False)
layer10.draw(image)
c.connect(image, layer9, layer10)

layer11 = ConvLSTM("Dense", layer10.end, palette, 300, (256, 256, 3))
layer11.draw(image)
c.connect(image, layer10, layer11)

layer12 = FlattenLayer("Dense", layer11.end, palette)
layer12.draw(image)
c.connect(image, layer11, layer12)

layer13 = DenseLayer("Dense", layer12.end, palette, 100)
layer13.draw(image)
c.connect(image, layer12, layer13)

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