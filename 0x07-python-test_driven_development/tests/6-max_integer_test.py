#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_max_at_beginning(self):
        """Checks if the max is at the beginning"""
        ints = [2, -1, -3]
        self.assertEqual(max_integer(ints), ints[0])

    def test_a_singleton(self):
        """if list is singleton, checks if the first element is returned"""
        s = [2]
        self.assertEqual(max_integer(s), s[0])

    def test_ints_and_floats(self):
        """Test a list of ints and floats"""
        ints_and_floats = [1, 23, 23.5, 3]
        self.assertEqual(max_integer(ints_and_floats), 23.5)

    def test_ordered_list(self):
        """Tests an ordered list"""
        ordered_list = [1, 2, 3, 5]
        self.assertEqual(max_integer(ordered_list), 5)

    def test_unordered_list(self):
        """Tests a list that is unordered"""
        unordered_list = [3, 2, 1, 5, -6]
        self.assertEqual(max_integer(unordered_list), 5)

    def test_floats(self):
        """Tests a list of floats"""
        floats = [1.2, 3.4, 5.4]
        self.assertEqual(max_integer(floats), 5.4)

    def test_large_list(self):
        """Tests a list that is large"""
        large_list = list(range(2, 10000, 3)) + list(range(3000, 100, -2))
        self.assertEqual(max_integer(large_list), max(large_list))

    def test_string(self):
        """Tests a string"""
        string = "Holberton School"
        self.assertEqual(max_integer(string), 't')

    def test_list_of_strings(self):
        """Tests a list of strings"""
        list_of_strings = ["holberton", "school", "software", "engineering"]
        self.assertEqual(max_integer(list_of_strings), 'software')

if __name__ == "__main__":
    unittest.main()
