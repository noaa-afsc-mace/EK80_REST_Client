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
from ek80_param_client.api.advanced_sequencing_api import AdvancedSequencingApi  # noqa: E501
from ek80_param_client.rest import ApiException


class TestAdvancedSequencingApi(unittest.TestCase):
    """AdvancedSequencingApi unit test stubs"""

    def setUp(self):
        self.api = ek80_param_client.api.advanced_sequencing_api.AdvancedSequencingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_advanced_sequencing_get_advanced_sequencing_settings(self):
        """Test case for advanced_sequencing_get_advanced_sequencing_settings

        Get Advanced Sequencing complete configuration  # noqa: E501
        """
        pass

    def test_advanced_sequencing_get_sequences(self):
        """Test case for advanced_sequencing_get_sequences

        """
        pass

    def test_advanced_sequencing_set_advanced_sequencing_settings(self):
        """Test case for advanced_sequencing_set_advanced_sequencing_settings

        Set Advanced Sequencing complete configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
