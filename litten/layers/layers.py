from PIL import ImageDraw, ImageFont 

class Layer:
    """
    Layer class contain the base structure for any layer
    """
    def __init__(self, name, number) -> None:
        """
        Construct Layer class

        Args:
            name: layer name
            number: layer number
        """
        self.name = name
        self.number = number
    
    def draw(self, image, show_properties=False):
        """
        draw default layer 
        """
        draw = ImageDraw.Draw(image)
        points = [(4 * (self.number - 1) * 20 + 20, 80),
                  (4 * (self.number - 1) * 20 + 60, 200)]
        
        draw.rectangle(xy  = points, fill='#98c1d9', width=1,outline='#000000')
        
        draw.ellipse((points[0][0] + 10, points[0][1] + 15 , points[0][0] + 30, points[0][1] + 35), fill = '#ffffff', outline='#ffffff')
        draw.ellipse((points[0][0] + 10, points[0][1] + 50 , points[0][0] + 30, points[0][1] + 70), fill = '#ffffff', outline='#ffffff')
        draw.ellipse((points[0][0] + 10, points[0][1] + 85, points[0][0] + 30, points[0][1] + 105), fill = '#ffffff', outline='#ffffff')

        if show_properties:
            fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 16)            
            draw.multiline_text((points[0][0] - 10, points[1][1] + 10), "{}".format(self.name ), fill='#000000', font=fnt)

        return image

    def show_prop(self):
        pass


class InputLayer(Layer):
    """
    Input Layer
    """
    def __init__(self, name, shape, number) -> None:
        super().__init__(name, number)
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
            points = [(20, 40 + i * 20), (40, 60 + i * 20)] 
            draw.rectangle(points, fill = "#98c1d9", width = 2, outline= '#000000')


        if show_properties:
            fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 16)            
            draw.multiline_text((points[0][0] - 10, points[0][1] + 25), "{}".format(self.name ), fill='#000000', font=fnt)
            draw.multiline_text((points[0][0] - 15, points[0][1] + 40), "{}".format(self.shape), fill='#000000', font=fnt)

        return image

    def show_prop(self):
        pass


class DenseLayer(Layer):
    def __init__(self, name, number, units) -> None:
        super().__init__(name, number)
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

        draw.ellipse((4 * (self.number - 1) * 20 + 20, 60 , 4 * (self.number - 1) * 20 + 60, 100), fill = '#98c1d9', outline='#000000')
        draw.ellipse((4 * (self.number - 1) * 20 + 20, 120, 4 * (self.number - 1) * 20 + 60, 160), fill = '#98c1d9', outline='#000000')
        draw.ellipse((4 * (self.number - 1) * 20 + 20, 180, 4 * (self.number - 1) * 20 + 60, 220), fill = '#98c1d9', outline='#000000')

        return image

    def show_prop(self):
        pass


class CNNLayer(Layer):
    def __init__(self, name, number) -> None:
        super().__init__(name, number)
    
    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)

        draw.rectangle((4 * (self.number - 1) * 20 + 10, 170, 4 * (self.number - 1) * 20 + 70, 110), fill = '#94a4b2', outline='#000000')
        draw.rectangle((4 * (self.number - 1) * 20 + 15, 175, 4 * (self.number - 1) * 20 + 75, 115), fill = '#a2dbf9', outline='#000000')
        draw.rectangle((4 * (self.number - 1) * 20 + 20, 180, 4 * (self.number - 1) * 20 + 80, 120), fill = '#94a4b2', outline='#000000')
        draw.rectangle((4 * (self.number - 1) * 20 + 25, 185, 4 * (self.number - 1) * 20 + 85, 125), fill = '#a2dbf9', outline='#000000')

        return image


class PoolingLayer(Layer):
    def __init__(self, name, number) -> None:
        super().__init__(name, number)
    
    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)

        draw.rectangle((4 * (self.number - 1) * 20 + 20, 160, 4 * (self.number - 1) * 20 + 60, 120), fill = '#94a4b2', outline='#000000')
        draw.rectangle((4 * (self.number - 1) * 20 + 25, 165, 4 * (self.number - 1) * 20 + 65, 125), fill = '#a2dbf9', outline='#000000')
        draw.rectangle((4 * (self.number - 1) * 20 + 30, 170, 4 * (self.number - 1) * 20 + 70, 130), fill = '#94a4b2', outline='#000000')
        draw.rectangle((4 * (self.number - 1) * 20 + 35, 175, 4 * (self.number - 1) * 20 + 75, 135), fill = '#a2dbf9', outline='#000000')

        return image

    def show_prop(self):
        pass


class EmbeddingLayer(Layer):
    def __init__(self, name, number) -> None:
        super().__init__(name, number)
    
    def draw(self, image, show_properties=False):
        return super().draw(image, show_properties)

    def show_prop(self):
        pass


class RecurrentLayer(Layer):
    def __init__(self, name, number) -> None:
        super().__init__(name, number)
    
    def draw(self, image, show_properties=False):
        return super().draw(image, show_properties)

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
    def __init__(self, name, number) -> None:
        super().__init__(name, number)
    
    def draw(self, image, show_properties=False):
        draw = ImageDraw.Draw(image)

        draw.rectangle((4 * (self.number - 1) * 20 + 20, 160, 4 * (self.number - 1) * 20 + 60, 120), fill = '#98c1d9', outline='#000000')
        draw.ellipse  ((4 * (self.number - 1) * 20 + 25, 125, 4 * (self.number - 1) * 20 + 55, 155), fill = '#ffffff', outline='#000000')

        return image

    def show_prop():
        pass

