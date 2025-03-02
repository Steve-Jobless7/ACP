class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def perimeter(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Formula for the area of a rectangle
        return self.width * self.height

    def perimeter(self):
        # Formula for the perimeter of a rectangle
        return 2 * (self.width + self.height)

# Subclass for Square (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side_length):
        # A square is a special case of a rectangle where width = height
        super().__init__(side_length, side_length)

    def area(self):
        # Formula for the area of a square
        return self.width ** 2

    def perimeter(self):
        # Formula for the perimeter of a square
        return 4 * self.width

# Main function to demonstrate the geometry shapes and their methods
def demonstrate_shapes():
    # Create objects for Rectangle and Square
    rectangle = Rectangle(4, 6)
    square = Square(5)

    # Display results for Rectangle
    print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")

    # Display results for Square
    print(f"Square - Area: {square.area()}, Perimeter: {square.perimeter()}")

# Example usage
if __name__ == "__main__":
    demonstrate_shapes()