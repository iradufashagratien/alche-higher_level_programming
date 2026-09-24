#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for creating Rectangle instances."""

    def test_basic_instantiation(self):
        """Test that width, height, x, y are assigned correctly."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_all_args(self):
        """Test instantiation with all five arguments given."""
        r = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                          (10, 2, 1, 3, 12))

    def test_auto_id(self):
        """Test that ids increment automatically without a given id."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)


class TestRectangleValidation(unittest.TestCase):
    """Tests for the setter validation on Rectangle."""

    def test_width_not_int_raises_type_error(self):
        """Test that a non-integer width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_width_zero_raises_value_error(self):
        """Test that a width of 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_width_negative_raises_value_error(self):
        """Test that a negative width raises ValueError."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_x_not_int_raises_type_error(self):
        """Test that a non-integer x raises TypeError."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = {}

    def test_y_negative_raises_value_error(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)


class TestRectangleArea(unittest.TestCase):
    """Tests for the area method."""

    def test_area_basic(self):
        """Test area calculation for a simple rectangle."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_with_position(self):
        """Test area calculation is unaffected by x/y position."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)


class TestRectangleStr(unittest.TestCase):
    """Tests for the __str__ method."""

    def test_str_format(self):
        """Test that __str__ returns the correct format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for update using no-keyword arguments."""

    def test_update_id_only(self):
        """Test that update with one argument sets only id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_all_args(self):
        """Test that update with five arguments sets everything."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                          (89, 2, 3, 4, 5))


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for update using keyword arguments."""

    def test_update_kwargs(self):
        """Test that update with keyword arguments works correctly."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

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

    def test_to_dictionary_keys(self):
        """Test that to_dictionary returns all five expected keys."""
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
