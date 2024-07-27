#!/usr/bin/env python3

"""
Test suite for client module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """
        Test org property with valid input.
        """
        mock_get_json.return_value = {"org": org}
        client = GithubOrgClient(org)
        self.assertEqual(client.org, org)
        mock_get_json.assert_called_once()

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """
        Test public_repos_url property with valid input.
        """
        mock_org.return_value = "example"
        client = GithubOrgClient()
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/example/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test public_repos property with valid input.
        """
        mock_public_repos_url.return_value = "https://api.github.com/orgs/example/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient()
        self.assertEqual(client.public_repos, ["repo1", "repo2"])
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/example/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test has_license method with valid inputs.
        """
        client = GithubOrgClient()
        self.assertEqual(client.has_license(repo, license_key), expected)

    @parameterized.expand([
        ({}, "my_license", False),
        ({"license": {}}, "my_license", False),
    ])
    def test_has_license_exception(self, repo, license_key, expected):
        """
        Test has_license method with invalid inputs.
        """
        client = GithubOrgClient()
        self.assertEqual(client.has_license(repo, license_key), expected)

    @patch('client.get_json')
    def test_public_repos_exception(self, mock_get_json):
        """
        Test public_repos property with invalid input.
        """
        mock_get_json.return_value = None
        client = GithubOrgClient()
        with self.assertRaises(TypeError):
            client.public_repos

    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos_url_exception(self, mock_public_repos_url):
        """
        Test public_repos_url property with invalid input.
        """
        mock_public_repos_url.return_value = None
        client = GithubOrgClient()
        with self.assertRaises(TypeError):
            client._public_repos_url

if __name__ == '__main__':
    unittest.main()
