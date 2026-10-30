# ek80paramclient.AdvancedSequencingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_advanced_sequencing_get**](AdvancedSequencingApi.md#api_sounder_advanced_sequencing_get) | **GET** /api/sounder/advanced-sequencing | 
[**api_sounder_advanced_sequencing_put**](AdvancedSequencingApi.md#api_sounder_advanced_sequencing_put) | **PUT** /api/sounder/advanced-sequencing | 
[**api_sounder_advanced_sequencing_sequence_list_get**](AdvancedSequencingApi.md#api_sounder_advanced_sequencing_sequence_list_get) | **GET** /api/sounder/advanced-sequencing/sequence-list | 

# **api_sounder_advanced_sequencing_get**
> AdvancedSequencingSettings api_sounder_advanced_sequencing_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.AdvancedSequencingApi()

try:
    api_response = api_instance.api_sounder_advanced_sequencing_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedSequencingApi->api_sounder_advanced_sequencing_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdvancedSequencingSettings**](AdvancedSequencingSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_advanced_sequencing_put**
> api_sounder_advanced_sequencing_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.AdvancedSequencingApi()
body = ek80paramclient.AdvancedSequencingSettings() # AdvancedSequencingSettings |  (optional)

try:
    api_instance.api_sounder_advanced_sequencing_put(body=body)
except ApiException as e:
    print("Exception when calling AdvancedSequencingApi->api_sounder_advanced_sequencing_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdvancedSequencingSettings**](AdvancedSequencingSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_advanced_sequencing_sequence_list_get**
> list[str] api_sounder_advanced_sequencing_sequence_list_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.AdvancedSequencingApi()

try:
    api_response = api_instance.api_sounder_advanced_sequencing_sequence_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedSequencingApi->api_sounder_advanced_sequencing_sequence_list_get: %s\n" % e)
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

