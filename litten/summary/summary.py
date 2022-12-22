import os
import sys
sys.path.append(os.path.realpath(''))
from litten import utils 

class LayersSummary:
    def __init__(self) -> None:
        pass

    def show_layers_summaries(self, model):
        for i, layer in enumerate(model.layers):
            print("=================================================================================================================")
            x = "Layer {}: {}".format(i+1, utils.get_layer_name(layer))
            x = x + " " * (24 - len(x)) + "| Attributes"
            print(x)
            print("----------------------------------------")
            attributes = vars(layer)

            for key, value in attributes.items():
                s = key + " " * (23 - len(key))
                if key[0] != "_" and key != "kernel" and key != "bias":
                    print(s, ": ", value)