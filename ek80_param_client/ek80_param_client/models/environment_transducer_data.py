# coding: utf-8

"""
    REST API for the EK80 Echo Sounder

    The API, and the documentation of it, is still under construction. Feel free to experiment with it, but Kongsberg is only able to provide very limited support at the moment.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EnvironmentTransducerData(object):
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
        'transducer_sound_speed_source': 'str',
        'transducer_manual_sound_speed': 'float'
    }

    attribute_map = {
        'transducer_sound_speed_source': 'transducer-sound-speed-source',
        'transducer_manual_sound_speed': 'transducer-manual-sound-speed'
    }

    def __init__(self, transducer_sound_speed_source=None, transducer_manual_sound_speed=None):  # noqa: E501
        """EnvironmentTransducerData - a model defined in Swagger"""  # noqa: E501

        self._transducer_sound_speed_source = None
        self._transducer_manual_sound_speed = None
        self.discriminator = None

        if transducer_sound_speed_source is not None:
            self.transducer_sound_speed_source = transducer_sound_speed_source
        if transducer_manual_sound_speed is not None:
            self.transducer_manual_sound_speed = transducer_manual_sound_speed

    @property
    def transducer_sound_speed_source(self):
        """Gets the transducer_sound_speed_source of this EnvironmentTransducerData.  # noqa: E501


        :return: The transducer_sound_speed_source of this EnvironmentTransducerData.  # noqa: E501
        :rtype: str
        """
        return self._transducer_sound_speed_source

    @transducer_sound_speed_source.setter
    def transducer_sound_speed_source(self, transducer_sound_speed_source):
        """Sets the transducer_sound_speed_source of this EnvironmentTransducerData.


        :param transducer_sound_speed_source: The transducer_sound_speed_source of this EnvironmentTransducerData.  # noqa: E501
        :type: str
        """
        allowed_values = ["manual", "calculated", "profile", "probe"]  # noqa: E501
        if transducer_sound_speed_source not in allowed_values:
            raise ValueError(
                "Invalid value for `transducer_sound_speed_source` ({0}), must be one of {1}"  # noqa: E501
                .format(transducer_sound_speed_source, allowed_values)
            )

        self._transducer_sound_speed_source = transducer_sound_speed_source

    @property
    def transducer_manual_sound_speed(self):
        """Gets the transducer_manual_sound_speed of this EnvironmentTransducerData.  # noqa: E501


        :return: The transducer_manual_sound_speed of this EnvironmentTransducerData.  # noqa: E501
        :rtype: float
        """
        return self._transducer_manual_sound_speed

    @transducer_manual_sound_speed.setter
    def transducer_manual_sound_speed(self, transducer_manual_sound_speed):
        """Sets the transducer_manual_sound_speed of this EnvironmentTransducerData.


        :param transducer_manual_sound_speed: The transducer_manual_sound_speed of this EnvironmentTransducerData.  # noqa: E501
        :type: float
        """

        self._transducer_manual_sound_speed = transducer_manual_sound_speed

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
        if issubclass(EnvironmentTransducerData, dict):
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
        if not isinstance(other, EnvironmentTransducerData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other