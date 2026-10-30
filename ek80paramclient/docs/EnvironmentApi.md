# ek80paramclient.EnvironmentApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_environment_transducer_face_get**](EnvironmentApi.md#api_environment_transducer_face_get) | **GET** /api/environment/TransducerFace | 
[**api_environment_transducer_face_put**](EnvironmentApi.md#api_environment_transducer_face_put) | **PUT** /api/environment/TransducerFace | 
[**api_environment_water_column_get**](EnvironmentApi.md#api_environment_water_column_get) | **GET** /api/environment/WaterColumn | 
[**api_environment_water_column_put**](EnvironmentApi.md#api_environment_water_column_put) | **PUT** /api/environment/WaterColumn | 

# **api_environment_transducer_face_get**
> EnvironmentTransducerData api_environment_transducer_face_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.EnvironmentApi()

try:
    api_response = api_instance.api_environment_transducer_face_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->api_environment_transducer_face_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnvironmentTransducerData**](EnvironmentTransducerData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_environment_transducer_face_put**
> api_environment_transducer_face_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.EnvironmentApi()
body = ek80paramclient.EnvironmentTransducerData() # EnvironmentTransducerData |  (optional)

try:
    api_instance.api_environment_transducer_face_put(body=body)
except ApiException as e:
    print("Exception when calling EnvironmentApi->api_environment_transducer_face_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentTransducerData**](EnvironmentTransducerData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_environment_water_column_get**
> WaterColumnData api_environment_water_column_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.EnvironmentApi()

try:
    api_response = api_instance.api_environment_water_column_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->api_environment_water_column_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WaterColumnData**](WaterColumnData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_environment_water_column_put**
> api_environment_water_column_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.EnvironmentApi()
body = ek80paramclient.WaterColumnData() # WaterColumnData |  (optional)

try:
    api_instance.api_environment_water_column_put(body=body)
except ApiException as e:
    print("Exception when calling EnvironmentApi->api_environment_water_column_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WaterColumnData**](WaterColumnData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

