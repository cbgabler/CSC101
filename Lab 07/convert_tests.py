import unittest
import convert

class TestConvert(unittest.TestCase):
   def test_float_default(self):
      self.assertEqual(convert.float_default('180', 9.0), 180.0)
      self.assertEqual(convert.float_default('hello', 0.0), 0.0)



if __name__ == '__main__':
   unittest.main()

