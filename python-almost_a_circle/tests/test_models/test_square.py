#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquareInstantiation(unittest.TestCase):
    """Tests for creating Square instances."""

    def test_is_rectangle_subclass(self):
        """Test that Square inherits from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_width_height_equal_size(self):
        """Test that width and height both equal the given size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_position_args(self):
        """Test that x, y, and id are assigned correctly."""
        s = Square(3, 1, 3, 12)
        self.assertEqual((s.x, s.y, s.id), (1, 3, 12))


class TestSquareValidation(unittest.TestCase):
    """Tests confirming Square reuses Rectangle's validation."""

    def test_non_int_size_raises_type_error(self):
        """Test that a non-integer size raises TypeError."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_negative_size_raises_value_error(self):
        """Test that a negative size raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-5)


class TestSquareStr(unittest.TestCase):
    """Tests for the __str__ method."""

    def test_str_format(self):
        """Test that __str__ returns the correct Square format."""
        s = Square(5, 1, 2, 99)
        self.assertEqual(str(s), "[Square] (99) 1/2 - 5")


class TestSquareSize(unittest.TestCase):
    """Tests for the size getter and setter."""

    def test_size_getter(self):
        """Test that the size getter returns the width value."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter_updates_width_height(self):
        """Test that setting size updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_validation(self):
        """Test that the size setter raises TypeError on bad input."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for update using no-keyword arguments."""

    def test_update_all_args(self):
        """Test update with id, size, x, y as positional arguments."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for update using keyword arguments."""

    def test_update_kwargs(self):
        """Test update using size and id as keyword arguments."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual((s.id, s.size, s.y), (89, 7, 1))


class TestSquareToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method."""

    def test_to_dictionary_keys(self):
        """Test that to_dictionary returns exactly the expected keys."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "size", "x", "y"})

    def test_to_dictionary_round_trip(self):
        """Test that a dictionary can rebuild an equivalent square."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
