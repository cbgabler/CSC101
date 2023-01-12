import unittest
import logic

class TestCases(unittest.TestCase):
   def test_even(self):
      self.assertTrue(logic.is_even(6))
      self.assertFalse(logic.is_even(7))

   def test_interval(self):
      self.assertTrue(logic.is_an_interval(6))
      self.assertFalse(logic.is_an_interval(1743))


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

