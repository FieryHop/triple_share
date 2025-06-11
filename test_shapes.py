import unittest
import math
from shapes import Circle, Triangle, calculate_area


class TestShapes(unittest.TestCase):

    # Тесты для круга
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    # Тесты для треугольника
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_invalid_triangle_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    def test_negative_triangle_sides(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 3)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_non_right_triangle(self):
        triangle = Triangle(2, 3, 4)
        self.assertFalse(triangle.is_right_triangle())

    # Тест полиморфизма
    def test_calculate_area(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [calculate_area(s) for s in shapes]
        self.assertAlmostEqual(areas[0], math.pi * 4)
        self.assertAlmostEqual(areas[1], 6.0)


if __name__ == '__main__':
    unittest.main()