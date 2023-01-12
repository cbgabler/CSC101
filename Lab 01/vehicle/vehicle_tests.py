import unittest
import vehicle

class VehicleTests(unittest.TestCase):
   def test_vehicle(self):
      a = vehicle.vehicle(4, 100, True, 4)
      self.assertEqual(a.door, 4)
      self.assertEqual(a.wheels, 4)
      self.assertTrue(a.roof)
      self.assertEqual(a.fuel, 100)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
