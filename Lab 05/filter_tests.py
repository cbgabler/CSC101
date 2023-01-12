import unittest
import filter
import point

class TestCases(unittest.TestCase):
   def test_positive(self):
      self.assertListEqual(filter.are_positive([-10, 2, 3]), [2, 3])

   def test_greater_than(self):
      self.assertListEqual(filter.are_greater_than([1, 2, 3, 4, 5], 3), [3, 4, 5])

   def test_first_quad(self):
      pt1 = point.Point(1, 2)
      pt2 = point.Point(-2, 3)
      pt3 = point.Point(4, 5)
      pt4 = point.Point(5, 6)
      self.assertEqual(filter.are_in_first_quadrant([pt1]), [pt1])
      self.assertEqual(filter.are_in_first_quadrant([pt2, pt3, pt4]), [pt3, pt4])




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

