# coding: utf-8

"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.10.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ibutsu_client
from ibutsu_client.api.result_api import ResultApi  # noqa: E501
from ibutsu_client.rest import ApiException


class TestResultApi(unittest.TestCase):
    """ResultApi unit test stubs"""

    def setUp(self):
        self.api = ibutsu_client.api.result_api.ResultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_result(self):
        """Test case for add_result

        Create a test result  # noqa: E501
        """
        pass

    def test_get_result(self):
        """Test case for get_result

        Get a single result  # noqa: E501
        """
        pass

    def test_get_result_list(self):
        """Test case for get_result_list

        Get the list of results.  # noqa: E501
        """
        pass

    def test_update_result(self):
        """Test case for update_result

        Updates a single result  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
