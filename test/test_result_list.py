"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ibutsu_client
from ibutsu_client.model.pagination import Pagination
from ibutsu_client.model.result import Result
globals()['Pagination'] = Pagination
globals()['Result'] = Result
from ibutsu_client.model.result_list import ResultList


class TestResultList(unittest.TestCase):
    """ResultList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResultList(self):
        """Test ResultList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResultList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
