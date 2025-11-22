# Getter, Setter, Property Decorator
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be positive!")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must be positive!")

    @property
    def area(self):
        return self._width * self._height

rect = Rectangle(5, 10)
print(rect.area)
rect.width = 7
print(rect.area)