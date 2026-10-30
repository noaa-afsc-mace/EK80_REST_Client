# ek80paramclient.SensorsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sensors_available_sensors_get**](SensorsApi.md#api_sensors_available_sensors_get) | **GET** /api/sensors/available-sensors | 
[**api_sensors_get**](SensorsApi.md#api_sensors_get) | **GET** /api/sensors | 
[**api_sensors_installed_sensors_custom_name_delete**](SensorsApi.md#api_sensors_installed_sensors_custom_name_delete) | **DELETE** /api/sensors/installed-sensors/{customName} | 
[**api_sensors_installed_sensors_get**](SensorsApi.md#api_sensors_installed_sensors_get) | **GET** /api/sensors/installed-sensors | 
[**api_sensors_installed_sensors_post**](SensorsApi.md#api_sensors_installed_sensors_post) | **POST** /api/sensors/installed-sensors | 

# **api_sensors_available_sensors_get**
> list[AvailableSensor] api_sensors_available_sensors_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SensorsApi()

try:
    api_response = api_instance.api_sensors_available_sensors_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->api_sensors_available_sensors_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AvailableSensor]**](AvailableSensor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sensors_get**
> list[str] api_sensors_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SensorsApi()

try:
    api_response = api_instance.api_sensors_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->api_sensors_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sensors_installed_sensors_custom_name_delete**
> api_sensors_installed_sensors_custom_name_delete(custom_name)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SensorsApi()
custom_name = 'custom_name_example' # str | 

try:
    api_instance.api_sensors_installed_sensors_custom_name_delete(custom_name)
except ApiException as e:
    print("Exception when calling SensorsApi->api_sensors_installed_sensors_custom_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sensors_installed_sensors_get**
> list[ConfiguredSensorDefinition] api_sensors_installed_sensors_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SensorsApi()

try:
    api_response = api_instance.api_sensors_installed_sensors_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->api_sensors_installed_sensors_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfiguredSensorDefinition]**](ConfiguredSensorDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sensors_installed_sensors_post**
> api_sensors_installed_sensors_post(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SensorsApi()
body = ek80paramclient.ConfiguredSensorDefinition() # ConfiguredSensorDefinition |  (optional)

try:
    api_instance.api_sensors_installed_sensors_post(body=body)
except ApiException as e:
    print("Exception when calling SensorsApi->api_sensors_installed_sensors_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfiguredSensorDefinition**](ConfiguredSensorDefinition.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

