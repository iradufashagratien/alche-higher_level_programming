#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for instantiation and id assignment of Base."""

    def test_id_is_public(self):
        """Test that id is a public attribute."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_no_id_increments(self):
        """Test that omitting id auto-increments the counter."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_none_explicit(self):
        """Test that passing id=None still auto-increments."""
        b1 = Base(None)
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)


class TestToJsonString(unittest.TestCase):
    """Tests for the to_json_string static method."""

    def test_none_returns_brackets(self):
        """Test that None returns the string '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list_returns_brackets(self):
        """Test that an empty list returns the string '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """Test that a list of dicts is correctly converted to JSON."""
        list_input = [{"id": 1}, {"id": 2}]
        json_output = Base.to_json_string(list_input)
        self.assertEqual(json.loads(json_output), list_input)


class TestFromJsonString(unittest.TestCase):
    """Tests for the from_json_string static method."""

    def test_none_returns_empty_list(self):
        """Test that None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string_returns_empty_list(self):
        """Test that an empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json_string(self):
        """Test that a valid JSON string round-trips correctly."""
        list_input = [{"id": 1}, {"id": 2}]
        json_string = Base.to_json_string(list_input)
        self.assertEqual(Base.from_json_string(json_string), list_input)


class TestSaveAndLoadFromFile(unittest.TestCase):
    """Tests for save_to_file and load_from_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_rectangle(self):
        """Test that Rectangle instances are saved to Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_none(self):
        """Test that saving None writes an empty list to the file."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test that Rectangle.save_to_file([]) writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file_no_file(self):
        """Test that loading with no existing file returns an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_and_load_round_trip(self):
        """Test that saved and reloaded rectangles match originals."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))

    def test_save_and_load_square(self):
        """Test that saved and reloaded squares match originals."""
        s1 = Square(5)
        Square.save_to_file([s1])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(str(loaded[0]), str(s1))


class TestCreate(unittest.TestCase):
    """Tests for the create class method."""

    def test_create_rectangle(self):
        """Test creating a Rectangle from a dictionary."""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test creating a Square from a dictionary."""
        s1 = Square(5, 1, 2, 99)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()
