#!/usr/bin/python3
"""Test cases for models/base.py"""
from turtle import position
import unittest
from unittest.mock import patch
from io import StringIO

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Test suite for the Base class in models.base"""

    def setUp(self):
        """SetUp for the TestBase class"""
        self.polygon = Base()
        self.polygon_1 = Base(1)
        self.polygon_2 = Base()
        self.polygon_3 = Base()

    # def test_miscellaneous(self):
    #     self.assertEqual(self.polygon.id + 1, self.polygon_2.id)
    #     self.assertEqual('0x11', Base('0x11').id)
    #     self.assertFalse('nb_objects' in dir(Base))
    #     self.assertFalse('__nb_objects' in dir(Base))
    #     self.assertIsNotNone(Base(None).id)
    #     self.assertNotEqual(None, Base(None))

    def test_base_objs_of_same_id_are_not_the_same_obj(self):
        self.assertFalse(self.polygon is self.polygon_1)

    def test_base_objs_without_arg_increment_by_one(self):
        self.assertEqual(self.polygon_2.id - self.polygon.id,
                         self.polygon_3.id - self.polygon_2.id)

    def test_that_the_first_and_third_base_obj_ids_difference(self):
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


class TestBaseMethods(unittest.TestCase):
    """Test suite for the methods of the Base class"""

    def test_to_json_string(self):
        """Tests the Base.to_json_string()"""
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{}]), '[{}]')
        self.assertEqual(Base.to_json_string([{'width': 3}]),
        '[{"width": 3}]')
        with self.assertRaises(TypeError):
            Base.to_json_string()
    
    def test_from_json_string(self):
        """Test suite for the methods of the Base class"""
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string([], 12)
        
        self.assertEqual(Base.from_json_string('"Batman"'), "Batman")
        self.assertEqual(Base.from_json_string('null'), None) # since None == null in JSON
        self.assertEqual(Base.from_json_string(str()), [])
        self.assertEqual(
            Base.from_json_string('[1, 2, "0x3", 4]'),
            [1, 2, '0x3', 4]
        )
        self.assertEqual(
            Rectangle.from_json_string(
                '[{"width": 3, "height": 2, "x": 3, "y": 5}]'
            ),
            [{"width": 3, "height": 2, "x": 3, "y": 5}]
        )


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

    def test_miscelleneous(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            rect = Rectangle(2, 0)

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

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.r1.update(2, 3, 2, 2, 2)
            self.r1.display()
            self.assertEqual(fake_stdout.getvalue(), "\n\n  ###\n  ###\n")

    def test_str(self):
        string = str(self.r1)

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            print(self.r1, end="")
            self.assertEqual(fake_stdout.getvalue(), string)

    def test_update(self):
        """Tests the update function in the Base class.
        """
        polygon = Square(5)
        # region valid arguments
        polygon.update(1)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 5)
        polygon.update(1, 7)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        polygon.update(1, 7, 5)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(1, 7, 5, 2)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, 15)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region *args with **kwargs
        polygon = Square(5)
        polygon.update(1, size=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 5)
        polygon.update(1, size=[12, ])
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 5)
        polygon.update(1, 7, size=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        polygon.update(1, 7, size={12, })
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        polygon.update(1, 7, 5, size=12, x=17)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(1, 7, 5, size=12, x='17')
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(1, 7, 5, 2, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, size=12, x=17, y=1.8)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, size=12, x=17, y='18')
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, 15, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, 15, size=12, x=17, y=(18, 54))
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size=None, x={'f': 17}, y=None)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size='12', x=1.7, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size='12', x=1.7, y=18, bee=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region **kwargs and no *args
        polygon = Square(5)
        id_init = polygon.id
        polygon.update(id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 5)
        # id has no get/set function
        polygon.update(id=None)
        self.assertEqual(polygon.id, None)
        self.assertEqual(polygon.size, 5)
        polygon.update(size=7, id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        polygon.update(x=5, size=7, id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(x=5, size=7, id='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region update should only update supported attributes
        polygon.update(x=5, size=7, id='35', y=2, foo=63)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        with self.assertRaises(AttributeError):
            print(polygon.foo == 63)
        polygon.update(x=5, width=425, id='35', y=2, foo=63)
        self.assertFalse(polygon.size == 425)
        self.assertFalse(polygon.width == 425)
        self.assertFalse(polygon.height == 425)
        # endregion
        # region update does not recognize width and height
        polygon.update(x=5, size=7, width=35, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, width='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, width=None, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, width=True, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height=35, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height=None, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height=True, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region update allows validations to be performed
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(size=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(size=0, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(size=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(x=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(y=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        # endregion
