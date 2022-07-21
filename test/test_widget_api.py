"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.widget_api import WidgetApi  # noqa: E501


class TestWidgetApi(unittest.TestCase):
    """WidgetApi unit test stubs"""

    def setUp(self):
        self.api = WidgetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_widget(self):
        """Test case for get_widget

        Generate data for a dashboard widget  # noqa: E501
        """
        pass

    def test_get_widget_types(self):
        """Test case for get_widget_types

        Get a list of widget types  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
