import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(10, 5), 50)

    def test_perimeter(self):
        self.assertEqual(perimeter(10, 5), 30)

    def test_zero_side(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(perimeter(10, 0), 20)

    def test_square_rectangle(self):
        self.assertEqual(area(10, 10), 100)
        self.assertEqual(perimeter(10, 10), 40)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-1, 5)
        with self.assertRaises(ValueError):
            perimeter(5, -1)


if __name__ == "__main__":
    unittest.main()
