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


class EnvironmentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def environment_get_transducer_face_data(self, **kwargs):  # noqa: E501
        """Get environmental data for the transducer face  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.environment_get_transducer_face_data(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: EnvironmentTransducerData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.environment_get_transducer_face_data_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.environment_get_transducer_face_data_with_http_info(**kwargs)  # noqa: E501
            return data

    def environment_get_transducer_face_data_with_http_info(self, **kwargs):  # noqa: E501
        """Get environmental data for the transducer face  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.environment_get_transducer_face_data_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: EnvironmentTransducerData
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
                    " to method environment_get_transducer_face_data" % key
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
            '/api/environment/TransducerFace', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnvironmentTransducerData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def environment_get_water_column_data(self, **kwargs):  # noqa: E501
        """Get environmental data for the water column  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.environment_get_water_column_data(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WaterColumnData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.environment_get_water_column_data_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.environment_get_water_column_data_with_http_info(**kwargs)  # noqa: E501
            return data

    def environment_get_water_column_data_with_http_info(self, **kwargs):  # noqa: E501
        """Get environmental data for the water column  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.environment_get_water_column_data_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WaterColumnData
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
                    " to method environment_get_water_column_data" % key
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
            '/api/environment/WaterColumn', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WaterColumnData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def environment_set_transducer_face_data(self, transducer_face, **kwargs):  # noqa: E501
        """Set environmental data for the transducer face  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.environment_set_transducer_face_data(transducer_face, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnvironmentTransducerData transducer_face: EnvironmentTransducerData struct (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.environment_set_transducer_face_data_with_http_info(transducer_face, **kwargs)  # noqa: E501
        else:
            (data) = self.environment_set_transducer_face_data_with_http_info(transducer_face, **kwargs)  # noqa: E501
            return data

    def environment_set_transducer_face_data_with_http_info(self, transducer_face, **kwargs):  # noqa: E501
        """Set environmental data for the transducer face  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.environment_set_transducer_face_data_with_http_info(transducer_face, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnvironmentTransducerData transducer_face: EnvironmentTransducerData struct (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transducer_face']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method environment_set_transducer_face_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transducer_face' is set
        if ('transducer_face' not in params or
                params['transducer_face'] is None):
            raise ValueError("Missing the required parameter `transducer_face` when calling `environment_set_transducer_face_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transducer_face' in params:
            body_params = params['transducer_face']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/environment/TransducerFace', 'POST',
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

    def environment_set_water_column_data(self, water_column, **kwargs):  # noqa: E501
        """set environmental data for the water column  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.environment_set_water_column_data(water_column, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WaterColumnData water_column: WaterColumnData struct (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.environment_set_water_column_data_with_http_info(water_column, **kwargs)  # noqa: E501
        else:
            (data) = self.environment_set_water_column_data_with_http_info(water_column, **kwargs)  # noqa: E501
            return data

    def environment_set_water_column_data_with_http_info(self, water_column, **kwargs):  # noqa: E501
        """set environmental data for the water column  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.environment_set_water_column_data_with_http_info(water_column, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WaterColumnData water_column: WaterColumnData struct (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['water_column']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method environment_set_water_column_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'water_column' is set
        if ('water_column' not in params or
                params['water_column'] is None):
            raise ValueError("Missing the required parameter `water_column` when calling `environment_set_water_column_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'water_column' in params:
            body_params = params['water_column']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/environment/WaterColumn', 'PUT',
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
