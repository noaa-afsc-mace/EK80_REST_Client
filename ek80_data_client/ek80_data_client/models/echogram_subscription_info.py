# coding: utf-8

"""
    REST API for setting up data subscriptions on the EK80 Echo Sounder

    The API, and the documentation of it, is still under construction. Feel free to experiment with it, but Kongsberg is only able to provide very limited support at the moment.  # How to start data output  1. Create a subscription  2. Create a communication end point  3. Add the subscription to the communication end point      # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EchogramSubscriptionInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'subscription_id': 'int',
        'specification': 'EchogramSubscriptionSpecification'
    }

    attribute_map = {
        'subscription_id': 'subscription-id',
        'specification': 'specification'
    }

    def __init__(self, subscription_id=None, specification=None):  # noqa: E501
        """EchogramSubscriptionInfo - a model defined in Swagger"""  # noqa: E501

        self._subscription_id = None
        self._specification = None
        self.discriminator = None

        if subscription_id is not None:
            self.subscription_id = subscription_id
        self.specification = specification

    @property
    def subscription_id(self):
        """Gets the subscription_id of this EchogramSubscriptionInfo.  # noqa: E501


        :return: The subscription_id of this EchogramSubscriptionInfo.  # noqa: E501
        :rtype: int
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this EchogramSubscriptionInfo.


        :param subscription_id: The subscription_id of this EchogramSubscriptionInfo.  # noqa: E501
        :type: int
        """

        self._subscription_id = subscription_id

    @property
    def specification(self):
        """Gets the specification of this EchogramSubscriptionInfo.  # noqa: E501


        :return: The specification of this EchogramSubscriptionInfo.  # noqa: E501
        :rtype: EchogramSubscriptionSpecification
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this EchogramSubscriptionInfo.


        :param specification: The specification of this EchogramSubscriptionInfo.  # noqa: E501
        :type: EchogramSubscriptionSpecification
        """
        if specification is None:
            raise ValueError("Invalid value for `specification`, must not be `None`")  # noqa: E501

        self._specification = specification

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EchogramSubscriptionInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EchogramSubscriptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
