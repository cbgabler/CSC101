import conditional
import unittest

class TestCases(unittest.TestCase):
   def test_max_101(self):
      self.assertEqual(conditional.max_101(2, 6), 6)
      self.assertTrue(conditional.max_101(4, 1), 4)

   def test_max_of_three(self):
      self.assertTrue(conditional.max_of_three(1, 2, 3), 3)
      self.assertTrue(conditional.max_of_three(1, 3, 2), 3)
      self.assertTrue(conditional.max_of_three(3, 2, 1), 3)

   def test_rental(self):
      self.assertEqual(conditional.rental_late_fee(0), 0)
      self.assertEqual(conditional.rental_late_fee(9), 5)
      self.assertEqual(conditional.rental_late_fee(15), 7)
      self.assertEqual(conditional.rental_late_fee(24), 19)
      self.assertEqual(conditional.rental_late_fee(50), 100)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

