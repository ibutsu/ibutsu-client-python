"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.admin_project_management_api import AdminProjectManagementApi  # noqa: E501


class TestAdminProjectManagementApi(unittest.TestCase):
    """AdminProjectManagementApi unit test stubs"""

    def setUp(self):
        self.api = AdminProjectManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_admin_add_project(self):
        """Test case for admin_add_project

        Administration endpoint to manually add a project. Only accessible to superadmins.  # noqa: E501
        """
        pass

    def test_admin_delete_project(self):
        """Test case for admin_delete_project

        Administration endpoint to delete a project. Only accessible to superadmins.  # noqa: E501
        """
        pass

    def test_admin_get_project(self):
        """Test case for admin_get_project

        Administration endpoint to return a project. Only accessible to superadmins.  # noqa: E501
        """
        pass

    def test_admin_get_project_list(self):
        """Test case for admin_get_project_list

        Administration endpoint to return a list of projects. Only accessible to superadmins.  # noqa: E501
        """
        pass

    def test_admin_update_project(self):
        """Test case for admin_update_project

        Administration endpoint to update a project. Only accessible to superadmins.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
