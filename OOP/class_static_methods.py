# Class Variables, Methods, Static Methods
class Circle:
    pi = 3.1416
    count = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.count += 1

    def area(self):
        return Circle.pi * self.radius ** 2

    @classmethod
    def total_circles(cls):
        return cls.count

    @staticmethod
    def description():
        return "This class represents a circle."


c1 = Circle(5)
c2 = Circle(10)
print(c1.area())
print(Circle.total_circles())
print(Circle.description())