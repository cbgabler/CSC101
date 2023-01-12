import unittest
import map
import point


class TestCases(unittest.TestCase):
   def test_square(self):
      self.assertListEqual(map.square_all([4, 1, 2]), [16, 1, 4])

   def test_add_n_all(self):
      self.assertListEqual(map.add_n_all([1, 2, 3, 4], 2), [3, 4, 5, 6])

   def test_distance_all(self):
      pt1 = point.Point(3, 4)
      pt2 = point.Point(5, 12)
      pt3 = point.Point(6, 8)
      self.assertEqual(map.distance_all([pt1, pt2, pt3]), [5, 13, 10])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

