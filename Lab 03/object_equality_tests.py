import unittest
import point


class TestCases(unittest.TestCase):
   def test_point_one(self):
      pt = point.Point(1, 2)
      self.assertAlmostEqual(pt.x, 1)
      self.assertAlmostEqual(pt.y, 2)


   def test_point_two(self):
      pt = point.Point(-4.7, 19.2)
      self.assertAlmostEqual(pt.x, -4.7)
      self.assertAlmostEqual(pt.y, 19.2)


   def test_equality(self):
      pt1 = point.Point(1, 2)
      pt2 = point.Point(1, 2)
      pt3 = point.Point(3, 4)
      pt4 = point.Point(4, 5)
      self.assertEqual(pt1 == pt2, True)
      self.assertEqual(pt3, pt4, False)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

