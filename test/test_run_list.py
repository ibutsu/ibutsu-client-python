# coding: utf-8

"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ibutsu_client
from ibutsu_client.models.run_list import RunList  # noqa: E501
from ibutsu_client.rest import ApiException

class TestRunList(unittest.TestCase):
    """RunList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RunList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ibutsu_client.models.run_list.RunList()  # noqa: E501
        if include_optional :
            return RunList(
                runs = [
                    {"id":"cd7994f77bcf8639011507f1","created":"2020-05-15T16:18:32.014053","duration":540.05433,"source":"my-tests","start_time":1.589559512014053E9,"summary":{"errors":1,"failures":3,"skips":0,"tests":548},"metadata":{"component":"login","env":"qa"}}
                    ], 
                pagination = {"page":2,"pageSize":25,"totalPages":10,"totalItems":243}
            )
        else :
            return RunList(
        )

    def testRunList(self):
        """Test RunList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()