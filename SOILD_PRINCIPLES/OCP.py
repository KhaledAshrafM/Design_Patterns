# Open-Closed Principle: a class should be open for extension and closed to modification.

# Example:
from enum import Enum
from abc import ABC, abstractmethod

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.size = size
        self.color = color 
        self.name = name

class productFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color  == color:
                yield p  
    
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if (p.size == size) and (p.color== color):
                yield p

# Enterprise Patterns: Specification
class Specification:
    def is_satisfied(self, item):
        pass

class Filter(ABC):
    @abstractmethod
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, item):
        return item.color == self.color
    

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.RED, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)
products = [apple, tree, house]

color_spec = ColorSpecification(Color.BLUE)
better_fly = BetterFilter()
better_fly.filter(products, color_spec)
