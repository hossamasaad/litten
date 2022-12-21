import math

from PIL import ImageDraw, ImageFont 
font = ImageFont.truetype("layers/FreeMonoBold.ttf", 10)


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
        points = [(self._start_x + 20, 80),
                  (self._start_x + 60, 200)]
        
        draw.rounded_rectangle(xy  = points, radius=3, fill=self.palette.main_color)
        
        draw.ellipse((points[0][0] + 10, points[0][1] + 15, points[0][0] + 30, points[0][1] + 35 ), fill = '#ffffff', outline='#000')
        draw.ellipse((points[0][0] + 10, points[0][1] + 50, points[0][0] + 30, points[0][1] + 70 ), fill = '#ffffff', outline='#000')
        draw.ellipse((points[0][0] + 10, points[0][1] + 85, points[0][0] + 30, points[0][1] + 105), fill = '#ffffff', outline='#000')

        # update end_x
        self._end_x = self._start_x + 80

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

    @property
    def end(self):
        return self._end_x

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 20, 210)
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 20, 210)
        draw.text(points, text=self.name, fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 60, 80), (self._start_x + 60, 200)]

    def get_to(self):
        return [(self._start_x + 20, 80), (self._start_x + 20, 200)]


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
            points = [(self._start_x + 20, 40 + i * 20), (self._start_x + 40, 60 + i * 20)] 
            draw.rectangle(points, fill = self.palette.main_color, width = 2, outline= '#000000')

        # update end_x
        self._end_x = self._start_x + 60

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 15, 250)
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        points = (self._start_x + 15, 250)        
        draw.text(points, text=self.name, fill="#000000", font=font) 
        
        points = (self._start_x, 262)
        draw.text(points, text="{}".format(self.shape), fill="#000000", font=font) 

    def get_from(self):
        return [(self._start_x + 40, 40), (self._start_x + 40, 240)]
        

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
        points = [(self._start_x + 20, 60),
                  (self._start_x + 60, 220)]
        
        draw.rounded_rectangle(xy  = points, radius=5, fill=self.palette.main_color)
        
        draw.ellipse((points[0][0] + 10, points[0][1] + 15, points[0][0] + 30, points[0][1] + 35 ), fill = '#ffffff', outline='#000')
        draw.ellipse((points[0][0] + 10, points[0][1] + 50, points[0][0] + 30, points[0][1] + 70 ), fill = '#ffffff', outline='#000')
        draw.ellipse((points[0][0] + 10, points[0][1] + 120, points[0][0] + 30, points[0][1] + 140), fill = '#ffffff', outline='#000')

        draw.line   ([(points[0][0] + 20, points[0][1] + 80), (points[0][0] + 20, points[0][1] + 81)], fill='#000000', width=2)
        draw.line   ([(points[0][0] + 20, points[0][1] + 90), (points[0][0] + 20, points[0][1] + 91)], fill='#000000', width=2)
        draw.line   ([(points[0][0] + 20, points[0][1] + 100), (points[0][0] + 20, points[0][1] + 101)], fill='#000000', width=2)
        draw.line   ([(points[0][0] + 20, points[0][1] + 110), (points[0][0] + 20, points[0][1] + 111)], fill='#000000', width=2)

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = self._start_x + 80

        return image
    
    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points1 = (self._start_x + 23, 225)
        draw.text(points1, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)
        points1 = (self._start_x + 23, 225)
        draw.text(points1, text=self.name, fill="#000000", font=font)
        
        points2 = (self._start_x + 23, 237)
        draw.text(points2, text="units: {}".format(self.units), fill="#000000", font=font)
        
        points3 = (self._start_x + 23, 249)
        draw.text(points3, text=self.activation, fill="#000000", font=font)

        points4 = (self._start_x + 23, 261)
        draw.text(points4, text="input shape\n{}".format(self.input_shape), fill="#000000", font=font)        
        
        points5 = (self._start_x + 23, 285)
        draw.text(points5, text="output shape\n{}".format(self.output_shape), fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 60, 63),
                (self._start_x + 60, 217)]
    
    def get_to(self):
        return [(self._start_x + 20, 63),
                (self._start_x + 20, 217)]


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
        points = [self._start_x + 30                , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                  self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]

        for i in range(self._c):
            if i%2:
                draw.rectangle(points, fill = self.palette.main_color, outline='#000000')
            else:
                draw.rectangle(points, fill = self.palette.secondry, outline='#000000')

            points[0], points[1], points[2], points[3] = points[0] + 5, points[1] + 5, points[2] + 5, points[3] + 5
        
        self.lpoints = points

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = points[2] + 20

        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self.lpoints[0], self.lpoints[3]]
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        points = [self.lpoints[0], self.lpoints[3]]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 12]
        draw.text(points, text=self.activation, fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 24]
        draw.text(points, text="filters:{}".format(self.filters), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 36]
        draw.text(points, text="kernel:{}".format(self.kernel), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 48]
        draw.text(points, text="input shape:\n{}".format(self.input_shape), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 72]
        draw.text(points, text="output shape:\n{}".format(self.output_shape), fill="#000000", font=font)

    def get_from(self):
        point_start = [self._start_x + 30                , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                       self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]
        
        point_end   = [self._start_x + 30                         + 5 * (self._c - 1), 110 - 5 * self._c // 2 - 10 * self._s // 2 + 5 * (self._c - 1),
                       self._start_x + 100 + 10    * self._s      + 5 * (self._c - 1), 170 - 5 * self._c // 2 + 10 * self._s // 2 + 5 * (self._c - 1)]

        return [(point_end[2], point_end[1]),
                (point_end[2], point_end[3]),
                (point_start[2], point_start[1])]
    
    def get_to(self):
        point_start = [self._start_x + 30                , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                       self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]
        point_end   = [self._start_x + 30                         + 5 * (self._c - 1), 110 - 5 * self._c // 2 - 10 * self._s // 2 + 5 * (self._c - 1),
                       self._start_x + 100 + 10    * self._s      + 5 * (self._c - 1), 170 - 5 * self._c // 2 + 10 * self._s // 2 + 5 * (self._c - 1)]


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
        points = [self._start_x + 30                     , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                  self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]

        for i in range(self._c):
            if i%2:
                draw.rectangle(points, fill = self.palette.main_color, outline='#000000')
            else:
                draw.rectangle(points, fill = self.palette.secondry, outline='#000000')

            points[0], points[1], points[2], points[3] = points[0] + 5, points[1] + 5, points[2] + 5, points[3] + 5
        
        self.lpoints = points
        
        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = points[2] + 20

        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self.lpoints[0], self.lpoints[3]]
        draw.text(points, text=self.name, fill="#000000", font=font)
    
    def _show_prop(self, image):

        draw = ImageDraw.Draw(image)
        
        points = [self.lpoints[0], self.lpoints[3]]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 12]
        draw.text(points, text="padding: {}".format(self.padding), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 24]
        draw.text(points, text="pool: {}".format(self.pool_size), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 36]
        draw.text(points, text="input shape: \n{}".format(self.input_shape), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 60]
        draw.text(points, text="output shape \n{}".format(self.output_shape), fill="#000000", font=font)

    def get_from(self):
        point_start = [self._start_x + 30                , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                       self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]
        
        point_end   = [self._start_x + 30                         + 5 * (self._c - 1), 110 - 5 * self._c // 2 - 10 * self._s // 2 + 5 * (self._c - 1),
                       self._start_x + 100 + 10    * self._s      + 5 * (self._c - 1), 170 - 5 * self._c // 2 + 10 * self._s // 2 + 5 * (self._c - 1)]

        return [(point_end[2], point_end[1]),
                (point_end[2], point_end[3]),
                (point_start[2], point_start[1])]
    
    def get_to(self):
        point_start = [self._start_x + 30                , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                       self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]
        point_end   = [self._start_x + 30                         + 5 * (self._c - 1), 110 - 5 * self._c // 2 - 10 * self._s // 2 + 5 * (self._c - 1),
                       self._start_x + 100 + 10    * self._s      + 5 * (self._c - 1), 170 - 5 * self._c // 2 + 10 * self._s // 2 + 5 * (self._c - 1)]


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
            points = [(self._start_x + 20, 70 + i * 20), (self._start_x + 40, 90 + i * 20)] 
            if i % 2:
                draw.rounded_rectangle(points, radius = 2, fill = self.palette.main_color, width = 1, outline= '#000000')
            else:
                draw.rounded_rectangle(points, radius = 2, fill = self.palette.secondry, width = 1, outline= '#000000')

        for i in range(7):
            points = [(self._start_x + 40, 70 + i * 20), (self._start_x + 60, 90 + i * 20)]
            if i % 2:
                draw.rounded_rectangle(points, radius = 2, fill = self.palette.secondry, width = 1, outline= '#000000')
            else:
                draw.rounded_rectangle(points, radius = 2, fill = self.palette.main_color, width = 1, outline= '#000000')

        self.lpoints = points

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = self._start_x + 80
        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self.lpoints[0][0] - 25, self.lpoints[1][1] + 5]
        draw.text(points, text=self.name, fill="#000000", font=font)
    
    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)
        
        points = [self.lpoints[0][0] - 27, self.lpoints[1][1] + 5]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self.lpoints[0][0] - 30, self.lpoints[1][1] + 17]
        draw.text(points, text="input_dim :{}".format(self.input_dim), fill="#000000", font=font)

        points = [self.lpoints[0][0] - 30, self.lpoints[1][1] + 29]
        draw.text(points, text="output_dim:{}".format(self.output_dim), fill="#000000", font=font)

        points = [self.lpoints[0][0] - 30, self.lpoints[1][1] + 41]
        draw.text(points, text="input_shape:\n{}".format(self.input_shape), fill="#000000", font=font)

        points = [self.lpoints[0][0] - 30, self.lpoints[1][1] + 65]
        draw.text(points, text="output_shape:\n{}".format(self.output_shape), fill="#000000", font=font)
 
    def get_from(self):
        return [(self._start_x + 57, 70), (self._start_x + 57, 210)]
    
    def get_to(self):
        return [(self._start_x + 23, 70), (self._start_x + 23, 210)]


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
        
        points1 = [ self._start_x + 40, 120, self._start_x + 120, 180]
        points2 = [(self._start_x + 40, 120), (self._start_x + 30, 110), (self._start_x + 30, 170), (self._start_x + 40, 180)]
        points3 = [(self._start_x + 40, 120), (self._start_x + 30, 110), (self._start_x + 110, 110), (self._start_x + 120, 120)]

        draw.rectangle(points1, fill = self.palette.main_color, outline='#000000')
        draw.polygon  (points2, fill = self.palette.main_color, outline='#000000')
        draw.polygon  (points3, fill = self.palette.main_color, outline='#000000')

        # draw arrows
        points5 = [(self._start_x + 60 , 140), (self._start_x + 100, 140), (self._start_x + 95, 135), (self._start_x + 100, 140), (self._start_x + 95, 145)]
        points6 = [(self._start_x + 100, 160), (self._start_x + 60 , 160), (self._start_x + 65, 155), (self._start_x + 60 , 160), (self._start_x + 65, 165)]

        points7 = [(self._start_x + 60 , 150), (self._start_x + 100, 150), (self._start_x + 95, 145), (self._start_x + 100, 150), (self._start_x + 95, 155)]

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
        self._end_x = self._start_x + 140
        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        draw.text((self.lpoints[0], self.lpoints[3] + 5) , text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        draw.text((self.lpoints[0], self.lpoints[3] + 5) , text=self.name, fill="#000000", font=font)
        draw.text((self.lpoints[0], self.lpoints[3] + 17), text="units: {}".format(self.units), fill="#000000", font=font)
        draw.text((self.lpoints[0], self.lpoints[3] + 29), text=self.activation, fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 120, 120),
                (self._start_x + 120, 180),
                (self._start_x + 110, 110)]
    
    def get_to(self):
        return [(self._start_x + 40, 120),
                (self._start_x + 40, 180),
                (self._start_x + 30, 110)]


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
        points = [self._start_x + 30                     , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                  self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]

        for i in range(self._c):
            if i%2:
                draw.rectangle(points, fill = self.palette.main_color, outline='#000000')
            else:
                draw.rectangle(points, fill = self.palette.secondry, outline='#000000')
            points[0], points[1], points[2], points[3] = points[0] + 5, points[1] + 5, points[2] + 5, points[3] + 5
        
        points[0], points[1], points[2], points[3] = points[0] - 5, points[1] - 5, points[2] - 5, points[3] - 5


        points2 = [(points[0] + (points[2] - points[0]) // 5, points[1] + (points[3] - points[1]) // 2),
                   (points[0] + 4 * (points[2] - points[0]) // 5, points[1] + (points[3] - points[1]) // 2),
                   (points[0] + 4 * (points[2] - points[0]) // 5 - 5, points[1] + (points[3] - points[1]) // 2 - 5),
                   (points[0] + 4 * (points[2] - points[0]) // 5, points[1] + (points[3] - points[1]) // 2),
                   (points[0] + 4 * (points[2] - points[0]) // 5 - 5, points[1] + (points[3] - points[1]) // 2 + 5)]

        self.lpoints = points
        draw.line(points2, fill="#000000")
        
        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = points[2] + 20

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self.lpoints[0], self.lpoints[3] + 5]
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        points = [self.lpoints[0], self.lpoints[3] + 5]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 17]
        draw.text(points, text="filters:{}".format(self.filters), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 29]
        draw.text(points, text="kernel :{}".format(self.kernels), fill="#000000", font=font)

        points = [self.lpoints[0], self.lpoints[3] + 41]
        draw.text(points, text="{}".format(self.activation), fill="#000000", font=font)
    
    def get_from(self):
        point_start = [self._start_x + 30                , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                       self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]
        
        point_end   = [self._start_x + 30                         + 5 * (self._c - 1), 110 - 5 * self._c // 2 - 10 * self._s // 2 + 5 * (self._c - 1),
                       self._start_x + 100 + 10    * self._s      + 5 * (self._c - 1), 170 - 5 * self._c // 2 + 10 * self._s // 2 + 5 * (self._c - 1)]

        return [(point_end[2], point_end[1]),
                (point_end[2], point_end[3]),
                (point_start[2], point_start[1])]

    def get_to(self):
        point_start = [self._start_x + 30                , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                       self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]
        point_end   = [self._start_x + 30                         + 5 * (self._c - 1), 110 - 5 * self._c // 2 - 10 * self._s // 2 + 5 * (self._c - 1),
                       self._start_x + 100 + 10    * self._s      + 5 * (self._c - 1), 170 - 5 * self._c // 2 + 10 * self._s // 2 + 5 * (self._c - 1)]


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

        draw.rectangle((self._start_x + 20, 160, self._start_x + 60, 120), fill = self.palette.main_color)
        draw.ellipse  ((self._start_x + 25, 125, self._start_x + 55, 155), fill = '#ffffff', outline='#000000')

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)

        # update end_x
        self._end_x = self._start_x + 70
        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 25, 165)
        draw.text(points, text=self.name, fill="#000000", font=font)

    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)
        points = (self._start_x + 25, 165)
        draw.text(points, text=self.name, fill="#000000", font=font)
        if self.activation:
            points = (self._start_x + 25, 177)
            draw.text(points, text=self.activation, fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 60, 120), (self._start_x + 60, 160)]
    
    def get_to(self):
        return [(self._start_x + 20, 120), (self._start_x + 20, 160)]


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

        points1 = [ self._start_x + 40, 170, self._start_x + 60, 190]
        points2 = [(self._start_x + 40, 170), (self._start_x, 110), (self._start_x, 130), (self._start_x + 40, 190)]
        points3 = [(self._start_x + 40, 170), (self._start_x, 110), (self._start_x + 20, 110), (self._start_x + 60, 170)]

        draw.rectangle(points1, fill = self.palette.main_color, outline='#000000')
        draw.polygon  (points2, fill = self.palette.main_color, outline='#000000')
        draw.polygon  (points3, fill = self.palette.main_color, outline='#000000')

        if show_properties:
            self._show_prop(image)
        elif show_name:
            self._show_name(image)
            
        # update end_x
        self._end_x = self._start_x + 80
        return image

    def _show_name(self, image):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 20, 195]
        draw.text(points, text=self.name, fill="#000000", font=font)
    
    def _show_prop(self, image):
        draw = ImageDraw.Draw(image)

        points = [self._start_x + 20, 195]
        draw.text(points, text=self.name, fill="#000000", font=font)

        points = [self._start_x + 20, 207]
        draw.text(points, text="input shape:\n{}".format(self.input_shape), fill="#000000", font=font)


        points = [self._start_x + 20, 232]
        draw.text(points, text="output shape:\n{}".format(self.output_shape), fill="#000000", font=font)

    def get_from(self):
        return [(self._start_x + 60, 170),
                (self._start_x + 60, 190),
                (self._start_x + 20, 110)]
    
    def get_to(self):
        return [(self._start_x + 40, 170),
                (self._start_x + 40, 190),
                (self._start_x, 110)]