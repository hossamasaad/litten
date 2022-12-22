import math
from matplotlib import font_manager
from PIL import ImageDraw, ImageFont 


fonts = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
font = ImageFont.truetype(font=fonts[0], size=100)


class Layer:
    """
    Layer class contain the base structure for any layer
    """
    def __init__(self, name: str, start_x: int, palette) -> None:
        """
        Construct Layer class

        Args:
            name: layer name
            number: layer number
        """
        self.name     = name
        self._start_x = start_x
        self._end_x   = 0
        self.palette  = palette

    def draw(self, image, show_name = False, show_properties=False):
        """
        draw default layer 
        """
        draw = ImageDraw.Draw(image)
        points = [(self._start_x + 2000, 800),
                  (self._start_x + 60, 200)]
        
        draw.rounded_rectangle(xy  = points, radius=3, fill=self.palette.main_color)
        
        draw.ellipse((points[0][0] + 100, points[0][1] + 150, points[0][0] + 300, points[0][1] + 350 ), fill = '#ffffff', outline='#000')
        draw.ellipse((points[0][0] + 100, points[0][1] + 500, points[0][0] + 300, points[0][1] + 700 ), fill = '#ffffff', outline='#000')
        draw.ellipse((points[0][0] + 100, points[0][1] + 850, points[0][0] + 300, points[0][1] + 1050), fill = '#ffffff', outline='#000')

        # update end_x
        self._end_x = self._start_x + 800

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

    @property
    def end(self):
        return self._end_x

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 200, 2100)
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 200, 2100)
        draw.text(points, text=self.name, fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 600, 800), (self._start_x + 600, 2000)]

    def get_to(self):
        return [(self._start_x + 200, 800), (self._start_x + 200, 2000)]


class InputLayer(Layer):
    """
    Input Layer
    """
    def __init__(self, name, shape, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
        self.shape = shape
    
    def draw(self, image, show_name=False, show_properties = False):
        """
        Draw input layer on the image

        Args:
            image: The image will draw the layer on it
        
        Returns:
            image: The image after drawing the layer
        """
        draw = ImageDraw.Draw(image)

        for i in range(10):
            points = [(self._start_x + 200, 400 + i * 200), (self._start_x + 400, 600 + i * 200)] 
            draw.rectangle(points, fill = self.palette.main_color, width = 5, outline= '#000000')

        # update end_x
        self._end_x = self._start_x + 600

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 150, 2500)
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        points = (self._start_x + 150, 2500)        
        draw.text(points, text=self.name, fill="#000000", font=font) 
        
        points = (self._start_x, 2620)
        draw.text(points, text="{}".format(self.shape), fill="#000000", font=font) 

    def get_from(self):
        return [(self._start_x + 400, 400), (self._start_x + 400, 2400)]
        

class DenseLayer(Layer):
    """
    Fully Connected Layer (Dense Layer)
    """
    def __init__(self, name, units, activation, input_shape, output_shape, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
        self.units = units
        self.activation   = activation
        self.input_shape  = input_shape
        self.output_shape = output_shape

    def draw(self, image, show_name = False, show_properties=False):
        """
        Draw a dense layer (FullyConnectedLayer)
        Args:
            image: The image will draw the layer on it
        
        Returns:
            image: The image after drawing the layer
        """
        draw = ImageDraw.Draw(image)
        points = [(self._start_x + 200, 600),
                  (self._start_x + 600, 2200)]
        
        draw.rounded_rectangle(xy  = points, radius=5, fill=self.palette.main_color)
        
        draw.ellipse((points[0][0] + 100, points[0][1] + 150 , points[0][0] + 300, points[0][1] + 350 ), fill = '#ffffff', outline='#000')
        draw.ellipse((points[0][0] + 100, points[0][1] + 500 , points[0][0] + 300, points[0][1] + 700 ), fill = '#ffffff', outline='#000')
        draw.ellipse((points[0][0] + 100, points[0][1] + 1200, points[0][0] + 300, points[0][1] + 1400), fill = '#ffffff', outline='#000')

        draw.line   ([(points[0][0] + 200, points[0][1] + 800 ), (points[0][0] + 200, points[0][1] + 810 )], fill='#000000', width=20)
        draw.line   ([(points[0][0] + 200, points[0][1] + 900 ), (points[0][0] + 200, points[0][1] + 910 )], fill='#000000', width=20)
        draw.line   ([(points[0][0] + 200, points[0][1] + 1000), (points[0][0] + 200, points[0][1] + 1010)], fill='#000000', width=20)
        draw.line   ([(points[0][0] + 200, points[0][1] + 1100), (points[0][0] + 200, points[0][1] + 1110)], fill='#000000', width=20)

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = self._start_x + 800

        return image
    
    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points1 = (self._start_x + 230, 2250)
        draw.text(points1, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)
        points1 = (self._start_x + 230, 2250)
        draw.text(points1, text=self.name, fill="#000000", font=font)
        
        points2 = (self._start_x + 230, 2370)
        draw.text(points2, text="units: {}".format(self.units), fill="#000000", font=font)
        
        points3 = (self._start_x + 230, 2490)
        draw.text(points3, text=self.activation, fill="#000000", font=font)

        points4 = (self._start_x + 230, 2610)
        draw.text(points4, text="input shape\n{}".format(self.input_shape), fill="#000000", font=font)        
        
        points5 = (self._start_x + 230, 2850)
        draw.text(points5, text="output shape\n{}".format(self.output_shape), fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 600, 630 ),
                (self._start_x + 600, 2170)]
    
    def get_to(self):
        return [(self._start_x + 200, 630 ),
                (self._start_x + 200, 2170)]


class ConvLayer(Layer):
    """
    Convluation Layer 
    """
    def __init__(self, name, filters, kernel, activation, input_shape, output_shape, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
        self.filters = filters
        self.kernel  = kernel
        self.activation   = activation
        self.input_shape  = input_shape
        self.output_shape = output_shape
        self._c     = int(min(math.log(filters, 2), 10))
        self._s     = min(int(input_shape[1]/100), 10)
        self.lpoints= [] 

    def draw(self, image, show_name = False, show_properties=False):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 300                 , 1100 - 50 * self._c // 2 - 100 * self._s // 2,
                  self._start_x + 1000 + 100 * self._s, 1700 - 50 * self._c // 2 + 100 * self._s // 2]

        for i in range(self._c):
            if self._c % 2 == 0:
                if i%2:
                    draw.rectangle(points, fill = self.palette.main_color, outline='#000000')
                else:
                    draw.rectangle(points, fill = self.palette.secondry, outline='#000000')
            else:
                if i%2:
                    draw.rectangle(points, fill = self.palette.secondry, outline='#000000')
                else:
                    draw.rectangle(points, fill = self.palette.main_color, outline='#000000')

            points[0], points[1], points[2], points[3] = points[0] + 50, points[1] + 50, points[2] + 50, points[3] + 50
        
        self.lpoints = points

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = points[2] + 200

        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self.lpoints[0], self.lpoints[3]]
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        points = [self.lpoints[0], self.lpoints[3]]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 120]
        draw.text(points, text=self.activation, fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 240]
        draw.text(points, text="filters:{}".format(self.filters), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 360]
        draw.text(points, text="kernel:{}".format(self.kernel), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 480]
        draw.text(points, text="input shape:\n{}".format(self.input_shape), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 720]
        draw.text(points, text="output shape:\n{}".format(self.output_shape), fill="#000000", font=font)

    def get_from(self):
        point_start = [self._start_x + 300                 , 1100 - 50 * self._c // 2 - 100 * self._s // 2,
                       self._start_x + 1000 + 100 * self._s, 1700 - 50 * self._c // 2 + 100 * self._s // 2]
        
        point_end   = [self._start_x + 300                         + 50 * (self._c - 1), 1100 - 50 * self._c // 2 - 100 * self._s // 2 + 50 * (self._c - 1),
                       self._start_x + 1000 + 100 * self._s        + 50 * (self._c - 1), 1700 - 50 * self._c // 2 + 100 * self._s // 2 + 50 * (self._c - 1)]

        return [(point_end[2], point_end[1]),
                (point_end[2], point_end[3]),
                (point_start[2], point_start[1])]
    
    def get_to(self):
        point_start = [self._start_x + 300                 , 1100 - 50 * self._c // 2 - 100 * self._s // 2,
                       self._start_x + 1000 + 100 * self._s, 1700 - 50 * self._c // 2 + 100 * self._s // 2]
        point_end   = [self._start_x + 300                      + 50 * (self._c - 1), 1100 - 50 * self._c // 2 - 100 * self._s // 2 + 50 * (self._c - 1),
                       self._start_x + 1000 + 100 * self._s     + 50 * (self._c - 1), 1700 - 50 * self._c // 2 + 100 * self._s // 2 + 50 * (self._c - 1)]


        return [(point_end[0], point_end[1]),
                (point_end[0], point_end[3]),
                (point_start[0], point_start[1])]


class PoolingLayer(Layer):
    """
    Pooling Layer
    """
    def __init__(self, name, pool_size, padding, input_shape, output_shape, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
        self.units = 64
        self.pool_size = pool_size
        self.padding   = padding
        self.input_shape  = input_shape
        self.output_shape = output_shape
        self._c      = int(min(math.log(self.units, 2), 10))
        self._s      = int(input_shape[1]/100) 
        self.lpoints = []

    def draw(self, image, show_name=False, show_properties=False):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 300                 , 1100 - 50 * self._c // 2 - 100 * self._s // 2,
                  self._start_x + 1000 + 100 * self._s, 1700 - 50 * self._c // 2 + 100 * self._s // 2]

        for i in range(self._c):
            if self._c % 2 == 1:
                if i%2:
                    draw.rectangle(points, fill = self.palette.main_color, outline='#000000')
                else:
                    draw.rectangle(points, fill = self.palette.secondry, outline='#000000')
            else:
                if i%2:
                    draw.rectangle(points, fill = self.palette.secondry, outline='#000000')
                else:
                    draw.rectangle(points, fill = self.palette.main_color, outline='#000000')

            points[0], points[1], points[2], points[3] = points[0] + 50, points[1] + 50, points[2] + 50, points[3] + 50
        
        self.lpoints = points
        
        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = points[2] + 200

        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self.lpoints[0], self.lpoints[3]]
        draw.text(points, text=self.name, fill="#000000", font=font)
    
    def _show_prop(self, image):

        draw = ImageDraw.Draw(image)
        
        points = [self.lpoints[0], self.lpoints[3]]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 120]
        draw.text(points, text="padding: {}".format(self.padding), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 240]
        draw.text(points, text="pool: {}".format(self.pool_size), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 360]
        draw.text(points, text="input shape: \n{}".format(self.input_shape), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 600]
        draw.text(points, text="output shape \n{}".format(self.output_shape), fill="#000000", font=font)

    def get_from(self):
        point_start = [self._start_x + 300                 , 1100 - 50 * self._c // 2 - 100 * self._s // 2,
                       self._start_x + 1000 + 100 * self._s, 1700 - 50 * self._c // 2 + 100 * self._s // 2]
        
        point_end   = [self._start_x + 300                       + 50 * (self._c - 1), 1100 - 50 * self._c // 2 - 100 * self._s // 2 + 50 * (self._c - 1),
                       self._start_x + 1000 + 100 * self._s      + 50 * (self._c - 1), 1700 - 50 * self._c // 2 + 100 * self._s // 2 + 50 * (self._c - 1)]

        return [(point_end[2], point_end[1]),
                (point_end[2], point_end[3]),
                (point_start[2], point_start[1])]
    
    def get_to(self):
        point_start = [self._start_x + 300                 , 1100 - 50 * self._c // 2 - 100 * self._s // 2,
                       self._start_x + 1000 + 100 * self._s, 1700 - 50 * self._c // 2 + 100 * self._s // 2]
        point_end   = [self._start_x + 300                        + 50 * (self._c - 1), 1100 - 50 * self._c // 2 - 100 * self._s // 2 + 50 * (self._c - 1),
                       self._start_x + 1000 + 100 * self._s       + 50 * (self._c - 1), 1700 - 50 * self._c // 2 + 100 * self._s // 2 + 50 * (self._c - 1)]


        return [(point_end[0], point_end[1]),
                (point_end[0], point_end[3]),
                (point_start[0], point_start[1])]


class EmbeddingLayer(Layer):
    """
    Embedding Layer
    """
    def __init__(self, name, input_dim, output_dim, input_shape, output_shape, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
        self.input_dim    = input_dim
        self.output_dim   = output_dim
        self.input_shape  = input_shape
        self.output_shape = output_shape
        self.lpoints      = []

    def draw(self, image, show_name=False, show_properties=False):
        draw = ImageDraw.Draw(image)

        for i in range(7):
            points = [(self._start_x + 200, 700 + i * 200), (self._start_x + 400, 900 + i * 200)] 
            if i % 2:
                draw.rounded_rectangle(points, radius = 2, fill = self.palette.main_color, width = 5, outline= '#000000')
            else:
                draw.rounded_rectangle(points, radius = 2, fill = self.palette.secondry  , width = 5, outline= '#000000')

        for i in range(7):
            points = [(self._start_x + 400, 700 + i * 200), (self._start_x + 600, 900 + i * 200)]
            if i % 2:
                draw.rounded_rectangle(points, radius = 2, fill = self.palette.secondry,   width = 5, outline= '#000000')
            else:
                draw.rounded_rectangle(points, radius = 2, fill = self.palette.main_color, width = 5, outline= '#000000')

        self.lpoints = points

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = self._start_x + 800
        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self.lpoints[0][0] - 2500, self.lpoints[1][1] + 500]
        draw.text(points, text=self.name, fill="#000000", font=font)
    
    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)
        
        points = [self.lpoints[0][0] - 270, self.lpoints[1][1] + 50]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self.lpoints[0][0] - 300, self.lpoints[1][1] + 170]
        draw.text(points, text="input_dim :{}".format(self.input_dim), fill="#000000", font=font)

        points = [self.lpoints[0][0] - 300, self.lpoints[1][1] + 290]
        draw.text(points, text="output_dim:{}".format(self.output_dim), fill="#000000", font=font)

        points = [self.lpoints[0][0] - 300, self.lpoints[1][1] + 410]
        draw.text(points, text="input_shape:\n{}".format(self.input_shape), fill="#000000", font=font)

        points = [self.lpoints[0][0] - 300, self.lpoints[1][1] + 650]
        draw.text(points, text="output_shape:\n{}".format(self.output_shape), fill="#000000", font=font)
 
    def get_from(self):
        return [(self._start_x + 570, 700), (self._start_x + 570, 2100)]
    
    def get_to(self):
        return [(self._start_x + 230, 700), (self._start_x + 230, 2100)]


class RecurrentLayer(Layer):
    """
    Recurrent Layer
    """
    def __init__(self, name, units, activation, bi, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
        self.units = units
        self.activation = activation
        self.bi = bi
        self.lpoints = []

    def draw(self, image, show_name=False, show_properties=False):
        draw = ImageDraw.Draw(image)
        
        points1 = [ self._start_x + 400, 1200, self._start_x + 1200, 1800]
        points2 = [(self._start_x + 400, 1200), (self._start_x + 300, 1100), (self._start_x + 300, 1700), (self._start_x + 400, 1800)]
        points3 = [(self._start_x + 400, 1200), (self._start_x + 300, 1100), (self._start_x + 1100, 1100), (self._start_x + 1200, 1200)]

        draw.rectangle(points1, fill = self.palette.main_color, outline='#000000')
        draw.polygon  (points2, fill = self.palette.main_color, outline='#000000')
        draw.polygon  (points3, fill = self.palette.main_color, outline='#000000')

        # draw arrows
        points5 = [(self._start_x + 600 , 1400), (self._start_x + 1000, 1400), (self._start_x + 950, 1350), (self._start_x + 1000, 1400), (self._start_x + 950, 1450)]
        points6 = [(self._start_x + 1000, 1600), (self._start_x + 600 , 1600), (self._start_x + 650, 1550), (self._start_x + 600 , 1600), (self._start_x + 650, 1650)]

        points7 = [(self._start_x + 600 , 1500), (self._start_x + 1000, 1500), (self._start_x + 950, 1450), (self._start_x + 1000, 1500), (self._start_x + 950, 1550)]

        self.lpoints = points1
        if self.bi:
            draw.line(points5, fill="#000000")
            draw.line(points6, fill="#000000")
        else:
            draw.line(points7, fill="#000000")
        
        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = self._start_x + 1400
        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        draw.text((self.lpoints[0], self.lpoints[3] + 50) , text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        draw.text((self.lpoints[0], self.lpoints[3] + 50 ), text=self.name, fill="#000000", font=font)
        draw.text((self.lpoints[0], self.lpoints[3] + 170), text="units: {}".format(self.units), fill="#000000", font=font)
        draw.text((self.lpoints[0], self.lpoints[3] + 290), text=self.activation, fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 1200, 1200),
                (self._start_x + 1200, 1800),
                (self._start_x + 1100, 1100)]
    
    def get_to(self):
        return [(self._start_x + 400, 1200),
                (self._start_x + 400, 1800),
                (self._start_x + 300, 1100)]


class ConvLSTM(Layer):
    """
    ConvLSTM Layer
    """
    def __init__(self, name, filters, kernels, activation, shape, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
        self.filters    = filters
        self.kernels    = kernels
        self.activation = activation
        self.shape = shape
        self._c    = int(min(math.log(filters, 2), 10))
        self._s    = min(int(shape[0]/100), 10)
        self.lpoints = []

    def draw(self, image, show_name=False, show_properties=False):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 300                 , 1100 - 50 * self._c // 2 - 100 * self._s // 2,
                  self._start_x + 1000 + 100 * self._s, 1700 - 50 * self._c // 2 + 100 * self._s // 2]

        for i in range(self._c):
            if i%2:
                draw.rectangle(points, fill = self.palette.main_color, outline='#000000')
            else:
                draw.rectangle(points, fill = self.palette.secondry, outline='#000000')
            points[0], points[1], points[2], points[3] = points[0] + 50, points[1] + 50, points[2] + 50, points[3] + 50
        
        points[0], points[1], points[2], points[3] = points[0] - 50, points[1] - 50, points[2] - 50, points[3] - 50


        points2 = [(points[0] +      (points[2] - points[0]) // 5,      points[1] + (points[3] - points[1]) // 2),
                   (points[0] + 40 * (points[2] - points[0]) // 5,      points[1] + (points[3] - points[1]) // 2),
                   (points[0] + 40 * (points[2] - points[0]) // 5 - 50, points[1] + (points[3] - points[1]) // 2 - 50),
                   (points[0] + 40 * (points[2] - points[0]) // 5     , points[1] + (points[3] - points[1]) // 2     ),
                   (points[0] + 40 * (points[2] - points[0]) // 5 - 50, points[1] + (points[3] - points[1]) // 2 + 50)]

        self.lpoints = points
        draw.line(points2, fill="#000000")
        
        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = points[2] + 200

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self.lpoints[0], self.lpoints[3] + 50]
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        points = [self.lpoints[0], self.lpoints[3] + 50]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 170]
        draw.text(points, text="filters:{}".format(self.filters), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 290]
        draw.text(points, text="kernel :{}".format(self.kernels), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 410]
        draw.text(points, text="{}".format(self.activation), fill="#000000", font=font)
    
    def get_from(self):
        point_start = [self._start_x + 300                 , 1100 - 50 * self._c // 2 - 100 * self._s // 2,
                       self._start_x + 1000 + 100 * self._s, 1700 - 50 * self._c // 2 + 100 * self._s // 2]
        
        point_end   = [self._start_x + 300                       + 50 * (self._c - 1), 1100 - 50 * self._c // 2 - 100 * self._s // 2 + 50 * (self._c - 1),
                       self._start_x + 1000 + 100 * self._s      + 50 * (self._c - 1), 1700 - 50 * self._c // 2 + 100 * self._s // 2 + 50 * (self._c - 1)]

        return [(point_end[2], point_end[1]),
                (point_end[2], point_end[3]),
                (point_start[2], point_start[1])]

    def get_to(self):
        point_start = [self._start_x + 300                 , 1100 - 50 * self._c // 2 - 100 * self._s // 2,
                       self._start_x + 1000 + 100 * self._s, 1700 - 50 * self._c // 2 + 100 * self._s // 2]
        point_end   = [self._start_x + 300                        + 50 * (self._c - 1), 1100 - 50 * self._c // 2 - 100 * self._s // 2 + 50 * (self._c - 1),
                       self._start_x + 1000 + 100 * self._s       + 50 * (self._c - 1), 1700 - 50 * self._c // 2 + 100 * self._s // 2 + 50 * (self._c - 1)]


        return [(point_end[0], point_end[1]),
                (point_end[0], point_end[3]),
                (point_start[0], point_start[1])]
    

class ActivationLayer(Layer):
    """
    Activation Layer
    """
    def __init__(self, name, activation, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
        self.activation = activation

    def draw(self, image, show_name=False, show_properties=False):
        draw = ImageDraw.Draw(image)

        draw.rectangle((self._start_x + 200, 1600, self._start_x + 600, 1200), fill = self.palette.main_color)
        draw.ellipse  ((self._start_x + 250, 1250, self._start_x + 550, 1550), fill = '#ffffff', outline='#000000')

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = self._start_x + 700
        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 250, 1650)
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 250, 1650)
        draw.text(points, text=self.name, fill="#000000", font=font)
        if self.activation:
            points = (self._start_x + 250, 1770)
            draw.text(points, text=self.activation, fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 600, 1200), (self._start_x + 600, 1600)]
    
    def get_to(self):
        return [(self._start_x + 200, 1200), (self._start_x + 200, 1600)]


class FlattenLayer(Layer):
    """
    Flatten Layer
    """
    def __init__(self, name, input_shape, output_shape, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
        self.input_shape = input_shape
        self.output_shape = output_shape

    def draw(self, image, show_name=False, show_properties=False):

        draw = ImageDraw.Draw(image)

        points1 = [ self._start_x + 100 , 1400 ,  self._start_x + 1100, 1600]
        points2 = [(self._start_x + 100 , 1400), (self._start_x + 200 , 1300), (self._start_x + 1200, 1300), (self._start_x + 1100, 1400)]
        points3 = [(self._start_x + 1200, 1300), (self._start_x + 1100, 1400), (self._start_x + 1100, 1600), (self._start_x + 1200, 1500)]

        draw.rectangle(points1, fill = self.palette.main_color, width = 3, outline='#000000')
        draw.polygon  (points2, fill = self.palette.main_color, width = 3, outline='#000000')
        draw.polygon  (points3, fill = self.palette.main_color, width = 3, outline='#000000')

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)
            
        # update end_x
        self._end_x = self._start_x + 1400
        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 100, 1650]
        draw.text(points, text=self.name, fill="#000000", font=font)
    
    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        points = [self._start_x + 200, 1650]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self._start_x + 200, 1770]
        draw.text(points, text="input shape:\n{}".format(self.input_shape), fill="#000000", font=font)


        points = [self._start_x + 200, 2010]
        draw.text(points, text="output shape:\n{}".format(self.output_shape), fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 1100, 1400),
                (self._start_x + 1100, 1600),
                (self._start_x + 1200, 1300)]
    
    def get_to(self):
        return [(self._start_x + 100, 1400),
                (self._start_x + 100, 1600),
                (self._start_x + 200, 1300)]