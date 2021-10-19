#!/usr/bin/python3
"""Test cases for models/base.py"""
import unittest

from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Test suite for the Base class in models.base"""
    
    def setUp(self):
        """SetUp for the TestBase class"""
        self.polygon = Base()
        self.polygon_1 = Base(1)
        self.polygon_2 = Base()
        self.polygon_3 = Base()

    def test_base_objs_of_same_id_are_not_the_same_obj(self):
        self.assertFalse(self.polygon is self.polygon_1)

    def test_base_objs_without_arg_increment_by_one(self):
        self.assertEqual(self.polygon_2.id - self.polygon.id, self.polygon_3.id - self.polygon_2.id)

    def test_that_the_first_and_third_base_obj_ids_difference_is_1_though_a_base_obj_with_given_id_is_in_between(self):
        self.assertTrue(self.polygon_2.id - self.polygon.id == 1)

    def test_when_arg_given_is_bool(self):
        b = Base(True)
        self.assertEqual(b.id, True)
        b1 = Base(False)
        self.assertEqual(b1.id, False)

    def test_that_error_is_raised_when_more_than_1_arg_passed(self):
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_that_no_error_is_raised_if_arg_is_a_str(self):
        b = Base("1")
        self.assertIsInstance(b.id, str)

    def test_that_error_is_raised_if_arg_is_a_list(self):
        b = Base(list("base"))
        self.assertIsInstance(b.id, list)

    def test_that_error_is_raised_when_accessing_private_class_attribute(self):
        with self.assertRaises(AttributeError):
            self.polygon.__nb_objects += 1
