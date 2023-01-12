import unittest
import funcs


class TestCases(unittest.TestCase):
    def test_square(self):
        self.assertEqual(funcs.f(1), 9)

    def test_f(self):
        self.assertEqual(funcs.g(2, 4), 20)

    def test_hyp(self):
        self.assertEqual(funcs.hypotenuse(3, 4), 5)

    def test_is_positive(self):
        n=1
        funcs.is_positive(n)
        self.assertTrue(n > 0)
        self.assertFalse(n < 0)



# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
