import math
import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(5), 25 * math.pi)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)

    def test_zero_radius(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == "__main__":
    unittest.main()
