# ek80paramclient.PingInfoCommonApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_ping_info_get**](PingInfoCommonApi.md#api_ping_info_get) | **GET** /api/ping-info | 

# **api_ping_info_get**
> ExecutedPing api_ping_info_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingInfoCommonApi()

try:
    api_response = api_instance.api_ping_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingInfoCommonApi->api_ping_info_get: %s\n" % e)
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

