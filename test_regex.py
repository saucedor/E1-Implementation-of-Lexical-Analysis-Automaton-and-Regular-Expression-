import unittest
# Load the main code file.
from regex import test_regex  

# Import the function to be tested
class TestMatchesPattern(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(test_regex(''))

    def test_valid_strings(self):
        # length 1
        self.assertTrue(test_regex('0'))
        self.assertTrue(test_regex('1'))
        self.assertTrue(test_regex('2'))

        # length 2
        self.assertTrue(test_regex('01'))
        self.assertTrue(test_regex('12'))
        self.assertTrue(test_regex('20'))

        # length 3 
        self.assertTrue(test_regex('012'))
        self.assertTrue(test_regex('021'))
        self.assertTrue(test_regex('102'))
        self.assertTrue(test_regex('201'))
        self.assertTrue(test_regex('120'))

        # length 4-6
        self.assertTrue(test_regex('0120'))
        self.assertTrue(test_regex('1021'))
        self.assertTrue(test_regex('1201'))
        self.assertTrue(test_regex('2012'))
        self.assertTrue(test_regex('2120'))
        self.assertTrue(test_regex('1212'))
        self.assertTrue(test_regex('012012'))
        self.assertTrue(test_regex('201201'))
        self.assertTrue(test_regex('202120'))

        # additional tests with long but valid sequences
        self.assertTrue(test_regex('012012012'))
        self.assertTrue(test_regex('201201201'))
        self.assertTrue(test_regex('120120120'))
        self.assertTrue(test_regex('021021021'))

    def test_invalid_strings(self):
        self.assertFalse(test_regex('1101'))
        self.assertFalse(test_regex('1122'))
        self.assertFalse(test_regex('1011'))
        self.assertFalse(test_regex('1012'))
        self.assertFalse(test_regex('2221012000'))
        self.assertFalse(test_regex('0001122111'))
        self.assertFalse(test_regex('201101000'))
        self.assertFalse(test_regex('0122201122'))
        self.assertFalse(test_regex('01101011'))
        self.assertFalse(test_regex('022110110'))

if __name__ == '__main__':
    unittest.main()