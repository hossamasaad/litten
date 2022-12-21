import abc

class ColorPallete(metaclass=abc.ABCMeta):

    @abc.abstractproperty
    def main_color():
        pass

    @abc.abstractproperty
    def secondry():
        pass

    @abc.abstractproperty
    def reg():
        pass
    
    @abc.abstractproperty
    def drop():
        pass

class Default(ColorPallete):
    main_color = "#c0cacc"
    secondry   = "#a6b1b3"
    reg        = "#7ba1a6"
    drop       = "#7ba1a6"

class Blues(ColorPallete):
    main_color = "#4F7C91"
    secondry   = "#6F9AAB"
    reg        = "#2E6583"
    drop       = "#4F7C91"

class Grays(ColorPallete):
    main_color = "#9ea3a3"
    secondry   = "#909696"
    reg        = "#828989"
    drop       = "#747c7c"

class Reds(ColorPallete):
    main_color = "#ca1414"
    secondry   = "#e9a8a1"
    reg        = "#f4d4d3"
    drop       = "#6b0003"

class Greens(ColorPallete):
    main_color = "#5c715e"
    secondry   = "#87a08b"
    reg        = "#d2d6a8"
    drop       = "#3a5335"