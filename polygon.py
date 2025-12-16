import math

class Polygon:
    def __init__(self, sides):
        self._sides = sides
        self._validate_sides()

    def __is_valid_side(self, side):
        return isinstance(side, (int, float)) and side > 0

    def _validate_sides(self):
        if not all(self.__is_valid_side(side) for side in self._sides):
            raise ValueError("All sides must be positive numbers.")

    def area(self):
        raise NotImplementedError("Area method must be implemented in the derived class.")

    def perimeter(self):
        return sum(self._sides)

    def get_sides(self):
        return self._sides

    def __str__(self):
        return f"{self.__class__.__name__} with sides: {self._sides}"

class Triangle(Polygon):
    def __init__(self, side_a, side_b, side_c):
        super().__init__([side_a, side_b, side_c])
        self.__validate_triangle()

    def __validate_triangle(self):
        a, b, c = self._sides
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Invalid side lengths for a triangle.")

    def area(self):
        s = self.perimeter() / 2
        a, b, c = self._sides
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def __str__(self):
        return f"Triangle (Sides: {self.get_sides()})"

class Rectangle(Polygon):
    def __init__(self, length, width):
        # Encapsulated sides: L, W, L, W
        super().__init__([length, width, length, width])

    def area(self):
        length = self._sides[0]
        width = self._sides[1]
        return length * width

    def __str__(self):
        length = self._sides[0]
        width = self._sides[1]
        return f"Rectangle (Length: {length}, Width: {width})"

class Square(Rectangle):
    # A Square is a specialized Rectangle where length and width are equal.
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        side = self._sides[0]
        return f"Square (Side: {side})"

def calculate_shape_properties(shape):
    print(f"\n--- Results for {shape.__class__.__name__} ---")
    print(f"Sides: {shape.get_sides()}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print(f"Area: {shape.area():.2f}")

def get_float_input(prompt):
    return float(input(prompt))

# --- Main Program with User Input ---
print("### Polygon Calculator (Simple Input) ###")

# 1. Triangle Input
print("\n--- Calculate Triangle ---")
a = get_float_input("Enter Side A: ")
b = get_float_input("Enter Side B: ")
c = get_float_input("Enter Side C: ")
triangle = Triangle(a, b, c)
calculate_shape_properties(triangle)

# 2. Rectangle Input
print("\n--- Calculate Rectangle ---")
length = get_float_input("Enter Length: ")
width = get_float_input("Enter Width: ")
rectangle = Rectangle(length, width)
calculate_shape_properties(rectangle)

# 3. Square Input
print("\n--- Calculate Square ---")
side = get_float_input("Enter Side Length: ")
square = Square(side)
calculate_shape_properties(square)