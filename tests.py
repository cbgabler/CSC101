import unittest
import data


class TestData(unittest.TestCase):
    def test_point(self):
        p = data.Point(2, 3, 4)
        self.assertEqual(p.x1, 2)
        self.assertEqual(p.y1, 3)
        self.assertEqual(p.z1, 4)

    def test_vector(self):
        v = data.Vector(1.1, 3.3, 5.5)
        self.assertEqual(v.x1, 1.1)
        self.assertEqual(v.y1, 3.3)
        self.assertEqual(v.z1, 5.5)

    def test_ray(self):
        r = data.Ray((1, 2), (1, 2, 3))
        self.assertEqual(r.pt, (1, 2))
        self.assertEqual(r.dir, (1, 2, 3))

    def test_sphere(self):
        s = data.Sphere((1, 2), 5.643)
        self.assertEqual(s.center, (1, 2))
        self.assertEqual(s.radius, 5.643)


if __name__ == "__main__":
    unittest.main()
