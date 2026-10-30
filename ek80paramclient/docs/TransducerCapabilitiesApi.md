# ek80paramclient.TransducerCapabilitiesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_transducer_capabilities_adcp_transducers_get**](TransducerCapabilitiesApi.md#api_transducer_capabilities_adcp_transducers_get) | **GET** /api/transducer-capabilities/adcp-transducers | GetAdcpTransducerCapabilities
[**api_transducer_capabilities_array_transducers_get**](TransducerCapabilitiesApi.md#api_transducer_capabilities_array_transducers_get) | **GET** /api/transducer-capabilities/array-transducers | GetArrayTransducerCapabilities
[**api_transducer_capabilities_channelid_get**](TransducerCapabilitiesApi.md#api_transducer_capabilities_channelid_get) | **GET** /api/transducer-capabilities/{channelid} | 
[**api_transducer_capabilities_get**](TransducerCapabilitiesApi.md#api_transducer_capabilities_get) | **GET** /api/transducer-capabilities | GetTransducerCapabilities
[**api_transducer_capabilities_single_split_transducers_get**](TransducerCapabilitiesApi.md#api_transducer_capabilities_single_split_transducers_get) | **GET** /api/transducer-capabilities/single-split-transducers | GetSingleSplitTransducerCapabilities
[**api_transducer_capabilities_single_transducers_get**](TransducerCapabilitiesApi.md#api_transducer_capabilities_single_transducers_get) | **GET** /api/transducer-capabilities/single-transducers | GetSingleTransducerCapabilities

# **api_transducer_capabilities_adcp_transducers_get**
> list[AdcpTransducerCapabilities] api_transducer_capabilities_adcp_transducers_get()

GetAdcpTransducerCapabilities

### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.TransducerCapabilitiesApi()

try:
    # GetAdcpTransducerCapabilities
    api_response = api_instance.api_transducer_capabilities_adcp_transducers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->api_transducer_capabilities_adcp_transducers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpTransducerCapabilities]**](AdcpTransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transducer_capabilities_array_transducers_get**
> list[ArrayTransducerCapabilities] api_transducer_capabilities_array_transducers_get()

GetArrayTransducerCapabilities

### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.TransducerCapabilitiesApi()

try:
    # GetArrayTransducerCapabilities
    api_response = api_instance.api_transducer_capabilities_array_transducers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->api_transducer_capabilities_array_transducers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ArrayTransducerCapabilities]**](ArrayTransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transducer_capabilities_channelid_get**
> TransducerCapabilities api_transducer_capabilities_channelid_get(channelid)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.TransducerCapabilitiesApi()
channelid = 'channelid_example' # str | 

try:
    api_response = api_instance.api_transducer_capabilities_channelid_get(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->api_transducer_capabilities_channelid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 

### Return type

[**TransducerCapabilities**](TransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transducer_capabilities_get**
> list[TransducerCapabilities] api_transducer_capabilities_get()

GetTransducerCapabilities

### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.TransducerCapabilitiesApi()

try:
    # GetTransducerCapabilities
    api_response = api_instance.api_transducer_capabilities_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->api_transducer_capabilities_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TransducerCapabilities]**](TransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transducer_capabilities_single_split_transducers_get**
> list[SingleSplitTransducerCapabilities] api_transducer_capabilities_single_split_transducers_get()

GetSingleSplitTransducerCapabilities

### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.TransducerCapabilitiesApi()

try:
    # GetSingleSplitTransducerCapabilities
    api_response = api_instance.api_transducer_capabilities_single_split_transducers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->api_transducer_capabilities_single_split_transducers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SingleSplitTransducerCapabilities]**](SingleSplitTransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_transducer_capabilities_single_transducers_get**
> list[SingleTransducerCapabilities] api_transducer_capabilities_single_transducers_get()

GetSingleTransducerCapabilities

### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.TransducerCapabilitiesApi()

try:
    # GetSingleTransducerCapabilities
    api_response = api_instance.api_transducer_capabilities_single_transducers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransducerCapabilitiesApi->api_transducer_capabilities_single_transducers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SingleTransducerCapabilities]**](SingleTransducerCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

