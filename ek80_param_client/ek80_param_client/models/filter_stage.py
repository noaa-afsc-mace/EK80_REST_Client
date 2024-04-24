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


class FilterStage(object):
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
        'decimation': 'int',
        'coefficients': 'list[list[float]]'
    }

    attribute_map = {
        'decimation': 'Decimation',
        'coefficients': 'Coefficients'
    }

    def __init__(self, decimation=None, coefficients=None):  # noqa: E501
        """FilterStage - a model defined in Swagger"""  # noqa: E501

        self._decimation = None
        self._coefficients = None
        self.discriminator = None

        if decimation is not None:
            self.decimation = decimation
        if coefficients is not None:
            self.coefficients = coefficients

    @property
    def decimation(self):
        """Gets the decimation of this FilterStage.  # noqa: E501


        :return: The decimation of this FilterStage.  # noqa: E501
        :rtype: int
        """
        return self._decimation

    @decimation.setter
    def decimation(self, decimation):
        """Sets the decimation of this FilterStage.


        :param decimation: The decimation of this FilterStage.  # noqa: E501
        :type: int
        """

        self._decimation = decimation

    @property
    def coefficients(self):
        """Gets the coefficients of this FilterStage.  # noqa: E501


        :return: The coefficients of this FilterStage.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._coefficients

    @coefficients.setter
    def coefficients(self, coefficients):
        """Sets the coefficients of this FilterStage.


        :param coefficients: The coefficients of this FilterStage.  # noqa: E501
        :type: list[list[float]]
        """

        self._coefficients = coefficients

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
        if issubclass(FilterStage, dict):
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
        if not isinstance(other, FilterStage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other