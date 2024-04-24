# coding: utf-8

"""
    REST API for the EK80 Echo Sounder

    The API, and the documentation of it, is still under construction. Feel free to experiment with it, but Kongsberg is only able to provide very limited support at the moment.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ek80_param_client.api_client import ApiClient


class SensorsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sensors_add_or_update_sensor(self, sensor_def, **kwargs):  # noqa: E501
        """Adds a new sensor.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_add_or_update_sensor(sensor_def, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConfiguredSensorDefinition sensor_def: A ConfiguredSensorDefinition that the defines the sensor to add. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sensors_add_or_update_sensor_with_http_info(sensor_def, **kwargs)  # noqa: E501
        else:
            (data) = self.sensors_add_or_update_sensor_with_http_info(sensor_def, **kwargs)  # noqa: E501
            return data

    def sensors_add_or_update_sensor_with_http_info(self, sensor_def, **kwargs):  # noqa: E501
        """Adds a new sensor.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_add_or_update_sensor_with_http_info(sensor_def, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConfiguredSensorDefinition sensor_def: A ConfiguredSensorDefinition that the defines the sensor to add. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sensor_def']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensors_add_or_update_sensor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sensor_def' is set
        if ('sensor_def' not in params or
                params['sensor_def'] is None):
            raise ValueError("Missing the required parameter `sensor_def` when calling `sensors_add_or_update_sensor`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sensor_def' in params:
            body_params = params['sensor_def']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sensors/installed-sensors', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sensors_delete_sensor(self, custom_name, **kwargs):  # noqa: E501
        """Deletes a sensor.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_delete_sensor(custom_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_name: Custom name of the sensor to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sensors_delete_sensor_with_http_info(custom_name, **kwargs)  # noqa: E501
        else:
            (data) = self.sensors_delete_sensor_with_http_info(custom_name, **kwargs)  # noqa: E501
            return data

    def sensors_delete_sensor_with_http_info(self, custom_name, **kwargs):  # noqa: E501
        """Deletes a sensor.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_delete_sensor_with_http_info(custom_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str custom_name: Custom name of the sensor to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['custom_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensors_delete_sensor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'custom_name' is set
        if ('custom_name' not in params or
                params['custom_name'] is None):
            raise ValueError("Missing the required parameter `custom_name` when calling `sensors_delete_sensor`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'custom_name' in params:
            path_params['customName'] = params['custom_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sensors/installed-sensors/{customName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sensors_get_available_sensors(self, **kwargs):  # noqa: E501
        """Get list of all sensor types that can be installed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_get_available_sensors(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[AvailableSensor]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sensors_get_available_sensors_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sensors_get_available_sensors_with_http_info(**kwargs)  # noqa: E501
            return data

    def sensors_get_available_sensors_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of all sensor types that can be installed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_get_available_sensors_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[AvailableSensor]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensors_get_available_sensors" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sensors/available-sensors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AvailableSensor]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sensors_get_installed_sensors(self, **kwargs):  # noqa: E501
        """Get list of all installed sensors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_get_installed_sensors(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sensors_get_installed_sensors_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sensors_get_installed_sensors_with_http_info(**kwargs)  # noqa: E501
            return data

    def sensors_get_installed_sensors_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of all installed sensors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_get_installed_sensors_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensors_get_installed_sensors" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sensors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sensors_get_installed_sensors_full(self, **kwargs):  # noqa: E501
        """Get list of all sensors that are installed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_get_installed_sensors_full(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ConfiguredSensorDefinition]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sensors_get_installed_sensors_full_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sensors_get_installed_sensors_full_with_http_info(**kwargs)  # noqa: E501
            return data

    def sensors_get_installed_sensors_full_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of all sensors that are installed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sensors_get_installed_sensors_full_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ConfiguredSensorDefinition]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sensors_get_installed_sensors_full" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/sensors/installed-sensors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ConfiguredSensorDefinition]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
