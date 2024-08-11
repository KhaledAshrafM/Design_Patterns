# Open-Closed Principle (OCP): 
# Software entities (classes, modules, functions, etc.) should be open for extension but closed to modification.

# Example:

from enum import Enum
from abc import ABC, abstractmethod

class Color(Enum):
    """Enumeration for colors."""
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    """Enumeration for sizes."""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    """Represents a product with a name, color, and size."""
    
    def __init__(self, name, color, size):
        """Initializes a new product.
        
        Args:
            name (str): The name of the product.
            color (Color): The color of the product.
            size (Size): The size of the product.
        """
        self.name = name
        self.color = color 
        self.size = size

# The old Filter that violates OCP:
class productFilter:
    """Filters products by their attributes. This class violates the Open-Closed Principle."""

    def filter_by_color(self, products, color):
        """Filters products by color.
        
        Args:
            products (list): List of products to filter.
            color (Color): Color to filter by.
            
        Yields:
            Product: A product that matches the color.
        """
        for p in products:
            if p.color == color:
                yield p  
    
    def filter_by_size(self, products, size):
        """Filters products by size.
        
        Args:
            products (list): List of products to filter.
            size (Size): Size to filter by.
            
        Yields:
            Product: A product that matches the size.
        """
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        """Filters products by both size and color.
        
        Args:
            products (list): List of products to filter.
            size (Size): Size to filter by.
            color (Color): Color to filter by.
            
        Yields:
            Product: A product that matches the size and color.
        """
        for p in products:
            if (p.size == size) and (p.color == color):
                yield p

# Enterprise Patterns: Specification Pattern
class Specification(ABC):
    """Base class for a specification to check if a product meets a certain criterion."""

    @abstractmethod
    def is_satisfied(self, item):
        """Determines if an item satisfies the specification.
        
        Args:
            item (Product): The item to check.
            
        Returns:
            bool: True if the item satisfies the specification, False otherwise.
        """
        pass

class Filter(ABC):
    """Base class for filtering items based on a specification."""
    
    @abstractmethod
    def filter(self, items, spec):
        """Filters items based on a specification.
        
        Args:
            items (list): List of items to filter.
            spec (Specification): The specification to use for filtering.
            
        Yields:
            Product: Items that satisfy the specification.
        """
        pass


class ColorSpecification(Specification):
    """Specification to filter by color."""
    
    def __init__(self, color):
        """Initializes the color specification.
        
        Args:
            color (Color): The color to filter by.
        """
        self.color = color
    
    def is_satisfied(self, item):
        """Checks if the item's color matches the specified color.
        
        Args:
            item (Product): The item to check.
            
        Returns:
            bool: True if the item has the specified color, False otherwise.
        """
        return item.color == self.color
    
class SizeSpecification(Specification):
    """Specification to filter by size."""
    
    def __init__(self, size):
        """Initializes the size specification.
        
        Args:
            size (Size): The size to filter by.
        """
        self.size = size

    def is_satisfied(self, item):
        """Checks if the item's size matches the specified size.
        
        Args:
            item (Product): The item to check.
            
        Returns:
            bool: True if the item has the specified size, False otherwise.
        """
        return self.size == item.size
    
class AndSpecification(Specification):
    """Combines two specifications to create a composite specification using logical AND."""
    
    def __init__(self, spec1, spec2):
        """Initializes the composite specification.
        
        Args:
            spec1 (Specification): The first specification.
            spec2 (Specification): The second specification.
        """
        self.spec1 = spec1 
        self.spec2 = spec2
    
    def is_satisfied(self, item):
        """Checks if the item satisfies both specifications.
        
        Args:
            item (Product): The item to check.
            
        Returns:
            bool: True if the item satisfies both specifications, False otherwise.
        """
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item) 
    
    def __and__(self, other):
        """Allows combining specifications using the '&' operator.
        
        Args:
            other (Specification): The other specification to combine with.
            
        Returns:
            AndSpecification: A new composite specification.
        """
        return AndSpecification(self, other)
    

class BetterFilter(Filter):
    """Filters items based on a specification. This adheres to the Open-Closed Principle."""
    
    def filter(self, items, spec):
        """Filters items based on a specification.
        
        Args:
            items (list): List of items to filter.
            spec (Specification): The specification to use for filtering.
            
        Yields:
            Product: Items that satisfy the specification.
        """
        for item in items:
            if spec.is_satisfied(item):
                yield item

# Usage Example:

apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

# Using the old filter (violates OCP):
old_filter = productFilter()
print("Green products (old):")
for product in old_filter.filter_by_color(products, Color.GREEN):
    print(f" - {product.name} is green")

# Using the new filter (adheres to OCP):
better_filter = BetterFilter()

print("Green products (new): ")
green = ColorSpecification(Color.GREEN)
for product in better_filter.filter(products, green):
    print(f" - {product.name} is green")

print("Large products (new): ")
large = SizeSpecification(Size.LARGE)
for product in better_filter.filter(products, large):
    print(f" - {product.name} is large")

print("Large Blue products: ")
large_blue = large & ColorSpecification(Color.BLUE)
for product in better_filter.filter(products, large_blue):
    print(f" - {product.name} is large and blue")
