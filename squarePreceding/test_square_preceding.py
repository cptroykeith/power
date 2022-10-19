from multiprocessing.sharedctypes import Value
from optparse import Values
import unittest
from square_preceding import square

class Testsquare_preceding(unittest.TestCase):
    def test_value_empty(self):
        self.assertTrue(Value)

    def test_value_positive(self):
        self.assertTrue(Values)

    def test_value_int(self):
        self.assertTrue(Values)

if __name__ == '__main__':
    unittest.main()
