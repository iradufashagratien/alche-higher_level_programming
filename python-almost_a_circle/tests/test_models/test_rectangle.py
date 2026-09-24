#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
import sys
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for creating Rectangle instances with valid arguments."""

    def test_two_args(self):
        """Test that Rectangle(1, 2) exists and is created correctly."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_three_args(self):
        """Test that Rectangle(1, 2, 3) exists and is created correctly."""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_four_args(self):
        """Test that Rectangle(1, 2, 3, 4) exists and is created."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_five_args(self):
        """Test that Rectangle(1, 2, 3, 4, 5) exists, including id."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                          (1, 2, 3, 4, 5))

    def test_auto_id(self):
        """Test that ids increment automatically without a given id."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)


class TestRectangleValidation(unittest.TestCase):
    """Tests for the setter validation on Rectangle, exact edge cases."""

    def test_width_string_raises_type_error(self):
        """Test that Rectangle("1", 2) raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_string_raises_type_error(self):
        """Test that Rectangle(1, "2") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_string_raises_type_error(self):
        """Test that Rectangle(1, 2, "3") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_string_raises_type_error(self):
        """Test that Rectangle(1, 2, 3, "4") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_negative_raises_value_error(self):
        """Test that Rectangle(-1, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_negative_raises_value_error(self):
        """Test that Rectangle(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_negative_raises_value_error(self):
        """Test that Rectangle(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_negative_raises_value_error(self):
        """Test that Rectangle(1, 2, 3, -4) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_width_zero_raises_value_error(self):
        """Test that Rectangle(0, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero_raises_value_error(self):
        """Test that Rectangle(1, 0) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_width_setter_negative(self):
        """Test that setting width to -10 after creation raises."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_x_setter_not_int(self):
        """Test that setting x to a dict raises TypeError."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = {}


class TestRectangleArea(unittest.TestCase):
    """Tests for the area method."""

    def test_area_exists(self):
        """Test that area() exists and returns the correct value."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_with_position(self):
        """Test area calculation is unaffected by x/y position."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)


class TestRectangleStr(unittest.TestCase):
    """Tests for the __str__ method."""

    def test_str_exists(self):
        """Test that __str__() exists and returns the correct format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


class TestRectangleDisplay(unittest.TestCase):
    """Tests for the display method, covering every x/y combination."""

    def test_display_exists(self):
        """Test that display() exists and prints something."""
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertNotEqual(captured.getvalue(), "")

    def test_display_without_x_and_y(self):
        """Test display() with default x=0 and y=0."""
        r = Rectangle(2, 3)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = "##\n" * 3
        self.assertEqual(captured.getvalue(), expected)

    def test_display_without_y(self):
        """Test display() with x given but y defaulted to 0."""
        r = Rectangle(3, 2, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = " ###\n" * 2
        self.assertEqual(captured.getvalue(), expected)

    def test_display_with_x_and_y(self):
        """Test display() with both x and y given."""
        r = Rectangle(2, 3, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(captured.getvalue(), expected)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for update using no-keyword arguments."""

    def test_update_id_only(self):
        """Test that update(89) sets only id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        """Test that update(89, 1) sets id and width."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_89_1_2(self):
        """Test that update(89, 1, 2) sets id, width, height."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_89_1_2_3(self):
        """Test that update(89, 1, 2, 3) sets id, width, height, x."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_all_args(self):
        """Test that update(89, 2, 3, 4, 5) sets everything."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                          (89, 2, 3, 4, 5))


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for update using keyword arguments."""

    def test_update_kwargs_id(self):
        """Test that update(**{'id': 89}) sets only id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        """Test that update(**{'id': 89, 'width': 1}) sets both."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{"id": 89, "width": 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_kwargs_multiple(self):
        """Test updating several attributes at once via kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual((r.id, r.width, r.x, r.y), (89, 2, 3, 1))

    def test_kwargs_skipped_if_args_present(self):
        """Test that kwargs are ignored when args are also given."""
        r = Rectangle(10, 10, 10, 10)
        r.update(1, height=99)
        self.assertEqual(r.id, 1)
        self.assertNotEqual(r.height, 99)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method."""

    def test_to_dictionary_exists(self):
        """Test that to_dictionary() exists and has the right keys."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(set(d.keys()),
                          {"id", "width", "height", "x", "y"})

    def test_to_dictionary_round_trip(self):
        """Test that a dictionary can rebuild an equivalent rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
