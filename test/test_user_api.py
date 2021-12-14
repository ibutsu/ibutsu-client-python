"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.13.4
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.user_api import UserApi  # noqa: E501


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_token(self):
        """Test case for add_token

        Create a token for the current user  # noqa: E501
        """
        pass

    def test_delete_token(self):
        """Test case for delete_token

        Delete the token  # noqa: E501
        """
        pass

    def test_get_token(self):
        """Test case for get_token

        Retrieve a single token for the current user  # noqa: E501
        """
        pass

    def test_get_token_list(self):
        """Test case for get_token_list

        Return the tokens for the user  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Return the user details for the current user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()