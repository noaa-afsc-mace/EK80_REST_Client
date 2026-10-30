# ek80paramclient.DataOutputApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_data_output_get**](DataOutputApi.md#api_data_output_get) | **GET** /api/data-output | 
[**api_data_output_processed_data_get**](DataOutputApi.md#api_data_output_processed_data_get) | **GET** /api/data-output/processed-data | 
[**api_data_output_processed_data_put**](DataOutputApi.md#api_data_output_processed_data_put) | **PUT** /api/data-output/processed-data | 

# **api_data_output_get**
> list[DataOutput] api_data_output_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataOutputApi()

try:
    api_response = api_instance.api_data_output_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataOutputApi->api_data_output_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DataOutput]**](DataOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_data_output_processed_data_get**
> bool api_data_output_processed_data_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataOutputApi()

try:
    api_response = api_instance.api_data_output_processed_data_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataOutputApi->api_data_output_processed_data_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_data_output_processed_data_put**
> api_data_output_processed_data_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataOutputApi()
body = True # bool |  (optional)

try:
    api_instance.api_data_output_processed_data_put(body=body)
except ApiException as e:
    print("Exception when calling DataOutputApi->api_data_output_processed_data_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**bool**](bool.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

