import unittest
import char

class TestChar(unittest.TestCase):
   def test_lower(self):
      self.assertTrue(char.is_lower_101('a'))
      self.assertFalse(char.is_lower_101('A'))

   def test_char_rot_13(self):
      self.assertEqual(char.char_rot_13('A'), 'N')
      self.assertEqual(char.char_rot_13('x'), 'k')
      self.assertEqual(char.char_rot_13('@'), '@')


if __name__ == '__main__':
   unittest.main()

