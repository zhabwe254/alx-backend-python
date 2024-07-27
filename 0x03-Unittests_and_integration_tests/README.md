 Unittests and Integration Tests

## Project Overview

This project focuses on implementing unit tests and integration tests for a Python application. It covers various testing techniques including parameterization, mocking, and fixtures.

## Requirements

- Python 3.7+
- Ubuntu 18.04 LTS
- pip3

## Installation

Clone the repository:

```bash
git clone https://github.com/zhabwe254/alx-backend-python.git
cd alx-backend-python/0x03-Unittests_and_integration_tests
Install the required packages:
bashCopypip3 install -r requirements.txt
File Descriptions

utils.py: Contains utility functions to be tested.
client.py: Implements a GitHub organization client.
fixtures.py: Contains test fixtures.
test_utils.py: Unit tests for utils.py.
test_client.py: Unit and integration tests for client.py.

Running Tests
To run all tests:
bashCopypython3 -m unittest discover
To run a specific test file:
bashCopypython3 -m unittest test_utils.py
python3 -m unittest test_client.py
Tasks

Parameterize a unit test
Parameterize a unit test (exception handling)
Mock HTTP calls
Parameterize and patch
Parameterize and patch as decorators
Mocking a property
More patching
Parameterize
Integration test: fixtures
