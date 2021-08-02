""" Play around with unittest library and features"""

from logging import setLogRecordFactory
import unittest

class NamTest1(unittest.TestCase):

    def test_something1(self):
        self.assertEqual(1,1)
        self.assertEqual("thing1","thing1")
        self.assertEqual('foo'.upper(), "FOO")
        self.assertEqual('boo', "boo")
        self.assertGreater(199,100)
        self.assertAlmostEqual(3.33,2.23,3)

    def test_something2(self):
        self.assertTrue(100==100)
        self.assertTrue(10==10)
        self.assertFalse(100==10)


if __name__ == "__main__":
    unittest.main()