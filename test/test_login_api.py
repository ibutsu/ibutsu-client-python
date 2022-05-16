"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 2.2.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.login_api import LoginApi  # noqa: E501


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate(self):
        """Test case for activate

        """
        pass

    def test_auth(self):
        """Test case for auth

        """
        pass

    def test_config(self):
        """Test case for config

        """
        pass

    def test_login(self):
        """Test case for login

        """
        pass

    def test_recover(self):
        """Test case for recover

        """
        pass

    def test_register(self):
        """Test case for register

        """
        pass

    def test_reset_password(self):
        """Test case for reset_password

        """
        pass

    def test_support(self):
        """Test case for support

        """
        pass


if __name__ == '__main__':
    unittest.main()
