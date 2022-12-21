import os
import sys

sys.path.append(os.path.realpath(''))

from litten.draw import utils
import PIL.Image as Image

from litten.draw import palettes
from litten.layers import *


class Drawer:
    def __init__(self, model, background_color = "#FFFFFF", palette = 'default', show_connectors=False, show_names=False, show_proporties=False) -> None:
        self.model            = model
        self.background_color = background_color
        self.show_names       = show_names
        self.show_proporties  = show_proporties
        self.show_connectors  = show_connectors
        self.width     = utils.get_width(model.layers)
        self.height    = 320
        self.palette   = utils.palettes[palette]
        self.image     = Image.new("RGB", (self.width, self.height), color=self.background_color)
        self.connector = Connector()

    def draw(self):
        
        layers = self.model.layers
        last_layer = None

        # Draw input layer
        shape = None
        layer_name = utils.get_layer_name(layer=layers[0])

        if layer_name == "Input": 
            shape = layers[0].shape
            del layers[0]
        else:
            shape = layers[0].input_shape

        last_layer = InputLayer(name="Input", shape=shape, start_x=20, palette=self.palette)
        last_layer.draw(image=self.image, show_name=self.show_names, show_properties=self.show_proporties)
        curr_layer = None

        for layer in layers:
            
            layer_name = utils.get_layer_name(layer=layer)

            if layer_name == "Flatten":
                curr_layer = FlattenLayer(name=layer_name, input_shape=layer.input_shape, output_shape=layer.output_shape, start_x=last_layer.end, palette=self.palette)
            
            elif layer_name == "Dense":
                activation = utils.get_activation_name(layer=layer)
                curr_layer = DenseLayer(name=layer_name, units=layer.units, activation=activation, input_shape=layer.input_shape, output_shape=layer.output_shape, start_x=last_layer.end, palette=self.palette)
            
            elif layer_name == "Embedding":
                curr_layer = EmbeddingLayer(name=layer_name, input_dim=layer.input_dim, output_dim=layer.output_dim, input_shape=layer.input_shape, output_shape=layer.output_shape, start_x=last_layer.end, palette=self.palette)

            elif layer_name in utils.activations:
                activation = None
                if layer_name == "Activation":
                    activation = utils.get_activation_name(layer=layer)
                curr_layer = ActivationLayer(name=layer_name, activation=activation, start_x=last_layer.end, palette=self.palette)

            elif layer_name in utils.convs:
                activation = utils.get_activation_name(layer=layer)
                curr_layer = ConvLayer(name=layer_name, filters=layer.filters, kernel=layer.kernel_size, activation=activation, input_shape=layer.input_shape, output_shape=layer.output_shape, start_x=last_layer.end, palette=self.palette)

            elif layer_name in utils.pools:
                curr_layer = PoolingLayer(name=layer_name, pool_size=layer.pool_size, padding=layer.padding, input_shape=layer.input_shape, output_shape=layer.output_shape, start_x=last_layer.end, palette=self.palette)

            elif layer_name in utils.rnns:
                bi = False
                if layer_name == 'Bidirectional':
                    bi = True
                    layer = layer.layer
                    layer_name = "Bi(" + utils.get_layer_name(layer) + ")"

                activation = utils.get_activation_name(layer=layer)
                curr_layer = RecurrentLayer(name=layer_name, units=layer.units, activation=activation, bi=bi, start_x=last_layer.end, palette=self.palette)

            elif layer_name in utils.convlstms:
                activation = utils.get_activation_name(layer=layer)
                curr_layer = ConvLayer(name=layer_name, filters=layer.filters, kernel=layer.kernel_size, activation=activation, input_shape=layer.input_shape, output_shape=layer.output_shape, start_x=last_layer.end, palette=self.palette)

            else:
                curr_layer = Layer(layer_name, start_x=last_layer.end, palette=self.palette)

            curr_layer.draw(image=self.image, show_name=self.show_names, show_properties=self.show_proporties)

            if self.show_connectors:
                self.connector.connect(image=self.image, layer1=last_layer, layer2=curr_layer)

            last_layer = curr_layer
        
        if self.show_connectors:
            self.connector.output(image=self.image, layer1=last_layer)

        self.image.resize((last_layer.end + 20, 320))
        self.image.show()