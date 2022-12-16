import math
from PIL import ImageDraw, ImageFont 

class Layer:
    """
    Layer class contain the base structure for any layer
    """
    def __init__(self, name, start_x) -> None:
        """
        Construct Layer class

        Args:
            name: layer name
            number: layer number
        """
        self.name    = name
        self._start_x = start_x
        self._end_x   = 0

    def draw(self, image, show_properties=False):
        """
        draw default layer 
        """
        draw = ImageDraw.Draw(image)
        points = [(self._start_x + 20, 80),
                  (self._start_x + 60, 200)]
        
        draw.rounded_rectangle(xy  = points, radius=5, fill='#94a4b2')
        
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


class InputLayer(Layer):
    """
    Input Layer
    """
    def __init__(self, name, shape, start_x = 0) -> None:
        super().__init__(name, start_x)
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
            draw.rectangle(points, fill = "#94a4b2", width = 2, outline= '#000000')

        # update end_x
        self._end_x = self._start_x + 60

        return image

    def show_prop(self):
        pass


class DenseLayer(Layer):
    def __init__(self, name, start_x, units) -> None:
        super().__init__(name, start_x)
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

        draw.ellipse((self._start_x + 20, 60 , self._start_x + 60, 100), fill = '#94a4b2', outline='#000000')
        draw.ellipse((self._start_x + 20, 120, self._start_x + 60, 160), fill = '#94a4b2', outline='#000000')
        draw.ellipse((self._start_x + 20, 180, self._start_x + 60, 220), fill = '#94a4b2', outline='#000000')
        
        # update end_x
        self._end_x = self._start_x + 80

        return image

    def show_prop(self):
        pass


class CNNLayer(Layer):
    def __init__(self, name, start_x, kernels, shape) -> None:
        super().__init__(name, start_x)
        self.units = kernels
        self.shape = shape
        self._c    = int(min(math.log(kernels, 2), 10))
        self._s    = min(int(shape[0]/100), 10) 

    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 30                     , 110 - 5 * self._c // 2 - 10 * self._s // 2,
                  self._start_x + 100 + 10 * self._s, 170 - 5 * self._c // 2 + 10 * self._s // 2]

        for i in range(self._c):
            draw.rectangle(points, fill = '#94a4b2', outline='#000000')
            points[0], points[1], points[2], points[3] = points[0] + 5, points[1] + 5, points[2] + 5, points[3] + 5
            
            
        # update end_x
        self._end_x = points[2] + 20

        return image


class PoolingLayer(Layer):
    def __init__(self, name, start_x, kernels, shape) -> None:
        super().__init__(name, start_x)
        self.units = kernels
        self.shape = shape
        self._c    = int(min(math.log(kernels, 2), 10))
        self._s    = int(shape[0]/100) 

    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)
        points = [self._start_x + 30                     , 110 - 5 * self._c // 2 - 10 * self._s,
                  self._start_x + 100 + 10 * self._s // 2, 170 - 5 * self._c // 2 + 10 * self._s]

        for i in range(self._c):
            draw.rectangle(points, fill = '#94a4b9', outline='#000000')
            points[0], points[1], points[2], points[3] = points[0] + 5, points[1] + 5, points[2] + 5, points[3] + 5
            
            
        # update end_x
        self._end_x = points[2] + 20

        return image


class EmbeddingLayer(Layer):
    def __init__(self, name, start_x) -> None:
        super().__init__(name, start_x)
    
    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((self._start_x + 20, 60, self._start_x + 60, 200), radius=5, fill = '#94a4b9', outline='#000000')

        # update end_x
        self._end_x = self._start_x + 80
        return image

    def show_prop(self):
        pass


class RecurrentLayer(Layer):
    def __init__(self, name, start_x, bi=False) -> None:
        super().__init__(name, start_x)
        self.bi = bi
        
    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)
        
        points1 = [ self._start_x + 40, 100, self._start_x + 120, 160]
        points2 = [(self._start_x + 40, 100), (self._start_x + 30, 90), (self._start_x + 30, 150), (self._start_x + 40, 160)]
        points3 = [(self._start_x + 40, 100), (self._start_x + 30, 90), (self._start_x + 110, 90), (self._start_x + 120, 100)]

        draw.rectangle(points1, fill = '#94a4b9', outline='#000000')
        draw.polygon  (points2, fill = '#94a4b9', outline='#000000')
        draw.polygon  (points3, fill = '#94a4b9', outline='#000000')

        # draw arrows
        points5 = [(self._start_x + 60 , 120), (self._start_x + 100, 120), (self._start_x + 95, 115), (self._start_x + 100, 120), (self._start_x + 95, 125)]
        points6 = [(self._start_x + 100, 140), (self._start_x + 60 , 140), (self._start_x + 65, 135), (self._start_x + 60 , 140), (self._start_x + 65, 145)]

        points7 = [(self._start_x + 60 , 130), (self._start_x + 100, 130), (self._start_x + 95, 125), (self._start_x + 100, 130), (self._start_x + 95, 135)]

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


class ConvLSTM(Layer):
    def __init__(self, name, number) -> None:
        super().__init__(name, number)
    
    def draw(self, image, show_properties=False):
        return super().draw(image, show_properties)

    def show_prop(self):
        pass


class NormaliztionLayer(Layer):
    def __init__(self, name, number) -> None:
        super().__init__(name, number)
    
    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)

        draw.rectangle((4 * (self.number - 1) * 20 + 20, 160, 4 * (self.number - 1) * 20 + 60, 120), fill = '#94a4b2', outline='#000000')
        draw.rectangle((4 * (self.number - 1) * 20 + 25, 165, 4 * (self.number - 1) * 20 + 65, 125), fill = '#edebd8', outline='#000000')
        draw.rectangle((4 * (self.number - 1) * 20 + 30, 170, 4 * (self.number - 1) * 20 + 70, 130), fill = '#94a4b2', outline='#000000')
        draw.rectangle((4 * (self.number - 1) * 20 + 35, 175, 4 * (self.number - 1) * 20 + 75, 135), fill = '#edebd8', outline='#000000')

        return image

    def show_prop(self):
        pass


class RegularizationLayer(Layer):
    def __init__(self, name, number) -> None:
        super().__init__(name, number)
    
    def draw(self, image, show_properties=False):
        return super().draw(image, show_properties)

    def show_prop(self):
        pass


class ActivationLayer(Layer):
    def __init__(self, name, start_x) -> None:
        super().__init__(name, start_x)
    
    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)

        draw.rectangle((self._start_x + 20, 160, self._start_x + 60, 120), fill = '#94a4b9')
        draw.ellipse  ((self._start_x + 25, 125, self._start_x + 55, 155), fill = '#ffffff', outline='#000000')

        # update end_x
        self._end_x = self._start_x + 70
        return image

    def show_prop():
        pass

