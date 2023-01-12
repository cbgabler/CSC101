import unittest
import groups

class TestGroups(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   def test_group(self):
      groupedlist = groups.groups_of_3([1, 2, 3, 4, 5, 6, 7, 8])
      self.assertListEqual(groupedlist, [[1, 2, 3], [4, 5, 6], [7, 8]])

if __name__ == '__main__':
   unittest.main()
