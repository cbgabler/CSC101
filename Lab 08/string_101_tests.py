import unittest
import string_101

class TestString(unittest.TestCase):
   def test_str_rot_13(self):
      self.assertEqual(string_101.str_rot_13('Hello there'), 'Uryyb gurer')
      self.assertEqual(string_101.str_rot_13('My Name is Jeff'), 'Zl Anzr vf Wrss')

   def test_str_translate_101(self):
      self.assertEqual(string_101.str_translate_101('abcdcba', 'a', 'x'), 'xbcdcbx')
      self.assertEqual(string_101.str_translate_101('hello there', 'e', 'a'), 'hallo thara')


if __name__ == '__main__':
   unittest.main()
