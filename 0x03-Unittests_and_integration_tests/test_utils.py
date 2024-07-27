#!/usr/bin/env python3

"""
Test utilities module.

This module provides tests for the utilities module.
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
        self.assertEqual(get_json("http://example.com"), {"payload": False})
        mock_get.assert_called_once_with("http://example.com")

class TestMemoize(unittest.TestCase):
    """
    Test case for memoize function.
    """

    def test_memoize(self):
        """
        Test memoize function with valid input.
        """
        def add(a, b):
            return a + b
        memoized_add = memoize(add)
        self.assertEqual(memoized_add(1, 2), 3)
        self.assertEqual(memoized_add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
