# Shapes

Python Package for Geometric Shapes.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Shapes.

```bash
pip install -e .


# Usage

from src.shapes.circle import Circle
from src.shapes.rectangle import Rectangle

# Create instances of geometric shapes
circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=3)

# Print information about the shapes
print(circle)
print(rectangle)

# Calculate area and perimeter
area_circle = circle.area()
perimeter_rectangle = rectangle.perimeter()

print(f"Area of the circle: {area_circle}")
print(f"Perimeter of the rectangle: {perimeter_rectangle}")
