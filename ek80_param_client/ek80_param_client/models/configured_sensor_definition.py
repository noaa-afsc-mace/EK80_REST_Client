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


class ConfiguredSensorDefinition(object):
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
        'sensor_type': 'str',
        'telegram_protocol': 'str',
        'custom_name': 'str',
        'configured_telegrams': 'list[str]',
        'port_name': 'str',
        'sensor_timeout': 'int',
        'talker_id': 'str',
        'sensor_offset': 'Offset',
        'sensor_rotation': 'Rotation'
    }

    attribute_map = {
        'sensor_type': 'sensor-type',
        'telegram_protocol': 'telegram-protocol',
        'custom_name': 'custom-name',
        'configured_telegrams': 'configured-telegrams',
        'port_name': 'port-name',
        'sensor_timeout': 'sensor-timeout',
        'talker_id': 'talker-id',
        'sensor_offset': 'sensor-offset',
        'sensor_rotation': 'sensor-rotation'
    }

    def __init__(self, sensor_type=None, telegram_protocol=None, custom_name=None, configured_telegrams=None, port_name=None, sensor_timeout=None, talker_id=None, sensor_offset=None, sensor_rotation=None):  # noqa: E501
        """ConfiguredSensorDefinition - a model defined in Swagger"""  # noqa: E501

        self._sensor_type = None
        self._telegram_protocol = None
        self._custom_name = None
        self._configured_telegrams = None
        self._port_name = None
        self._sensor_timeout = None
        self._talker_id = None
        self._sensor_offset = None
        self._sensor_rotation = None
        self.discriminator = None

        if sensor_type is not None:
            self.sensor_type = sensor_type
        if telegram_protocol is not None:
            self.telegram_protocol = telegram_protocol
        if custom_name is not None:
            self.custom_name = custom_name
        if configured_telegrams is not None:
            self.configured_telegrams = configured_telegrams
        if port_name is not None:
            self.port_name = port_name
        if sensor_timeout is not None:
            self.sensor_timeout = sensor_timeout
        if talker_id is not None:
            self.talker_id = talker_id
        if sensor_offset is not None:
            self.sensor_offset = sensor_offset
        if sensor_rotation is not None:
            self.sensor_rotation = sensor_rotation

    @property
    def sensor_type(self):
        """Gets the sensor_type of this ConfiguredSensorDefinition.  # noqa: E501


        :return: The sensor_type of this ConfiguredSensorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._sensor_type

    @sensor_type.setter
    def sensor_type(self, sensor_type):
        """Sets the sensor_type of this ConfiguredSensorDefinition.


        :param sensor_type: The sensor_type of this ConfiguredSensorDefinition.  # noqa: E501
        :type: str
        """

        self._sensor_type = sensor_type

    @property
    def telegram_protocol(self):
        """Gets the telegram_protocol of this ConfiguredSensorDefinition.  # noqa: E501


        :return: The telegram_protocol of this ConfiguredSensorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._telegram_protocol

    @telegram_protocol.setter
    def telegram_protocol(self, telegram_protocol):
        """Sets the telegram_protocol of this ConfiguredSensorDefinition.


        :param telegram_protocol: The telegram_protocol of this ConfiguredSensorDefinition.  # noqa: E501
        :type: str
        """

        self._telegram_protocol = telegram_protocol

    @property
    def custom_name(self):
        """Gets the custom_name of this ConfiguredSensorDefinition.  # noqa: E501


        :return: The custom_name of this ConfiguredSensorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._custom_name

    @custom_name.setter
    def custom_name(self, custom_name):
        """Sets the custom_name of this ConfiguredSensorDefinition.


        :param custom_name: The custom_name of this ConfiguredSensorDefinition.  # noqa: E501
        :type: str
        """

        self._custom_name = custom_name

    @property
    def configured_telegrams(self):
        """Gets the configured_telegrams of this ConfiguredSensorDefinition.  # noqa: E501


        :return: The configured_telegrams of this ConfiguredSensorDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._configured_telegrams

    @configured_telegrams.setter
    def configured_telegrams(self, configured_telegrams):
        """Sets the configured_telegrams of this ConfiguredSensorDefinition.


        :param configured_telegrams: The configured_telegrams of this ConfiguredSensorDefinition.  # noqa: E501
        :type: list[str]
        """

        self._configured_telegrams = configured_telegrams

    @property
    def port_name(self):
        """Gets the port_name of this ConfiguredSensorDefinition.  # noqa: E501


        :return: The port_name of this ConfiguredSensorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        """Sets the port_name of this ConfiguredSensorDefinition.


        :param port_name: The port_name of this ConfiguredSensorDefinition.  # noqa: E501
        :type: str
        """

        self._port_name = port_name

    @property
    def sensor_timeout(self):
        """Gets the sensor_timeout of this ConfiguredSensorDefinition.  # noqa: E501


        :return: The sensor_timeout of this ConfiguredSensorDefinition.  # noqa: E501
        :rtype: int
        """
        return self._sensor_timeout

    @sensor_timeout.setter
    def sensor_timeout(self, sensor_timeout):
        """Sets the sensor_timeout of this ConfiguredSensorDefinition.


        :param sensor_timeout: The sensor_timeout of this ConfiguredSensorDefinition.  # noqa: E501
        :type: int
        """

        self._sensor_timeout = sensor_timeout

    @property
    def talker_id(self):
        """Gets the talker_id of this ConfiguredSensorDefinition.  # noqa: E501


        :return: The talker_id of this ConfiguredSensorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._talker_id

    @talker_id.setter
    def talker_id(self, talker_id):
        """Sets the talker_id of this ConfiguredSensorDefinition.


        :param talker_id: The talker_id of this ConfiguredSensorDefinition.  # noqa: E501
        :type: str
        """

        self._talker_id = talker_id

    @property
    def sensor_offset(self):
        """Gets the sensor_offset of this ConfiguredSensorDefinition.  # noqa: E501


        :return: The sensor_offset of this ConfiguredSensorDefinition.  # noqa: E501
        :rtype: Offset
        """
        return self._sensor_offset

    @sensor_offset.setter
    def sensor_offset(self, sensor_offset):
        """Sets the sensor_offset of this ConfiguredSensorDefinition.


        :param sensor_offset: The sensor_offset of this ConfiguredSensorDefinition.  # noqa: E501
        :type: Offset
        """

        self._sensor_offset = sensor_offset

    @property
    def sensor_rotation(self):
        """Gets the sensor_rotation of this ConfiguredSensorDefinition.  # noqa: E501


        :return: The sensor_rotation of this ConfiguredSensorDefinition.  # noqa: E501
        :rtype: Rotation
        """
        return self._sensor_rotation

    @sensor_rotation.setter
    def sensor_rotation(self, sensor_rotation):
        """Sets the sensor_rotation of this ConfiguredSensorDefinition.


        :param sensor_rotation: The sensor_rotation of this ConfiguredSensorDefinition.  # noqa: E501
        :type: Rotation
        """

        self._sensor_rotation = sensor_rotation

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
        if issubclass(ConfiguredSensorDefinition, dict):
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
        if not isinstance(other, ConfiguredSensorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other