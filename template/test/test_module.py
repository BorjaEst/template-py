"""Unittest module. Note that unit tests is designed to test the
internal structure of the program, therefore knowledge about the
design can be (and it is recommended to be) used.

This includes for example, the edit and assert of private module
and class variables.

Also note that the usage of files for setup, might produce files
on the root directory when a test fails if a dir mockup is not
used.

"""

import os
import unittest

from template import module


class TestsGroup001(unittest.TestCase):
    """Group to test the main database calls."""

    def setUp(self):
        """DB contruction with some key-values."""
        database = module.Database()
        database._dict = {'a': 1, 'b': 2}
        self.db = database

    def test_str(self):
        """Tests the string method."""
        self.assertEqual(str(self.db), "a:1\nb:2")

    def test_property_size(self):
        """Tests the property size."""
        self.assertEqual(self.db.size, 2)

    def test_property_keys(self):
        """Tests the property keys."""
        self.assertEqual(self.db.keys, ['a', 'b'])

    def test_add_key_value(self):
        """Tests the method to add a key value."""
        self.assertEqual(self.db.add('c', 1), None)
        self.assertEqual(self.db._dict, {'a': 1, 'b': 2, 'c': 1})

    def test_get_key_value(self):
        """Tests the method to get a key value."""
        self.assertEqual(self.db.get('a'), 1)
        self.assertEqual(self.db.get('b'), 2)

    def test_delete_key(self):
        """Tests the method to delete a key"""
        self.assertEqual(self.db.delete('a'), None)
        self.assertEqual(self.db._dict, {'b': 2})


class TestsGroup002(unittest.TestCase):
    """Group to test the saving of the database."""

    def setUp(self):
        """DB contruction with some key-values."""
        database = module.Database()
        database._dict = {'a': 1, 'b': 2}
        self.db = database

    def tearDown(self):
        """DB file destructor with some key-values."""
        os.remove("test_db1.mydb")

    def test_save_db(self):
        """Tests the method to delete a key"""
        self.assertNotIn("test_db1.mydb", os.listdir())
        self.assertEqual(self.db.save("test_db1.mydb"), None)
        self.assertIn("test_db1.mydb", os.listdir())


class TestsGroup003(unittest.TestCase):
    """Group to test the correct loading of a database."""

    def setUp(self):
        """DB file contruction with some key-values."""
        database = module.Database()
        database._dict = {'a': 1, 'b': 2}
        database.save("test_db2.mydb")

    def tearDown(self):
        """DB file destructor with some key-values."""
        os.remove("test_db2.mydb")

    def test_load_db(self):
        """Tests the method to delete a key"""
        db = module.Database()
        self.assertEqual(db.load("test_db2.mydb"), None)
        self.assertEqual(db._dict, {'a': 1, 'b': 2})
