import os
import sys
sys.path.append(os.path.realpath(''))

import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
from tensorflow.keras.models import Model

from litten import utils
from litten.visualize import palettes
from litten.layers import *
from IPython.display import display


class ModelVisualizer:
    def __init__(self, model, background_color = "#FFFFFF", palette = 'default', show_connectors=False, show_names=False, show_proporties=False) -> None:
        self.model            = model
        self.background_color = background_color
        self.show_names       = show_names
        self.show_proporties  = show_proporties
        self.show_connectors  = show_connectors
        self.width     = utils.get_width(model.layers) * 10
        self.height    = 3200
        self.palette   = utils.palettes[palette]
        self.image     = Image.new("RGB", (self.width, self.height), color=self.background_color)
        self.connector = Connector()

    def visualize_model(self):
        
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

        scale = 1
        display(self.image.resize(( int(self.image.width * scale), int(self.image.height * scale))))


    def visualize_featuremap(self, input_image, cmap = "gray"):

        image = np.expand_dims(input_image, axis=0)
        
        fig = plt.figure()
        fig.suptitle("{}".format("Input Image") , fontsize=18)
        plt.imshow(input_image)

        for layer in self.model.layers:  

            if 'conv' not in layer.name:
                continue    
            
            
            intermediate_model = Model(inputs=self.model.inputs , outputs=layer.output)
            features = intermediate_model.predict(image)

            fig = plt.figure(figsize=(20, 20))
            fig.suptitle("{}".format(layer.name) , fontsize=18)

            for i in range(1, features.shape[3]+1):
                plt.subplot(8,8,i)
                plt.imshow(features[0,:,:,i-1] , cmap=cmap)

            plt.show()
    
    def visualize_filters(self, cmap = "gray"):
    
        for layer in self.model.layers:  

            if 'conv' not in layer.name:
                continue    
            
            filters, _ = layer.get_weights()

            fig = plt.figure(figsize=(10,10))
            fig.suptitle("{}".format(layer.name) , fontsize=18)

            idx=1
            no_filters = 6

            for i in range(no_filters):
                filter = filters[:,:,:,i]
                ch = min(filter.shape[2], 3)
                for j in range(ch):
                    plt.subplot(no_filters, ch, idx)
                    plt.imshow(filter[:,:,j], cmap=cmap)
                    idx += 1
            plt.show()
