"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 2.2.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.admin_user_management_api import AdminUserManagementApi  # noqa: E501


class TestAdminUserManagementApi(unittest.TestCase):
    """AdminUserManagementApi unit test stubs"""

    def setUp(self):
        self.api = AdminUserManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_add_user(self):
        """Test case for admin_add_user

        Administration endpoint to manually add a user. Only accessible to superadmins.  # noqa: E501
        """
        pass

    def test_admin_delete_user(self):
        """Test case for admin_delete_user

        Administration endpoint to delete a user. Only accessible to superadmins.  # noqa: E501
        """
        pass

    def test_admin_get_user(self):
        """Test case for admin_get_user

        Administration endpoint to return a user. Only accessible to superadmins.  # noqa: E501
        """
        pass

    def test_admin_get_user_list(self):
        """Test case for admin_get_user_list

        Administration endpoint to return a list of users. Only accessible to superadmins.  # noqa: E501
        """
        pass

    def test_admin_update_user(self):
        """Test case for admin_update_user

        Administration endpoint to update a user. Only accessible to superadmins.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
