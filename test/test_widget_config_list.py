"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.13.4
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ibutsu_client
from ibutsu_client.model.pagination import Pagination
from ibutsu_client.model.widget_config import WidgetConfig
globals()['Pagination'] = Pagination
globals()['WidgetConfig'] = WidgetConfig
from ibutsu_client.model.widget_config_list import WidgetConfigList


class TestWidgetConfigList(unittest.TestCase):
    """WidgetConfigList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetConfigList(self):
        """Test WidgetConfigList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WidgetConfigList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
