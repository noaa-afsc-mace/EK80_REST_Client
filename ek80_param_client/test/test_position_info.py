# coding: utf-8

"""
    REST API for the EK80 Echo Sounder

    The API, and the documentation of it, is still under construction. Feel free to experiment with it, but Kongsberg is only able to provide very limited support at the moment.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ek80_param_client
from ek80_param_client.models.position_info import PositionInfo  # noqa: E501
from ek80_param_client.rest import ApiException


class TestPositionInfo(unittest.TestCase):
    """PositionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPositionInfo(self):
        """Test PositionInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ek80_param_client.models.position_info.PositionInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
