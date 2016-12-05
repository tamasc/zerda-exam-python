import unittest
from third import count_letter_in_string

class Test_count_letter_in_string(unittest.TestCase):

    def setUp(self):
        self.test_string = 'aaaaaaaaaaab   aaaaaabaaaaaaaaakkkbaaaaaa6'
        self.test_empty_string = ''
        self.test_list = [3, 'karalabe' ,3, 6, 4]
        self.test_int = 6

    def test_count_b_in_string(self):
        self.assertEqual(count_letter_in_string(self.test_string, 'b'), 3)

    def test_count_y_in_string(self):
        self.assertEqual(count_letter_in_string(self.test_string, 'y'), 0)

    def test_count_int_in_string(self):
        self.assertEqual(count_letter_in_string(self.test_string, self.test_int), 0)

    def test_count_list_in_string(self):
        self.assertEqual(count_letter_in_string(self.test_string, self.test_list), 0)

    def test_count_b_in_list(self):
        self.assertEqual(count_letter_in_string(self.test_list, 'b'), 0)

    def test_count_b_in_int(self):
        self.assertEqual(count_letter_in_string(self.test_int, 'b'), 0)

if __name__ == '__main__':
    unittest.main()
