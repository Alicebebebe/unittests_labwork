import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), 9)

    def test_perimeter(self):
        self.assertEqual(perimeter(3), 12)

    def test_zero_side(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == "__main__":
    unittest.main()
