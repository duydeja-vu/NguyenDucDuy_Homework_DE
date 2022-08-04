import unittest
from unittest.mock import patch
from modules.utils.src import numeric_checker


class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_is_integer(self):
        res = numeric_checker.check_is_integer(4)
        self.assertTrue(res)

        res = numeric_checker.check_is_integer(
            4444444444444444444444444444444444444444444444444)
        self.assertTrue(res)

        res = numeric_checker.check_is_integer(-1)
        self.assertTrue(res)

        res = numeric_checker.check_is_integer(0.5)
        self.assertFalse(res)

        res = numeric_checker.check_is_integer("a")
        self.assertFalse(res)

        res = numeric_checker.check_is_integer([1, 2, 3])
        self.assertFalse(res)

        res = numeric_checker.check_is_integer((1, 2, 3))
        self.assertFalse(res)

        res = numeric_checker.check_is_integer({1: "a"})
        self.assertFalse(res)

    def test_check_is_general_numeric(self):
        res = numeric_checker.check_is_general_numeric(4)
        self.assertTrue(res)

        res = numeric_checker.check_is_general_numeric(
            44444444444444444444444444444444444444444444444444444444.5)
        self.assertTrue(res)

        res = numeric_checker.check_is_general_numeric(0.5)
        self.assertTrue(res)

        res = numeric_checker.check_is_general_numeric(-1)
        self.assertTrue(res)

        res = numeric_checker.check_is_general_numeric("a")
        self.assertFalse(res)

        res = numeric_checker.check_is_general_numeric([1, 2, 3])
        self.assertFalse(res)

        res = numeric_checker.check_is_general_numeric((1, 2, 3))
        self.assertFalse(res)

        res = numeric_checker.check_is_general_numeric({1: "a"})
        self.assertFalse(res)

    def test_check_is_list(self):
        res = numeric_checker.check_is_list([1, 2, 3])
        self.assertTrue(res)

        res = numeric_checker.check_is_list((1, 2, 3))
        self.assertFalse(res)

        res = numeric_checker.check_is_list({1: "a"})
        self.assertFalse(res)

        res = numeric_checker.check_is_list(1)
        self.assertFalse(res)

        res = numeric_checker.check_is_list("a")
        self.assertFalse(res)

    def test_check_float_in_range(self):
        res = numeric_checker.check_float_in_range(0.5, 0, 1)
        self.assertTrue(res)

        res = numeric_checker.check_float_in_range(0.5, 1, 2)
        self.assertFalse(res)
