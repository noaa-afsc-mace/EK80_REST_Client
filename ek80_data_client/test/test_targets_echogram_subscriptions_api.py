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
from ek80_data_client.api.targets_echogram_subscriptions_api import TargetsEchogramSubscriptionsApi  # noqa: E501
from ek80_data_client.rest import ApiException


class TestTargetsEchogramSubscriptionsApi(unittest.TestCase):
    """TargetsEchogramSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = ek80_data_client.api.targets_echogram_subscriptions_api.TargetsEchogramSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_targets_echogram_subscription(self):
        """Test case for create_targets_echogram_subscription

        Create a targets echogram data subscription  # noqa: E501
        """
        pass

    def test_delete_targets_echogram_subscription(self):
        """Test case for delete_targets_echogram_subscription

        Delete a targets echogram data subscription  # noqa: E501
        """
        pass

    def test_get_targets_echogram_subscription(self):
        """Test case for get_targets_echogram_subscription

        Get a particular targets echogram data subscription specification  # noqa: E501
        """
        pass

    def test_get_targets_echogram_subscriptions(self):
        """Test case for get_targets_echogram_subscriptions

        Get all targets echogram data subscriptions  # noqa: E501
        """
        pass

    def test_update_targets_echogram_subscription(self):
        """Test case for update_targets_echogram_subscription

        Update a targets echogram data subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
