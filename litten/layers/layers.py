import math
from PIL import ImageDraw, ImageFont 


class Layer:
    """
    Layer class contain the base structure for any layer
    """
    def __init__(self, name, start_x, palette) -> None:
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

    def draw(self, image, show_properties=False):
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

        return image

    @property
    def end(self):
        return self._end_x

    def show_prop(self):
        pass
    
    def get_from(self):
        return [(self._start_x + 60, 80), (self._start_x + 60, 200)]

    def get_to(self):
        return [(self._start_x + 20, 80), (self._start_x + 20, 200)]


class InputLayer(Layer):
    """
    Input Layer
    """
    def __init__(self, name, start_x, palette, shape=0) -> None:
        super().__init__(name, start_x, palette)
        self.shape = shape
    
    def draw(self, image, show_properties = False):
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

        return image

    def show_prop(self):
        pass
    
    def get_from(self):
        return [(self._start_x + 40, 40), (self._start_x + 40, 240)]


class DenseLayer(Layer):
    """
    Fully Connected Layer (Dense Layer)
    """
    def __init__(self, name, start_x, palette, units) -> None:
        super().__init__(name, start_x, palette)
        self.units = units

    def draw(self, image, show_properties=False):
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

        draw.line   ([(points[0][0] + 20, points[0][1] + 80 ), (points[0][0] + 20, points[0][1] + 81 )], fill='#000000', width=2)
        draw.line   ([(points[0][0] + 20, points[0][1] + 90 ), (points[0][0] + 20, points[0][1] + 91 )], fill='#000000', width=2)
        draw.line   ([(points[0][0] + 20, points[0][1] + 100), (points[0][0] + 20, points[0][1] + 101)], fill='#000000', width=2)
        draw.line   ([(points[0][0] + 20, points[0][1] + 110), (points[0][0] + 20, points[0][1] + 111)], fill='#000000', width=2)

        # update end_x
        self._end_x = self._start_x + 80

        return image

    def show_prop(self):
        pass

    def get_from(self):
        return [(self._start_x + 60, 63), (self._start_x + 60, 217)]
    
    def get_to(self):
        return [(self._start_x + 20, 63), (self._start_x + 20, 217)]


class ConvLayer(Layer):
    """
    Convluation Layer 
    """
    def __init__(self, name, start_x, palette, kernels, shape) -> None:
        super().__init__(name, start_x, palette)
        self.units = kernels
        self.shape = shape
        self._c    = int(min(math.log(kernels, 2), 10))
        self._s    = min(int(shape[0]/100), 10) 

    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 30                , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                  self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]

        for i in range(self._c):
            if i%2:
                draw.rectangle(points, fill = self.palette.main_color, outline='#000000')
            else:
                draw.rectangle(points, fill = self.palette.secondry, outline='#000000')

            points[0], points[1], points[2], points[3] = points[0] + 5, points[1] + 5, points[2] + 5, points[3] + 5
            
            
        # update end_x
        self._end_x = points[2] + 20

        return image

    def show_prop(self):
        pass
    
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
    def __init__(self, name, start_x, palette, kernels, shape) -> None:
        super().__init__(name, start_x, palette)
        self.units = kernels
        self.shape = shape
        self._c    = int(min(math.log(kernels, 2), 10))
        self._s    = int(shape[0]/100) 

    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 30                     , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                  self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]

        for i in range(self._c):
            if i%2:
                draw.rectangle(points, fill = self.palette.main_color, outline='#000000')
            else:
                draw.rectangle(points, fill = self.palette.secondry, outline='#000000')

            points[0], points[1], points[2], points[3] = points[0] + 5, points[1] + 5, points[2] + 5, points[3] + 5
                 
            
        # update end_x
        self._end_x = points[2] + 20

        return image

    def show_prop(self):
        pass

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
    def __init__(self, name, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
    
    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((self._start_x + 20, 60, self._start_x + 60, 200), radius=5, fill = self.palette.main_color, outline='#000000')

        # update end_x
        self._end_x = self._start_x + 80
        return image

    def show_prop(self):
        pass
    
    def get_from(self):
        return [(self._start_x + 57, 60), (self._start_x + 57, 200)]
    
    def get_to(self):
        return [(self._start_x + 23, 60), (self._start_x + 23, 200)]


class RecurrentLayer(Layer):
    """
    Recurrent Layer
    """
    def __init__(self, name, start_x, palette, bi=False) -> None:
        super().__init__(name, start_x, palette)
        self.bi = bi
        
    def draw(self, image, show_properties=False):
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

        if self.bi:
            draw.line(points5, fill="#000000")
            draw.line(points6, fill="#000000")
        else:
            draw.line(points7, fill="#000000")

        # update end_x
        self._end_x = self._start_x + 140
        return image

    def show_prop(self):
        pass

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
    def __init__(self, name, start_x, palette, kernels, shape) -> None:
        super().__init__(name, start_x, palette)
        self.units = kernels
        self.shape = shape
        self._c    = int(min(math.log(kernels, 2), 10))
        self._s    = min(int(shape[0]/100), 10)

    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 30                     , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                  self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]

        for i in range(self._c):
            draw.rectangle(points, fill = self.palette.main_color, outline='#000000')
            points[0], points[1], points[2], points[3] = points[0] + 5, points[1] + 5, points[2] + 5, points[3] + 5
        
        points[0], points[1], points[2], points[3] = points[0] - 5, points[1] - 5, points[2] - 5, points[3] - 5


        points2 = [(points[0] + (points[2] - points[0]) // 5, points[1] + (points[3] - points[1]) // 2),
                   (points[0] + 4 * (points[2] - points[0]) // 5, points[1] + (points[3] - points[1]) // 2),
                   (points[0] + 4 * (points[2] - points[0]) // 5 - 5, points[1] + (points[3] - points[1]) // 2 - 5),
                   (points[0] + 4 * (points[2] - points[0]) // 5, points[1] + (points[3] - points[1]) // 2),
                   (points[0] + 4 * (points[2] - points[0]) // 5 - 5, points[1] + (points[3] - points[1]) // 2 + 5)]

        draw.line(points2, fill="#000000")
            
        # update end_x
        self._end_x = points[2] + 20

    def show_prop(self):
        pass
    
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
    def __init__(self, name, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
    
    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)

        draw.rectangle((self._start_x + 20, 160, self._start_x + 60, 120), fill = self.palette.main_color)
        draw.ellipse  ((self._start_x + 25, 125, self._start_x + 55, 155), fill = '#ffffff', outline='#000000')

        # update end_x
        self._end_x = self._start_x + 70
        return image

    def show_prop():
        pass

    def get_from(self):
        return [(self._start_x + 60, 120), (self._start_x + 60, 160)]
    
    def get_to(self):
        return [(self._start_x + 20, 120), (self._start_x + 20, 160)]


class FlattenLayer(Layer):
    """
    Flatten Layer
    """
    def __init__(self, name, start_x, palette) -> None:
        super().__init__(name, start_x, palette)
    
    def draw(self, image, show_properties=False):

        draw = ImageDraw.Draw(image)

        points1 = [ self._start_x + 40, 170, self._start_x + 60, 190]
        points2 = [(self._start_x + 40, 170), (self._start_x, 110), (self._start_x, 130), (self._start_x + 40, 190)]
        points3 = [(self._start_x + 40, 170), (self._start_x, 110), (self._start_x + 20, 110), (self._start_x + 60, 170)]

        draw.rectangle(points1, fill = self.palette.main_color, outline='#000000')
        draw.polygon  (points2, fill = self.palette.main_color, outline='#000000')
        draw.polygon  (points3, fill = self.palette.main_color, outline='#000000')

        # update end_x
        self._end_x = self._start_x + 80
        return image

    def show_prop(self):
        pass

    def get_from(self):
        return [(self._start_x + 60, 170),
                (self._start_x + 60, 190),
                (self._start_x + 20, 110)]
    
    def get_to(self):
        return [(self._start_x + 40, 170),
                (self._start_x + 40, 190),
                (self._start_x, 110)]