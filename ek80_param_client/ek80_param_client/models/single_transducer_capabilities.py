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


class SingleTransducerCapabilities(object):
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
        'beam_type': 'str',
        'beam_id': 'str',
        'gain': 'list[float]',
        'sa_correction': 'list[float]',
        'equivalent_2_way_beam_angle': 'float',
        'directivity_drop_at_2_x_beam_width': 'float',
        'pulse_durations_map': 'dict(str, list[float])',
        'channel_modes': 'list[str]',
        'beam_type_number': 'int'
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
        'beam_type': 'beam-type',
        'beam_id': 'beam-id',
        'gain': 'gain',
        'sa_correction': 'sa-correction',
        'equivalent_2_way_beam_angle': 'equivalent-2-way-beam-angle',
        'directivity_drop_at_2_x_beam_width': 'directivity-drop-at-2-x-beam-width',
        'pulse_durations_map': 'pulse-durations-map',
        'channel_modes': 'channel-modes',
        'beam_type_number': 'beam-type-number'
    }

    def __init__(self, transducer_custom_name=None, unique_name=None, transducer_name=None, serial_number=None, article_number=None, is_fixed_beam=None, geometry_type=None, nominal_frequency=None, minimum_frequency=None, maximum_frequency=None, nominal_beam_opening=None, max_tx_power=None, is_multiplexed=None, transceiver_capabilities=None, beam_type=None, beam_id=None, gain=None, sa_correction=None, equivalent_2_way_beam_angle=None, directivity_drop_at_2_x_beam_width=None, pulse_durations_map=None, channel_modes=None, beam_type_number=None):  # noqa: E501
        """SingleTransducerCapabilities - a model defined in Swagger"""  # noqa: E501

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
        self._beam_type = None
        self._beam_id = None
        self._gain = None
        self._sa_correction = None
        self._equivalent_2_way_beam_angle = None
        self._directivity_drop_at_2_x_beam_width = None
        self._pulse_durations_map = None
        self._channel_modes = None
        self._beam_type_number = None
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
        if beam_type is not None:
            self.beam_type = beam_type
        if beam_id is not None:
            self.beam_id = beam_id
        if gain is not None:
            self.gain = gain
        if sa_correction is not None:
            self.sa_correction = sa_correction
        if equivalent_2_way_beam_angle is not None:
            self.equivalent_2_way_beam_angle = equivalent_2_way_beam_angle
        if directivity_drop_at_2_x_beam_width is not None:
            self.directivity_drop_at_2_x_beam_width = directivity_drop_at_2_x_beam_width
        if pulse_durations_map is not None:
            self.pulse_durations_map = pulse_durations_map
        if channel_modes is not None:
            self.channel_modes = channel_modes
        if beam_type_number is not None:
            self.beam_type_number = beam_type_number

    @property
    def transducer_custom_name(self):
        """Gets the transducer_custom_name of this SingleTransducerCapabilities.  # noqa: E501


        :return: The transducer_custom_name of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._transducer_custom_name

    @transducer_custom_name.setter
    def transducer_custom_name(self, transducer_custom_name):
        """Sets the transducer_custom_name of this SingleTransducerCapabilities.


        :param transducer_custom_name: The transducer_custom_name of this SingleTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._transducer_custom_name = transducer_custom_name

    @property
    def unique_name(self):
        """Gets the unique_name of this SingleTransducerCapabilities.  # noqa: E501


        :return: The unique_name of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, unique_name):
        """Sets the unique_name of this SingleTransducerCapabilities.


        :param unique_name: The unique_name of this SingleTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._unique_name = unique_name

    @property
    def transducer_name(self):
        """Gets the transducer_name of this SingleTransducerCapabilities.  # noqa: E501


        :return: The transducer_name of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._transducer_name

    @transducer_name.setter
    def transducer_name(self, transducer_name):
        """Sets the transducer_name of this SingleTransducerCapabilities.


        :param transducer_name: The transducer_name of this SingleTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._transducer_name = transducer_name

    @property
    def serial_number(self):
        """Gets the serial_number of this SingleTransducerCapabilities.  # noqa: E501


        :return: The serial_number of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: int
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this SingleTransducerCapabilities.


        :param serial_number: The serial_number of this SingleTransducerCapabilities.  # noqa: E501
        :type: int
        """

        self._serial_number = serial_number

    @property
    def article_number(self):
        """Gets the article_number of this SingleTransducerCapabilities.  # noqa: E501


        :return: The article_number of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._article_number

    @article_number.setter
    def article_number(self, article_number):
        """Sets the article_number of this SingleTransducerCapabilities.


        :param article_number: The article_number of this SingleTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._article_number = article_number

    @property
    def is_fixed_beam(self):
        """Gets the is_fixed_beam of this SingleTransducerCapabilities.  # noqa: E501


        :return: The is_fixed_beam of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._is_fixed_beam

    @is_fixed_beam.setter
    def is_fixed_beam(self, is_fixed_beam):
        """Sets the is_fixed_beam of this SingleTransducerCapabilities.


        :param is_fixed_beam: The is_fixed_beam of this SingleTransducerCapabilities.  # noqa: E501
        :type: bool
        """

        self._is_fixed_beam = is_fixed_beam

    @property
    def geometry_type(self):
        """Gets the geometry_type of this SingleTransducerCapabilities.  # noqa: E501


        :return: The geometry_type of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._geometry_type

    @geometry_type.setter
    def geometry_type(self, geometry_type):
        """Sets the geometry_type of this SingleTransducerCapabilities.


        :param geometry_type: The geometry_type of this SingleTransducerCapabilities.  # noqa: E501
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
        """Gets the nominal_frequency of this SingleTransducerCapabilities.  # noqa: E501


        :return: The nominal_frequency of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._nominal_frequency

    @nominal_frequency.setter
    def nominal_frequency(self, nominal_frequency):
        """Sets the nominal_frequency of this SingleTransducerCapabilities.


        :param nominal_frequency: The nominal_frequency of this SingleTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._nominal_frequency = nominal_frequency

    @property
    def minimum_frequency(self):
        """Gets the minimum_frequency of this SingleTransducerCapabilities.  # noqa: E501


        :return: The minimum_frequency of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._minimum_frequency

    @minimum_frequency.setter
    def minimum_frequency(self, minimum_frequency):
        """Sets the minimum_frequency of this SingleTransducerCapabilities.


        :param minimum_frequency: The minimum_frequency of this SingleTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._minimum_frequency = minimum_frequency

    @property
    def maximum_frequency(self):
        """Gets the maximum_frequency of this SingleTransducerCapabilities.  # noqa: E501


        :return: The maximum_frequency of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._maximum_frequency

    @maximum_frequency.setter
    def maximum_frequency(self, maximum_frequency):
        """Sets the maximum_frequency of this SingleTransducerCapabilities.


        :param maximum_frequency: The maximum_frequency of this SingleTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._maximum_frequency = maximum_frequency

    @property
    def nominal_beam_opening(self):
        """Gets the nominal_beam_opening of this SingleTransducerCapabilities.  # noqa: E501


        :return: The nominal_beam_opening of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: BeamAxes
        """
        return self._nominal_beam_opening

    @nominal_beam_opening.setter
    def nominal_beam_opening(self, nominal_beam_opening):
        """Sets the nominal_beam_opening of this SingleTransducerCapabilities.


        :param nominal_beam_opening: The nominal_beam_opening of this SingleTransducerCapabilities.  # noqa: E501
        :type: BeamAxes
        """

        self._nominal_beam_opening = nominal_beam_opening

    @property
    def max_tx_power(self):
        """Gets the max_tx_power of this SingleTransducerCapabilities.  # noqa: E501


        :return: The max_tx_power of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._max_tx_power

    @max_tx_power.setter
    def max_tx_power(self, max_tx_power):
        """Sets the max_tx_power of this SingleTransducerCapabilities.


        :param max_tx_power: The max_tx_power of this SingleTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._max_tx_power = max_tx_power

    @property
    def is_multiplexed(self):
        """Gets the is_multiplexed of this SingleTransducerCapabilities.  # noqa: E501


        :return: The is_multiplexed of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._is_multiplexed

    @is_multiplexed.setter
    def is_multiplexed(self, is_multiplexed):
        """Sets the is_multiplexed of this SingleTransducerCapabilities.


        :param is_multiplexed: The is_multiplexed of this SingleTransducerCapabilities.  # noqa: E501
        :type: bool
        """

        self._is_multiplexed = is_multiplexed

    @property
    def transceiver_capabilities(self):
        """Gets the transceiver_capabilities of this SingleTransducerCapabilities.  # noqa: E501


        :return: The transceiver_capabilities of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: TransceiverCapabilities
        """
        return self._transceiver_capabilities

    @transceiver_capabilities.setter
    def transceiver_capabilities(self, transceiver_capabilities):
        """Sets the transceiver_capabilities of this SingleTransducerCapabilities.


        :param transceiver_capabilities: The transceiver_capabilities of this SingleTransducerCapabilities.  # noqa: E501
        :type: TransceiverCapabilities
        """

        self._transceiver_capabilities = transceiver_capabilities

    @property
    def beam_type(self):
        """Gets the beam_type of this SingleTransducerCapabilities.  # noqa: E501


        :return: The beam_type of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._beam_type

    @beam_type.setter
    def beam_type(self, beam_type):
        """Sets the beam_type of this SingleTransducerCapabilities.


        :param beam_type: The beam_type of this SingleTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._beam_type = beam_type

    @property
    def beam_id(self):
        """Gets the beam_id of this SingleTransducerCapabilities.  # noqa: E501


        :return: The beam_id of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._beam_id

    @beam_id.setter
    def beam_id(self, beam_id):
        """Sets the beam_id of this SingleTransducerCapabilities.


        :param beam_id: The beam_id of this SingleTransducerCapabilities.  # noqa: E501
        :type: str
        """

        self._beam_id = beam_id

    @property
    def gain(self):
        """Gets the gain of this SingleTransducerCapabilities.  # noqa: E501


        :return: The gain of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: list[float]
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        """Sets the gain of this SingleTransducerCapabilities.


        :param gain: The gain of this SingleTransducerCapabilities.  # noqa: E501
        :type: list[float]
        """

        self._gain = gain

    @property
    def sa_correction(self):
        """Gets the sa_correction of this SingleTransducerCapabilities.  # noqa: E501


        :return: The sa_correction of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: list[float]
        """
        return self._sa_correction

    @sa_correction.setter
    def sa_correction(self, sa_correction):
        """Sets the sa_correction of this SingleTransducerCapabilities.


        :param sa_correction: The sa_correction of this SingleTransducerCapabilities.  # noqa: E501
        :type: list[float]
        """

        self._sa_correction = sa_correction

    @property
    def equivalent_2_way_beam_angle(self):
        """Gets the equivalent_2_way_beam_angle of this SingleTransducerCapabilities.  # noqa: E501


        :return: The equivalent_2_way_beam_angle of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._equivalent_2_way_beam_angle

    @equivalent_2_way_beam_angle.setter
    def equivalent_2_way_beam_angle(self, equivalent_2_way_beam_angle):
        """Sets the equivalent_2_way_beam_angle of this SingleTransducerCapabilities.


        :param equivalent_2_way_beam_angle: The equivalent_2_way_beam_angle of this SingleTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._equivalent_2_way_beam_angle = equivalent_2_way_beam_angle

    @property
    def directivity_drop_at_2_x_beam_width(self):
        """Gets the directivity_drop_at_2_x_beam_width of this SingleTransducerCapabilities.  # noqa: E501


        :return: The directivity_drop_at_2_x_beam_width of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._directivity_drop_at_2_x_beam_width

    @directivity_drop_at_2_x_beam_width.setter
    def directivity_drop_at_2_x_beam_width(self, directivity_drop_at_2_x_beam_width):
        """Sets the directivity_drop_at_2_x_beam_width of this SingleTransducerCapabilities.


        :param directivity_drop_at_2_x_beam_width: The directivity_drop_at_2_x_beam_width of this SingleTransducerCapabilities.  # noqa: E501
        :type: float
        """

        self._directivity_drop_at_2_x_beam_width = directivity_drop_at_2_x_beam_width

    @property
    def pulse_durations_map(self):
        """Gets the pulse_durations_map of this SingleTransducerCapabilities.  # noqa: E501


        :return: The pulse_durations_map of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: dict(str, list[float])
        """
        return self._pulse_durations_map

    @pulse_durations_map.setter
    def pulse_durations_map(self, pulse_durations_map):
        """Sets the pulse_durations_map of this SingleTransducerCapabilities.


        :param pulse_durations_map: The pulse_durations_map of this SingleTransducerCapabilities.  # noqa: E501
        :type: dict(str, list[float])
        """

        self._pulse_durations_map = pulse_durations_map

    @property
    def channel_modes(self):
        """Gets the channel_modes of this SingleTransducerCapabilities.  # noqa: E501


        :return: The channel_modes of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: list[str]
        """
        return self._channel_modes

    @channel_modes.setter
    def channel_modes(self, channel_modes):
        """Sets the channel_modes of this SingleTransducerCapabilities.


        :param channel_modes: The channel_modes of this SingleTransducerCapabilities.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["active", "passive", "test"]  # noqa: E501
        if not set(channel_modes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `channel_modes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(channel_modes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._channel_modes = channel_modes

    @property
    def beam_type_number(self):
        """Gets the beam_type_number of this SingleTransducerCapabilities.  # noqa: E501


        :return: The beam_type_number of this SingleTransducerCapabilities.  # noqa: E501
        :rtype: int
        """
        return self._beam_type_number

    @beam_type_number.setter
    def beam_type_number(self, beam_type_number):
        """Sets the beam_type_number of this SingleTransducerCapabilities.


        :param beam_type_number: The beam_type_number of this SingleTransducerCapabilities.  # noqa: E501
        :type: int
        """

        self._beam_type_number = beam_type_number

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
        if issubclass(SingleTransducerCapabilities, dict):
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
        if not isinstance(other, SingleTransducerCapabilities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other