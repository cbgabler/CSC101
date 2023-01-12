import unittest
import line

class LineTests(unittest.TestCase):
   def test_line(self):
      # Add code here.
      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.
      a = line.line(1, 2, 3, 4)
      self.assertEqual(a.x1, 1)
      self.assertEqual(a.y1, 2)
      self.assertEqual(a.x2, 3)
      self.assertEqual(a.y2, 4)

   def test_line_again(self):
      a = line.line(12, 16, 20, 24)
      self.assertEqual(a.x1, 12)
      self.assertEqual(a.y1, 16)
      self.assertEqual(a.x2, 20)
      self.assertEqual(a.y2, 24)


   # Run the unit tests.
if __name__ == '__main__':
   unittest.main()
