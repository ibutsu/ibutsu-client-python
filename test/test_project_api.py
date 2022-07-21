"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.project_api import ProjectApi  # noqa: E501


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_project(self):
        """Test case for add_project

        Create a project  # noqa: E501
        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Get a single project by ID  # noqa: E501
        """
        pass

    def test_get_project_list(self):
        """Test case for get_project_list

        Get a list of projects  # noqa: E501
        """
        pass

    def test_update_project(self):
        """Test case for update_project

        Update a project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
