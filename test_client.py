#!/usr/bin/env python3

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test the _public_repos_url property."""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://testurl.com"}
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, "http://testurl.com")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method."""
        mock_get_json.return_value = repos_payload
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://testurl.com"
            client = GithubOrgClient("test")
            self.assertEqual(client.public_repos(), expected_repos)
            mock_get_json.assert_called_once_with("http://testurl.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method."""
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Set up class fixtures."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class fixtures."""
        cls.get_patcher.stop()

    @staticmethod
    def get_json_side_effect(url):
        """Return different payloads based on the URL."""
        if url == "https://api.github.com/orgs/google":
            return Mock(json=lambda: org_payload)
        if url == "https://api.github.com/orgs/google/repos":
            return Mock(json=lambda: repos_payload)
        return Mock(json=lambda: {})

    def test_public_repos(self):
        """Test public_repos integration."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), apache2_repos)
