#!/usr/bin/python3
"""A test suite for models/rectangle.py"""

import unittest
from unittest.mock import patch
from io import StringIO

from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstantiationAndAttributes(unittest.TestCase):
    """Test suite for Rectangle instantiation and attributes in
    models.rectangle"""

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

    def test_error_is_raised_if_width_not_int(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(3.2, 2)

    def test_error_is_raised_if_height_not_int(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "s")

    def test_error_is_raised_if_x_not_int(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, True)

    def test_error_is_raised_if_y_not_int(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, y="g")

    def test_width_not_under_nor_equals_0(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 3)

    def test_height_not_under_nor_equals_0(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 0)

    def test_x_not_under_0(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 1, -1)

    def test_y_not_under_0(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 1, y=-1)


class TestRectangleMethods(unittest.TestCase):
    """A test suite for the Rectangle methods"""

    def setUp(self):
        """Set up instances and data for this class"""
        self.r1 = Rectangle(3, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(8, 7, 0, 0, 12)

    def test_area(self):
        self.assertEqual(self.r1.area(), 6)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 56)

    def test_display(self):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.r1.display()
            self.assertEqual(fake_stdout.getvalue(), '###\n###\n')

    def test_str(self):
        string = str(self.r1)

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            print(self.r1, end="")
            self.assertEqual(fake_stdout.getvalue(), string)

    def test_update(self):
        self.r1.update(23, 2, 3, 4)

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            print(self.r1, end="")
            self.assertEqual(fake_stdout.getvalue(), str(self.r1))
