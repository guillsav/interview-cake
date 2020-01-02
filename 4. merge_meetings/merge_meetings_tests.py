import unittest
from merge_meetings import merge_mettings


class Test(unittest.TestCase):

    def test_case_1(self):
        actual = merge_mettings([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_case_2(self):
        actual = merge_mettings([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_case_3(self):
        actual = merge_mettings([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_case_4(self):
        actual = merge_mettings([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_case_5(self):
        actual = merge_mettings([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_case_6(self):
        actual = merge_mettings([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_case_7(self):
        actual = merge_mettings([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_case_8(self):
        actual = merge_mettings([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
