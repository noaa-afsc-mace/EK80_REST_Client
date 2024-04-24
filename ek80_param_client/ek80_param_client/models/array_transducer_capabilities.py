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


class ArrayTransducerCapabilities(object):
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
        'transducer_custom_name': 'str',
        'unique_name': 'str',
        'transducer_name': 'str',
        'serial_number': 'int',
        'article_number': 'str',
        'is_fixed_beam': 'bool',
        'geometry_type': 'str',
        'nominal_frequency': 'float',
        'minimum_frequency': 'float',
        'maximum_frequency': 'float',
        'nominal_beam_opening': 'BeamAxes',
        'max_tx_power': 'float',
        'is_multiplexed': 'bool',
        'transceiver_capabilities': 'TransceiverCapabilities',
        'element_layout': 'str',
        'number_of_td_elements_x': 'int',
        'number_of_td_elements_y': 'int',
        'td_element_separation_x': 'float',
        'td_element_separation_y': 'float',
        'max_number_of_rx_beams_x': 'int',
        'max_number_of_rx_beams_y': 'int',
        'split_beam_percentage': 'int'
    }

    attribute_map = {
        'transducer_custom_name': 'transducer-custom-name',
        'unique_name': 'unique-name',
        'transducer_name': 'transducer-name',
        'serial_number': 'serial-number',
        'article_number': 'article-number',
        'is_fixed_beam': 'is-fixed-beam',
        'geometry_type': 'geometry-type',
        'nominal_frequency': 'nominal-frequency',
        'minimum_frequency': 'minimum-frequency',
        'maximum_frequency': 'maximum-frequency',
        'nominal_beam_opening': 'nominal-beam-opening',
        'max_tx_power': 'max-tx-power',
        'is_multiplexed': 'is-multiplexed',
        'transceiver_capabilities': 'transceiver-capabilities',
        'element_layout': 'element-layout',
        'number_of_td_elements_x': 'number-of-td-elements-x',
        'number_of_td_elements_y': 'number-of-td-elements-y',
        'td_element_separation_x': 'td-element-separation-x',
        'td_element_separation_y': 'td-element-separation-y',
        'max_number_of_rx_beams_x': 'max-number-of-rx-beams-x',
        'max_number_of_rx_beams_y': 'max-number-of-rx-beams-y',
        'split_beam_percentage': 'split-beam-percentage'
    }

    def __init__(self, transducer_custom_name=None, unique_name=None, transducer_name=None, serial_number=None, article_number=None, is_fixed_beam=None, geometry_type=None, nominal_frequency=None, minimum_frequency=None, maximum_frequency=None, nominal_beam_opening=None, max_tx_power=None, is_multiplexed=None, transceiver_capabilities=None, element_layout=None, number_of_td_elements_x=None, number_of_td_elements_y=None, td_element_separation_x=None, td_element_separation_y=None, max_number_of_rx_beams_x=None, max_number_of_rx_beams_y=None, split_beam_percentage=None):  # noqa: E501
        """ArrayTransducerCapabilities - a model defined in Swagger"""  # noqa: E501

        self._transducer_custom_name = None
        self._unique_name = None
        self._transducer_name = None
        self._serial_number = None
        self._article_number = None
        self._is_fixed_beam = None
        self._geometry_type = None
        self._nominal_frequency = None
        self._minimum_frequency = None
        self._maximum_frequency = None
        self._nominal_beam_opening = None
        self._max_tx_power = None
        self._is_multiplexed = None
        self._transceiver_capabilities = None
        self._element_layout = None
        self._number_of_td_elements_x = None
        self._number_of_td_elements_y = None
        self._td_element_separation_x = None
        self._td_element_separation_y = None
        self._max_number_of_rx_beams_x = None
        self._max_number_of_rx_beams_y = None
        self._split_beam_percentage = None
        self.discriminator = None

        if transducer_custom_name is not None:
            self.transducer_custom_name = transducer_custom_name
        if unique_name is not None:
            self.unique_name = unique_name
        if transducer_name is not None:
            self.transducer_name = transducer_name
        if serial_number is not None:
            self.serial_number = serial_number
        if article_number is not None:
            self.article_number = article_number
        if is_fixed_beam is not None:
            self.is_fixed_beam = is_fixed_beam
        if geometry_type is not None:
            self.geometry_type = geometry_type
        if nominal_frequency is not None:
            self.nominal_frequency = nominal_frequency
        if minimum_frequency is not None:
            self.minimum_frequency = minimum_frequency
        if maximum_frequency is not None:
            self.maximum_frequency = maximum_frequency
        if nominal_beam_opening is not None:
            self.nominal_beam_opening = nominal_beam_opening
        if max_tx_power is not None:
            self.max_tx_power = max_tx_power
        if is_multiplexed is not None:
            self.is_multiplexed = is_multiplexed
        if transceiver_capabilities is not None:
            self.transceiver_capabilities = transceiver_capabilities
        if element_layout is not None:
            self.element_layout = element_layout
        if number_of_td_elements_x is not None:
            self.number_of_td_elements_x = number_of_td_elements_x
        if number_of_td_elements_y is not None:
            self.number_of_td_elements_y = number_of_td_elements_y
        if td_element_separation_x is not None:
            self.td_element_separation_x = td_element_separation_x
        if td_element_separation_y is not None:
            self.td_element_separation_y = td_element_separation_y
        if max_number_of_rx_beams_x is not None:
            self.max_number_of_rx_beams_x = max_number_of_rx_beams_x
        if max_number_of_rx_beams_y is not None:
            self.max_number_of_rx_beams_y = max_number_of_rx_beams_y
        if split_beam_percentage is not None:
            self.split_beam_percentage = split_beam_percentage

    @property
    def transducer_custom_name(self):
        """Gets the transducer_custom_name of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The transducer_custom_name of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._transducer_custom_name

    @transducer_custom_name.setter
    def transducer_custom_name(self, transducer_custom_name):
        """Sets the transducer_custom_name of this ArrayTransducerCapabilities.


        :param transducer_custom_name: The transducer_custom_name of this ArrayTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._transducer_custom_name = transducer_custom_name

    @property
    def unique_name(self):
        """Gets the unique_name of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The unique_name of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, unique_name):
        """Sets the unique_name of this ArrayTransducerCapabilities.


        :param unique_name: The unique_name of this ArrayTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._unique_name = unique_name

    @property
    def transducer_name(self):
        """Gets the transducer_name of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The transducer_name of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._transducer_name

    @transducer_name.setter
    def transducer_name(self, transducer_name):
        """Sets the transducer_name of this ArrayTransducerCapabilities.


        :param transducer_name: The transducer_name of this ArrayTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._transducer_name = transducer_name

    @property
    def serial_number(self):
        """Gets the serial_number of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The serial_number of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: int
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ArrayTransducerCapabilities.


        :param serial_number: The serial_number of this ArrayTransducerCapabilities.  # noqa: E501
        :type: int
        """

        self._serial_number = serial_number

    @property
    def article_number(self):
        """Gets the article_number of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The article_number of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._article_number

    @article_number.setter
    def article_number(self, article_number):
        """Sets the article_number of this ArrayTransducerCapabilities.


        :param article_number: The article_number of this ArrayTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._article_number = article_number

    @property
    def is_fixed_beam(self):
        """Gets the is_fixed_beam of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The is_fixed_beam of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._is_fixed_beam

    @is_fixed_beam.setter
    def is_fixed_beam(self, is_fixed_beam):
        """Sets the is_fixed_beam of this ArrayTransducerCapabilities.


        :param is_fixed_beam: The is_fixed_beam of this ArrayTransducerCapabilities.  # noqa: E501
        :type: bool
        """

        self._is_fixed_beam = is_fixed_beam

    @property
    def geometry_type(self):
        """Gets the geometry_type of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The geometry_type of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._geometry_type

    @geometry_type.setter
    def geometry_type(self, geometry_type):
        """Sets the geometry_type of this ArrayTransducerCapabilities.


        :param geometry_type: The geometry_type of this ArrayTransducerCapabilities.  # noqa: E501
        :type: str
        """
        allowed_values = ["single", "single-split", "planar-array", "cylindrical-array", "spherical-array", "custom-transducer"]  # noqa: E501
        if geometry_type not in allowed_values:
            raise ValueError(
                "Invalid value for `geometry_type` ({0}), must be one of {1}"  # noqa: E501
                .format(geometry_type, allowed_values)
            )

        self._geometry_type = geometry_type

    @property
    def nominal_frequency(self):
        """Gets the nominal_frequency of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The nominal_frequency of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._nominal_frequency

    @nominal_frequency.setter
    def nominal_frequency(self, nominal_frequency):
        """Sets the nominal_frequency of this ArrayTransducerCapabilities.


        :param nominal_frequency: The nominal_frequency of this ArrayTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._nominal_frequency = nominal_frequency

    @property
    def minimum_frequency(self):
        """Gets the minimum_frequency of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The minimum_frequency of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._minimum_frequency

    @minimum_frequency.setter
    def minimum_frequency(self, minimum_frequency):
        """Sets the minimum_frequency of this ArrayTransducerCapabilities.


        :param minimum_frequency: The minimum_frequency of this ArrayTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._minimum_frequency = minimum_frequency

    @property
    def maximum_frequency(self):
        """Gets the maximum_frequency of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The maximum_frequency of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._maximum_frequency

    @maximum_frequency.setter
    def maximum_frequency(self, maximum_frequency):
        """Sets the maximum_frequency of this ArrayTransducerCapabilities.


        :param maximum_frequency: The maximum_frequency of this ArrayTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._maximum_frequency = maximum_frequency

    @property
    def nominal_beam_opening(self):
        """Gets the nominal_beam_opening of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The nominal_beam_opening of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: BeamAxes
        """
        return self._nominal_beam_opening

    @nominal_beam_opening.setter
    def nominal_beam_opening(self, nominal_beam_opening):
        """Sets the nominal_beam_opening of this ArrayTransducerCapabilities.


        :param nominal_beam_opening: The nominal_beam_opening of this ArrayTransducerCapabilities.  # noqa: E501
        :type: BeamAxes
        """

        self._nominal_beam_opening = nominal_beam_opening

    @property
    def max_tx_power(self):
        """Gets the max_tx_power of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The max_tx_power of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._max_tx_power

    @max_tx_power.setter
    def max_tx_power(self, max_tx_power):
        """Sets the max_tx_power of this ArrayTransducerCapabilities.


        :param max_tx_power: The max_tx_power of this ArrayTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._max_tx_power = max_tx_power

    @property
    def is_multiplexed(self):
        """Gets the is_multiplexed of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The is_multiplexed of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._is_multiplexed

    @is_multiplexed.setter
    def is_multiplexed(self, is_multiplexed):
        """Sets the is_multiplexed of this ArrayTransducerCapabilities.


        :param is_multiplexed: The is_multiplexed of this ArrayTransducerCapabilities.  # noqa: E501
        :type: bool
        """

        self._is_multiplexed = is_multiplexed

    @property
    def transceiver_capabilities(self):
        """Gets the transceiver_capabilities of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The transceiver_capabilities of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: TransceiverCapabilities
        """
        return self._transceiver_capabilities

    @transceiver_capabilities.setter
    def transceiver_capabilities(self, transceiver_capabilities):
        """Sets the transceiver_capabilities of this ArrayTransducerCapabilities.


        :param transceiver_capabilities: The transceiver_capabilities of this ArrayTransducerCapabilities.  # noqa: E501
        :type: TransceiverCapabilities
        """

        self._transceiver_capabilities = transceiver_capabilities

    @property
    def element_layout(self):
        """Gets the element_layout of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The element_layout of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._element_layout

    @element_layout.setter
    def element_layout(self, element_layout):
        """Sets the element_layout of this ArrayTransducerCapabilities.


        :param element_layout: The element_layout of this ArrayTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._element_layout = element_layout

    @property
    def number_of_td_elements_x(self):
        """Gets the number_of_td_elements_x of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The number_of_td_elements_x of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: int
        """
        return self._number_of_td_elements_x

    @number_of_td_elements_x.setter
    def number_of_td_elements_x(self, number_of_td_elements_x):
        """Sets the number_of_td_elements_x of this ArrayTransducerCapabilities.


        :param number_of_td_elements_x: The number_of_td_elements_x of this ArrayTransducerCapabilities.  # noqa: E501
        :type: int
        """

        self._number_of_td_elements_x = number_of_td_elements_x

    @property
    def number_of_td_elements_y(self):
        """Gets the number_of_td_elements_y of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The number_of_td_elements_y of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: int
        """
        return self._number_of_td_elements_y

    @number_of_td_elements_y.setter
    def number_of_td_elements_y(self, number_of_td_elements_y):
        """Sets the number_of_td_elements_y of this ArrayTransducerCapabilities.


        :param number_of_td_elements_y: The number_of_td_elements_y of this ArrayTransducerCapabilities.  # noqa: E501
        :type: int
        """

        self._number_of_td_elements_y = number_of_td_elements_y

    @property
    def td_element_separation_x(self):
        """Gets the td_element_separation_x of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The td_element_separation_x of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._td_element_separation_x

    @td_element_separation_x.setter
    def td_element_separation_x(self, td_element_separation_x):
        """Sets the td_element_separation_x of this ArrayTransducerCapabilities.


        :param td_element_separation_x: The td_element_separation_x of this ArrayTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._td_element_separation_x = td_element_separation_x

    @property
    def td_element_separation_y(self):
        """Gets the td_element_separation_y of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The td_element_separation_y of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._td_element_separation_y

    @td_element_separation_y.setter
    def td_element_separation_y(self, td_element_separation_y):
        """Sets the td_element_separation_y of this ArrayTransducerCapabilities.


        :param td_element_separation_y: The td_element_separation_y of this ArrayTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._td_element_separation_y = td_element_separation_y

    @property
    def max_number_of_rx_beams_x(self):
        """Gets the max_number_of_rx_beams_x of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The max_number_of_rx_beams_x of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: int
        """
        return self._max_number_of_rx_beams_x

    @max_number_of_rx_beams_x.setter
    def max_number_of_rx_beams_x(self, max_number_of_rx_beams_x):
        """Sets the max_number_of_rx_beams_x of this ArrayTransducerCapabilities.


        :param max_number_of_rx_beams_x: The max_number_of_rx_beams_x of this ArrayTransducerCapabilities.  # noqa: E501
        :type: int
        """

        self._max_number_of_rx_beams_x = max_number_of_rx_beams_x

    @property
    def max_number_of_rx_beams_y(self):
        """Gets the max_number_of_rx_beams_y of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The max_number_of_rx_beams_y of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: int
        """
        return self._max_number_of_rx_beams_y

    @max_number_of_rx_beams_y.setter
    def max_number_of_rx_beams_y(self, max_number_of_rx_beams_y):
        """Sets the max_number_of_rx_beams_y of this ArrayTransducerCapabilities.


        :param max_number_of_rx_beams_y: The max_number_of_rx_beams_y of this ArrayTransducerCapabilities.  # noqa: E501
        :type: int
        """

        self._max_number_of_rx_beams_y = max_number_of_rx_beams_y

    @property
    def split_beam_percentage(self):
        """Gets the split_beam_percentage of this ArrayTransducerCapabilities.  # noqa: E501


        :return: The split_beam_percentage of this ArrayTransducerCapabilities.  # noqa: E501
        :rtype: int
        """
        return self._split_beam_percentage

    @split_beam_percentage.setter
    def split_beam_percentage(self, split_beam_percentage):
        """Sets the split_beam_percentage of this ArrayTransducerCapabilities.


        :param split_beam_percentage: The split_beam_percentage of this ArrayTransducerCapabilities.  # noqa: E501
        :type: int
        """

        self._split_beam_percentage = split_beam_percentage

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
        if issubclass(ArrayTransducerCapabilities, dict):
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
        if not isinstance(other, ArrayTransducerCapabilities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
