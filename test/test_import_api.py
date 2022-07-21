"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.import_api import ImportApi  # noqa: E501


class TestImportApi(unittest.TestCase):
    """ImportApi unit test stubs"""

    def setUp(self):
        self.api = ImportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_import(self):
        """Test case for add_import

        Import a file into Ibutsu. This can be either a JUnit XML file, or an Ibutsu archive  # noqa: E501
        """
        pass

    def test_get_import(self):
        """Test case for get_import

        Get the status of an import  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
