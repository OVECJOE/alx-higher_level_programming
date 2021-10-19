#!/usr/bin/python3
"""A test suite for models/rectangle.py"""

import unittest

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle class in models.rectangle"""

    def test_rectangle_is_subclass_of_base(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_error_raised_when_no_arg_is_passed(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle()

    def test_error_raised_when_one_arg_is_passed(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1)

    def test_width_can_be_set_though_private(self):
        rectangle = Rectangle(1, 2)
        rectangle.width = 2
        self.assertEqual(2, rectangle.width)

    def test_height_can_be_set_though_private(self):
        rectangle = Rectangle(1, 2)
        rectangle.height = 2
        self.assertTrue(2, rectangle.height)

    def test_id_increment_by_one_if_not_given(self):
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 2)
        self.assertEqual(rect2.id - rect1.id, 1)
