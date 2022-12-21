import os
import sys
sys.path.append(os.path.realpath(''))
from litten.draw import get_layer_name 

class LayersSummary:
    def __init__(self, model) -> None:
        self.model = model

    def show_layers_summaries(self):
        for i, layer in enumerate(self.model.layers):
            print("=================================================================================================================")
            x = "Layer {}: {}".format(i+1, get_layer_name(layer))
            x = x + " " * (24 - len(x)) + "| Attributes"
            print(x)
            print("----------------------------------------")
            attributes = vars(layer)

            for key, value in attributes.items():
                s = key + " " * (23 - len(key))
                if key[0] != "_" and key != "kernel" and key != "bias":
                    print(s, ": ", value)