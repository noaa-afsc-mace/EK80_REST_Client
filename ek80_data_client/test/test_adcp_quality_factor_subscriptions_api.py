# coding: utf-8

"""
    REST API for setting up data subscriptions on the EK80 Echo Sounder

    The API, and the documentation of it, is still under construction. Feel free to experiment with it, but Kongsberg is only able to provide very limited support at the moment.  # How to start data output  1. Create a subscription  2. Create a communication end point  3. Add the subscription to the communication end point      # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ek80_data_client
from ek80_data_client.api.adcp_quality_factor_subscriptions_api import AdcpQualityFactorSubscriptionsApi  # noqa: E501
from ek80_data_client.rest import ApiException


class TestAdcpQualityFactorSubscriptionsApi(unittest.TestCase):
    """AdcpQualityFactorSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = ek80_data_client.api.adcp_quality_factor_subscriptions_api.AdcpQualityFactorSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_adcp_quality_factor_subscription(self):
        """Test case for create_adcp_quality_factor_subscription

        Create an adcp data subscription  # noqa: E501
        """
        pass

    def test_delete_adcp_quality_factor_subscription(self):
        """Test case for delete_adcp_quality_factor_subscription

        Delete an adcp detection data subscription  # noqa: E501
        """
        pass

    def test_get_adcp_quality_factor_subscriptions(self):
        """Test case for get_adcp_quality_factor_subscriptions

        Get all adcp data subscriptions  # noqa: E501
        """
        pass

    def test_get_quality_factor_adcp_subscription(self):
        """Test case for get_quality_factor_adcp_subscription

        Get an adcp subscription specification  # noqa: E501
        """
        pass

    def test_update_adcp_quality_factor_subscription(self):
        """Test case for update_adcp_quality_factor_subscription

        Update an adcp subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()