#!/usr/bin/env python3

"""
Test client module.

This module provides tests for the client module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient
from fixtures import load_fixture

class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", "google.json"),
        ("facebook", "facebook.json"),
    ])
    def test_public_repos(self, org, fixture_name):
        """
        Test public_repos property with valid inputs.
        """
        client = GithubOrgClient(org)
        expected = load_fixture(fixture_name)
        self.assertEqual(client.public_repos, expected)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test has_license method with valid inputs.
        """
        client = GithubOrgClient("org")
        self.assertEqual(client.has_license(repo, license_key), expected)

    @patch('client.get_json')
    def test_public_repos_exception(self, mock_get_json):
        """
        Test public_repos property with invalid input.
        """
        mock_get_json.return_value = None
        client = GithubOrgClient("org")
        with self.assertRaises(TypeError):
            client.public_repos

    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos_url_exception(self, mock_public_repos_url):
        """
        Test
