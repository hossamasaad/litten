from litten import utils

class TestUtils:

    def test_layers(self):
        assert ("Activation" in utils.activations) == True
        assert ("Activation" in utils.activations) == True
        assert ("ELU"        in utils.activations) == True

        assert ("SeparableConv1D"  in utils.convs) == True
        assert ("Conv2D"           in utils.convs) == True
        assert ("DepthwiseConv2D"  in utils.convs) == True
        
        assert ("MaxPooling1D"           in utils.pools) == True
        assert ("GlobalAveragePooling3D" in utils.pools) == True
        assert ("AveragePooling2D"       in utils.pools) == True

        assert ("Dropout" in utils.dropouts) == True
        assert ("BatchNormalization" in utils.normalizations) == True

    def test_get_width(self, model):
        assert utils.get_width(model.layers)      == 1400
        assert utils.get_width(model.layers[ :1]) == 300
        assert utils.get_width(model.layers[1:2]) == 300
        assert utils.get_width(model.layers[5:6]) == 200
        assert utils.get_width(model.layers[6:7]) == 260
        assert utils.get_width(model.layers[7:8]) == 200

    def test_get_layer_name(self, model):
        assert utils.get_layer_name(model.layers[0]) == "Conv2D"
        assert utils.get_layer_name(model.layers[1]) == "MaxPooling2D"
        assert utils.get_layer_name(model.layers[5]) == "Dropout"
        assert utils.get_layer_name(model.layers[6]) == "Flatten"
        assert utils.get_layer_name(model.layers[7]) == "Dense"

    def test_get_activation_name(self, model):
        assert utils.get_activation_name(model.layers[0]) == "relu"
        assert utils.get_activation_name(model.layers[7]) == "relu"
        assert utils.get_activation_name(model.layers[8]) == "linear"