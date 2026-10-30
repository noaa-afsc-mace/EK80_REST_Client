# ek80paramclient.PingInfoApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_ping_info_channelid_get**](PingInfoApi.md#api_sounder_ping_info_channelid_get) | **GET** /api/sounder/ping-info/{channelid} | 
[**api_sounder_ping_info_get**](PingInfoApi.md#api_sounder_ping_info_get) | **GET** /api/sounder/ping-info | 

# **api_sounder_ping_info_channelid_get**
> ChannelPingConfiguration api_sounder_ping_info_channelid_get(channelid)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingInfoApi()
channelid = 'channelid_example' # str | 

try:
    api_response = api_instance.api_sounder_ping_info_channelid_get(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingInfoApi->api_sounder_ping_info_channelid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 

### Return type

[**ChannelPingConfiguration**](ChannelPingConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_ping_info_get**
> ExecutedPing api_sounder_ping_info_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingInfoApi()

try:
    api_response = api_instance.api_sounder_ping_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingInfoApi->api_sounder_ping_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExecutedPing**](ExecutedPing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

