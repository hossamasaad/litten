from keras.layers import Layer
from litten.layers import *
from litten.visualize.palettes import *


palettes = {
    "default":Default,
    "red"    :Reds,
    "blue"   :Blues,
    "gray"   :Grays,
    "green"  :Greens
}

activations = ["Activation", "Softmax", "ELU", "ReLU", "PReLU", "LeakyReLU", "ThresholdedReLU"]
convs       = ["Conv1D", "Conv2D", "Conv3D", "SeparableConv1D", "SeparableConv2D", "SeparableConv3D", "DepthwiseConv2D", "Conv1DTranspose", "Conv2DTranspose", "Conv3DTranspose" ]
pools       = ["MaxPooling1D", "MaxPooling2D", "MaxPooling3D", "AveragePooling1D", "AveragePooling2D", "AveragePooling3D", "GlobalMaxPooling1D", "GlobalMaxPooling2D", "GlobalMaxPooling3D", "GlobalAveragePooling1D", "GlobalAveragePooling2D", "GlobalAveragePooling3D"]
rnns        = ["LSTM", "GRU", "RNN", "SimpleRNN", "Bidirectional"]
convlstms   = ["ConvLSTM1D layer", "ConvLSTM2D layer", "ConvLSTM3D layer"]

def get_width(layers):
    width = 0
    layer_name = get_layer_name(layer=layers[0])
    if layer_name == "Input": 
        del layers[0]

    width += 60

    for layer in layers:        
        layer_name = get_layer_name(layer=layer)
        if layer_name in activations:
            width += 70
        elif layer_name in convs or layer_name in pools or layer_name in convlstms:
            width += 180
        elif layer_name in rnns or layer_name == 'Flatten':
            width += 140
        else:
            width += 80
    return width + 60   

def get_layer_name(layer):
    try:
        return layer.__class__.__name__
    except:
        return "unknown"

def get_activation_name(layer):
    try:
        return layer.activation.__name__
    except:
        return "unknown"