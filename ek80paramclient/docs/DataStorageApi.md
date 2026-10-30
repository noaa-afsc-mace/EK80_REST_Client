# ek80paramclient.DataStorageApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_storage_get**](DataStorageApi.md#api_sounder_data_storage_get) | **GET** /api/sounder/data-storage | 
[**api_sounder_data_storage_individual_channel_range_channel_name_get**](DataStorageApi.md#api_sounder_data_storage_individual_channel_range_channel_name_get) | **GET** /api/sounder/data-storage/individual-channel-range/{channel_name} | 
[**api_sounder_data_storage_individual_channel_range_put**](DataStorageApi.md#api_sounder_data_storage_individual_channel_range_put) | **PUT** /api/sounder/data-storage/individual-channel-range | 
[**api_sounder_data_storage_put**](DataStorageApi.md#api_sounder_data_storage_put) | **PUT** /api/sounder/data-storage | 
[**api_sounder_data_storage_record_raw_active_get**](DataStorageApi.md#api_sounder_data_storage_record_raw_active_get) | **GET** /api/sounder/data-storage/record-raw-active | 
[**api_sounder_data_storage_record_raw_active_put**](DataStorageApi.md#api_sounder_data_storage_record_raw_active_put) | **PUT** /api/sounder/data-storage/record-raw-active | 
[**api_sounder_data_storage_sample_data_format_wbt_cw_get**](DataStorageApi.md#api_sounder_data_storage_sample_data_format_wbt_cw_get) | **GET** /api/sounder/data-storage/sample-data-format-wbt-cw | 
[**api_sounder_data_storage_sample_data_format_wbt_cw_put**](DataStorageApi.md#api_sounder_data_storage_sample_data_format_wbt_cw_put) | **PUT** /api/sounder/data-storage/sample-data-format-wbt-cw | 

# **api_sounder_data_storage_get**
> MainStorageSettings api_sounder_data_storage_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataStorageApi()

try:
    api_response = api_instance.api_sounder_data_storage_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStorageApi->api_sounder_data_storage_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MainStorageSettings**](MainStorageSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_storage_individual_channel_range_channel_name_get**
> IndividualRangeControl api_sounder_data_storage_individual_channel_range_channel_name_get(channel_name)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataStorageApi()
channel_name = 'channel_name_example' # str | 

try:
    api_response = api_instance.api_sounder_data_storage_individual_channel_range_channel_name_get(channel_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStorageApi->api_sounder_data_storage_individual_channel_range_channel_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 

### Return type

[**IndividualRangeControl**](IndividualRangeControl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_storage_individual_channel_range_put**
> api_sounder_data_storage_individual_channel_range_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataStorageApi()
body = ek80paramclient.IndividualRangeControl() # IndividualRangeControl |  (optional)

try:
    api_instance.api_sounder_data_storage_individual_channel_range_put(body=body)
except ApiException as e:
    print("Exception when calling DataStorageApi->api_sounder_data_storage_individual_channel_range_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndividualRangeControl**](IndividualRangeControl.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_storage_put**
> api_sounder_data_storage_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataStorageApi()
body = ek80paramclient.MainStorageSettings() # MainStorageSettings |  (optional)

try:
    api_instance.api_sounder_data_storage_put(body=body)
except ApiException as e:
    print("Exception when calling DataStorageApi->api_sounder_data_storage_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MainStorageSettings**](MainStorageSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_storage_record_raw_active_get**
> bool api_sounder_data_storage_record_raw_active_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataStorageApi()

try:
    api_response = api_instance.api_sounder_data_storage_record_raw_active_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStorageApi->api_sounder_data_storage_record_raw_active_get: %s\n" % e)
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

# **api_sounder_data_storage_record_raw_active_put**
> api_sounder_data_storage_record_raw_active_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataStorageApi()
body = True # bool |  (optional)

try:
    api_instance.api_sounder_data_storage_record_raw_active_put(body=body)
except ApiException as e:
    print("Exception when calling DataStorageApi->api_sounder_data_storage_record_raw_active_put: %s\n" % e)
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

# **api_sounder_data_storage_sample_data_format_wbt_cw_get**
> str api_sounder_data_storage_sample_data_format_wbt_cw_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataStorageApi()

try:
    api_response = api_instance.api_sounder_data_storage_sample_data_format_wbt_cw_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStorageApi->api_sounder_data_storage_sample_data_format_wbt_cw_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_storage_sample_data_format_wbt_cw_put**
> api_sounder_data_storage_sample_data_format_wbt_cw_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DataStorageApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.api_sounder_data_storage_sample_data_format_wbt_cw_put(body=body)
except ApiException as e:
    print("Exception when calling DataStorageApi->api_sounder_data_storage_sample_data_format_wbt_cw_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

