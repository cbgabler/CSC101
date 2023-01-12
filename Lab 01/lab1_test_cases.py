#
# Test cases example for lab 1.
#

import unittest      # import the module that supports writing unit tests

# Define a class that will be used for these test cases.
# This class will include testing functions.
#
# Much of this code should be viewed as boilerplate for now.
#
class TestsLab1(unittest.TestCase):
   def test_expressions(self):         # Defines one testing function.
      self.assertAlmostEqual(0 + 1, 1)
      self.assertAlmostEqual(2*2, 4)
      self.assertAlmostEqual(19//3,6)
      self.assertAlmostEqual(19/3,6.33, 2)
      self.assertAlmostEqual(19/3.0,6.33, 2)
      self.assertAlmostEqual(19.0/3.0,6.33, 2)
      self.assertAlmostEqual(4*2+27//3+4,21)
      self.assertAlmostEqual(4*(2+27)//3+4,42)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

