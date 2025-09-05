import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper2(self):
        self.assertTrue('FOO'.isupper(), 'True')

if __name__ == '__main__':
    unittest.main()