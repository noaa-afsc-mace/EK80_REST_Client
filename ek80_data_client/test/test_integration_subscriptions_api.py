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
from ek80_data_client.api.integration_subscriptions_api import IntegrationSubscriptionsApi  # noqa: E501
from ek80_data_client.rest import ApiException


class TestIntegrationSubscriptionsApi(unittest.TestCase):
    """IntegrationSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = ek80_data_client.api.integration_subscriptions_api.IntegrationSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_integration_subscription(self):
        """Test case for create_integration_subscription

        Create an integration data subscription  # noqa: E501
        """
        pass

    def test_delete_integration_subscription(self):
        """Test case for delete_integration_subscription

        Delete an integration data subscription  # noqa: E501
        """
        pass

    def test_get_integration_subscription(self):
        """Test case for get_integration_subscription

        Get a particular integration data subscription specification  # noqa: E501
        """
        pass

    def test_get_integration_subscriptions(self):
        """Test case for get_integration_subscriptions

        Get all integration data subscriptions  # noqa: E501
        """
        pass

    def test_update_integration_state(self):
        """Test case for update_integration_state

        Update the integration state (start/stop integration)  # noqa: E501
        """
        pass

    def test_update_integration_subscription(self):
        """Test case for update_integration_subscription

        Update an integration data subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
