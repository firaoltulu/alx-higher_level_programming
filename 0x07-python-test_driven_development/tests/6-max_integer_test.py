#!/usr/bin/python3
"""This is a Unit test for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a unit test class for max_integer."""
    def test_module_docstring(self):
        """Tests for module docsting"""
        one = __import__('6-max_integer').__doc__
        self.assertTrue(len(one) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        two = max_integer.__doc__
        self.assertTrue(len(two) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        three = []
        self.assertIsNone(max_integer(three))

    def test_no_args(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""
        four = [1]
        self.assertEqual(max_integer(four), 1)

    def test_positive_end(self):
        """Tests for all positive with max at end"""
        five = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(five), 50)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        six = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(six), 360)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        seven = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(seven), 200)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        eight = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(eight), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        nine = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(nine), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        ten = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(ten)

if __name__ == "__main__":
    unittest.main()
