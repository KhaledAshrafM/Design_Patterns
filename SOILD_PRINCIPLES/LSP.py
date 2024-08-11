# Liskov Substitution Principle (LSP):
# Subclasses should be substitutable for their base classes without affecting the correctness of the program.
# This means that, if class B is a subclass of class A, we should be able to pass an object of class B to any method
# that expects an object of class A, and the method should behave correctly without any unexpected results.

# Example:

class Rectangle:
    """Represents a rectangle shape with width and height."""

    def __init__(self, width, height):
        """Initializes a new rectangle with the specified width and height.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self._width = width
        self._height = height
    
    @property
    def area(self):
        """Calculates and returns the area of the rectangle.
        
        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return f"Width: {self.width}, Height: {self.height}"
    
    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        self._width = value
        
    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        self._height = value

class Square(Rectangle):
    """Represents a square, which is a special case of a rectangle where width equals height."""

    def __init__(self, size):
        """Initializes a new square with the specified size for both width and height.
        
        Args:
            size (int): The size of the square (both width and height).
        """
        Rectangle.__init__(self, size, size)
        
    @Rectangle.width.setter
    def width(self, value):
        """Sets both the width and height of the square to the same value."""
        self._width = self._height = value
        
    @Rectangle.height.setter
    def height(self, value):
        """Sets both the height and width of the square to the same value."""
        self._height = self._width = value

def use_it(rc):
    """A function that works with any rectangle-like object and expects to manipulate its height.
    
    Args:
        rc (Rectangle): A rectangle-like object.
    """
    w = rc.width
    rc.height = 10
    expected = w * 10
    print(f"Expected area: {expected}, but got: {rc.area}")

# Usage Example:

rc = Rectangle(2, 3)
use_it(rc)  # This works as expected.

sq = Square(5)
use_it(sq)  # This violates the Liskov Substitution Principle because setting the height affects the width.
