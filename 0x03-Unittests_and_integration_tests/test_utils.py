#!/usr/bin/env python3

"""
Test suite for utils module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with valid inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test access_nested_map function with invalid inputs.
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """
    Test case for get_json function.
    """

    @patch('requests.get')
    def test_get_json(self, mock_get):
        """
        Test get_json function with valid input.
        """
        mock_get.return_value.json.return_value = {"payload": True}
        self.assertEqual(get_json("http://example.com"), {"payload": True})
        mock_get.assert_called_once_with("http://example.com")

    @patch('requests.get')
    def test_get_json_payload_false(self, mock_get):
        """
        Test get_json function with invalid input.
        """
        mock_get.return_value.json.return_value = {"payload": False}
        self.assertEqual(get_json("http://holberton.io"), {"payload": False})
        mock_get.assert_called_once_with("http://holberton.io")

class TestMemoize(unittest.TestCase):
    """
    Test case for memoize function.
    """

    def test_memoize(self):
        """
        Test memoize function with valid input.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_class = TestClass()
        with patch.object(test_class, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_a_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
