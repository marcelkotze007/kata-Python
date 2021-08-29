import unittest

from String_Calc import Calculator as Calc

class AddTests(unittest.TestCase):
    def test_Zero(self):
        self.assertEqual(0, Calc(""))

    def test_One(self):
        self.assertEqual(1, Calc("1"))

if __name__ == '__main__':
    unittest.main()