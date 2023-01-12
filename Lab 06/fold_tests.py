import unittest
import fold
import point

class TestCases(unittest.TestCase):
   def test_sum(self):
      self.assertEqual(fold.add_all([1, 2, 3]), 6)

   def test_smallest(self):
      self.assertEqual(fold.index_of_smallest([1, 2, 3]), 1)

   def test_origin(self):
      pt1 = point.Point(1, 1)
      pt2 = point.Point(2, 2)
      pt3 = point.Point(3, 3)
      self.assertEqual(fold.nearest_origin([pt1, pt2, pt3]), [1, 1])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

