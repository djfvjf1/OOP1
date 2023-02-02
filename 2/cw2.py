from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, value):
        pass

    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
        
class Circle(Shape):
    pass

class Rectangle(Shape):
