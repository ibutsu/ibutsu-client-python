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
from ibutsu_client.models.artifact import Artifact  # noqa: E501
from ibutsu_client.rest import ApiException

class TestArtifact(unittest.TestCase):
    """Artifact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Artifact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ibutsu_client.models.artifact.Artifact()  # noqa: E501
        if include_optional :
            return Artifact(
                id = '507f1f77bcf86cd799439011', 
                result_id = '0', 
                filename = '0', 
                additional_metadata = None
            )
        else :
            return Artifact(
        )

    def testArtifact(self):
        """Test Artifact"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()