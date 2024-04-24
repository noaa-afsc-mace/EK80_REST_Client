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
from ek80_data_client.api.create_a_data_subscription_api import CreateADataSubscriptionApi  # noqa: E501
from ek80_data_client.rest import ApiException


class TestCreateADataSubscriptionApi(unittest.TestCase):
    """CreateADataSubscriptionApi unit test stubs"""

    def setUp(self):
        self.api = ek80_data_client.api.create_a_data_subscription_api.CreateADataSubscriptionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_adcp_backscatter_subscription(self):
        """Test case for create_adcp_backscatter_subscription

        Create an adcp data subscription  # noqa: E501
        """
        pass

    def test_create_adcp_beam_data_subscription(self):
        """Test case for create_adcp_beam_data_subscription

        Create an adcp data subscription  # noqa: E501
        """
        pass

    def test_create_adcp_bottom_detector_subscription(self):
        """Test case for create_adcp_bottom_detector_subscription

        Create an adcp data subscription  # noqa: E501
        """
        pass

    def test_create_adcp_output_subscription(self):
        """Test case for create_adcp_output_subscription

        Create an adcp data subscription  # noqa: E501
        """
        pass

    def test_create_adcp_quality_factor_subscription(self):
        """Test case for create_adcp_quality_factor_subscription

        Create an adcp data subscription  # noqa: E501
        """
        pass

    def test_create_adcp_velocity_subscription(self):
        """Test case for create_adcp_velocity_subscription

        Create an adcp data subscription  # noqa: E501
        """
        pass

    def test_create_bottom_detection_subscription(self):
        """Test case for create_bottom_detection_subscription

        Create a bottom detection data subscription  # noqa: E501
        """
        pass

    def test_create_echogram_subscription(self):
        """Test case for create_echogram_subscription

        Create an echogram data subscription  # noqa: E501
        """
        pass

    def test_create_integration_chirp_subscription(self):
        """Test case for create_integration_chirp_subscription

        Create an integration chirp data subscription  # noqa: E501
        """
        pass

    def test_create_integration_subscription(self):
        """Test case for create_integration_subscription

        Create an integration data subscription  # noqa: E501
        """
        pass

    def test_create_noise_spectrum_subscription(self):
        """Test case for create_noise_spectrum_subscription

        Create a noise spectrum data subscription  # noqa: E501
        """
        pass

    def test_create_sample_data_subscription(self):
        """Test case for create_sample_data_subscription

        Create a processed sample-data subscription  # noqa: E501
        """
        pass

    def test_create_system_state_subscription(self):
        """Test case for create_system_state_subscription

        Create a system state data subscription  # noqa: E501
        """
        pass

    def test_create_targets_echogram_subscription(self):
        """Test case for create_targets_echogram_subscription

        Create a targets echogram data subscription  # noqa: E501
        """
        pass

    def test_create_targets_integration_subscription(self):
        """Test case for create_targets_integration_subscription

        Create a targets integration data subscription  # noqa: E501
        """
        pass

    def test_create_ts_detection_chirp_subscription(self):
        """Test case for create_ts_detection_chirp_subscription

        Create a ts detection chirp data subscription  # noqa: E501
        """
        pass

    def test_create_ts_detection_subscription(self):
        """Test case for create_ts_detection_subscription

        Create a ts detection data subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()