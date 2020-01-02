import unittest
from highest_product_of_3 import highest_product_of_3


class Test(unittest.TestCase):

    def test_case_1(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_case_2(self):
        actual = highest_product_of_3([3, 1, 2, 6, 8, 7, 5])
        expected = 336
        self.assertEqual(actual, expected)

    def test_case_3(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_case_4(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_case_5(self):
        actual = highest_product_of_3([-5, -1, -3, -2])

        expected = -6
        self.assertEqual(actual, expected)

    def test_case_6(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_case_7(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_case_8(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
