import unittest
from making_change import change_possibilities


class Test(unittest.TestCase):

    def test_case_1(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_case_2(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_case_3(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_case_4(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_case_5(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_case_6(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
