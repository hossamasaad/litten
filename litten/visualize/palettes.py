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
    main_color = "#adb5bd"
    secondry   = "#ced4da"
    reg        = "#dee2e6"
    drop       = "#495057"

class Browns(ColorPallete):
    main_color = "#ddb892"
    secondry   = "#b08968"
    reg        = "#e6ccb2"
    drop       = "#7f5539"

class Blues(ColorPallete):
    main_color = "#1965a0"
    secondry   = "#2476b1"
    reg        = "#4893c6"
    drop       = "#003a70"

class Grays(ColorPallete):
    main_color = "#495057"
    secondry   = "#adb5bd"
    reg        = "#dee2e6"
    drop       = "#212529"

class Reds(ColorPallete):
    main_color = "#cd0000"  
    secondry   = "#ef2b2b"
    reg        = "#e56b6b"
    drop       = "#aa0000"

class Greens(ColorPallete):
    main_color = "#97a97c"
    secondry   = "#87a08b"
    reg        = "#d2d6a8"
    drop       = "#3a5335"

class Yellows(ColorPallete):
    main_color = "#ffcf33"
    secondry   = "#ffd95c"
    reg        = "#ffe285"
    drop       = "#ffc60a"

class Purples(ColorPallete):
    main_color = "#3e2248"
    secondry   = "#5b3f64"
    reg        = "#775c7f"
    drop       = "#22052d"