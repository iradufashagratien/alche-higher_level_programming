#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
import os
from models.square import Square
from models.rectangle import Rectangle


class TestSquareInstantiation(unittest.TestCase):
    """Tests for creating Square instances with valid arguments."""

    def test_is_rectangle_subclass(self):
        """Test that Square inherits from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_one_arg(self):
        """Test that Square(1) exists and sets width/height equal."""
        s = Square(1)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 0, 0))

    def test_two_args(self):
        """Test that Square(1, 2) exists, size and x set correctly."""
        s = Square(1, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 0))

    def test_three_args(self):
        """Test that Square(1, 2, 3) exists, size, x, and y set."""
        s = Square(1, 2, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 3))

    def test_four_args(self):
        """Test that Square(3, 1, 3, 12) exists, including id."""
        s = Square(3, 1, 3, 12)
        self.assertEqual((s.x, s.y, s.id), (1, 3, 12))

    def test_width_height_equal_size(self):
        """Test that width and height both equal the given size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)


class TestSquareValidation(unittest.TestCase):
    """Tests confirming Square reuses Rectangle's validation exactly."""

    def test_size_string_raises_type_error(self):
        """Test that Square("1") raises TypeError."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_string_raises_type_error(self):
        """Test that Square(1, "2") raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_string_raises_type_error(self):
        """Test that Square(1, 2, "3") raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_zero_raises_value_error(self):
        """Test that Square(0) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative_raises_value_error(self):
        """Test that Square(-1) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_negative_raises_value_error(self):
        """Test that Square(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative_raises_value_error(self):
        """Test that Square(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)


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


class TestSquareCreate(unittest.TestCase):
    """Tests for the create class method on Square."""

    def test_create_id_only(self):
        """Test Square.create(**{'id': 89}) exists."""
        s = Square.create(**{"id": 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Test Square.create(**{'id': 89, 'size': 1}) exists."""
        s = Square.create(**{"id": 89, "size": 1})
        self.assertEqual((s.id, s.size), (89, 1))


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


class TestSquareSaveAndLoadFromFile(unittest.TestCase):
    """Tests for save_to_file and load_from_file on Square."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_none(self):
        """Test that Square.save_to_file(None) writes an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test that Square.save_to_file([]) writes an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one_square(self):
        """Test that Square.save_to_file([Square(1)]) writes a file."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file_no_file(self):
        """Test that load_from_file with no file returns an empty list."""
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_with_file(self):
        """Test that load_from_file returns saved squares correctly."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(s1))
        self.assertEqual(str(loaded[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
