import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):

    def __init__(self, side1: float, side2: float, side3: float):
        sides = [side1, side2, side3]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны должны быть положительными числами")

        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            raise ValueError("Недопустимые стороны треугольника")

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_triangle(self, tolerance: float = 1e-6) -> bool:
        sides = sorted([self.side1, self.side2, self.side3])
        return math.isclose(
            sides[0] ** 2 + sides[1] ** 2,
            sides[2] ** 2,
            rel_tol=tolerance
        )
def calculate_area(shape: Shape) -> float:
    return shape.area()