import unittest
import objects
import funcs_objects

class TestCases(unittest.TestCase):
   def test_cases(self):
      a = objects.point(1, 5)
      self.assertEqual(a.x, 1)
      self.assertEqual(a.y, 5)
      b = objects.circle(1, (2, 4))
      self.assertEqual(b.radius, 1)
      self.assertEqual(b.center, (2, 4))

   def test_distance(self):
      p1 = objects.point(1, 5)
      p2 = objects.point(2, 6)
      d = funcs_objects.distance(p1, p2)
      self.assertAlmostEqual(d, 1.414, 3)
      return d

   def test_circles_overlap(self):
      c1 = objects.point(1, 2)
      c2 = objects.point(2, 4)
      r1 = 1
      r2 = 3
      r = funcs_objects.radii(r1, r2)
      c = funcs_objects.center(c1, c2)
      self.assertAlmostEqual(c, 2.236, 3)
      self.assertEqual(r, 4)
      self.assertTrue(c < r)
      self.assertFalse(c >= r)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

