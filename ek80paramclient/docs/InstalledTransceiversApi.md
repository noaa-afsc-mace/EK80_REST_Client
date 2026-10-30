# ek80paramclient.InstalledTransceiversApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_installed_transceivers_channelid_get**](InstalledTransceiversApi.md#api_sounder_installed_transceivers_channelid_get) | **GET** /api/sounder/installed-transceivers/{channelid} | 
[**api_sounder_installed_transceivers_channellistindex_get**](InstalledTransceiversApi.md#api_sounder_installed_transceivers_channellistindex_get) | **GET** /api/sounder/installed-transceivers/{channellistindex} | 
[**api_sounder_installed_transceivers_get**](InstalledTransceiversApi.md#api_sounder_installed_transceivers_get) | **GET** /api/sounder/installed-transceivers | 

# **api_sounder_installed_transceivers_channelid_get**
> EchoSounderTransducer api_sounder_installed_transceivers_channelid_get(channelid)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.InstalledTransceiversApi()
channelid = 'channelid_example' # str | 

try:
    api_response = api_instance.api_sounder_installed_transceivers_channelid_get(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstalledTransceiversApi->api_sounder_installed_transceivers_channelid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 

### Return type

[**EchoSounderTransducer**](EchoSounderTransducer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_installed_transceivers_channellistindex_get**
> EchoSounderTransducer api_sounder_installed_transceivers_channellistindex_get(channellistindex)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.InstalledTransceiversApi()
channellistindex = 56 # int | 

try:
    api_response = api_instance.api_sounder_installed_transceivers_channellistindex_get(channellistindex)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstalledTransceiversApi->api_sounder_installed_transceivers_channellistindex_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channellistindex** | **int**|  | 

### Return type

[**EchoSounderTransducer**](EchoSounderTransducer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_installed_transceivers_get**
> list[EchoSounderTransducer] api_sounder_installed_transceivers_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.InstalledTransceiversApi()

try:
    api_response = api_instance.api_sounder_installed_transceivers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstalledTransceiversApi->api_sounder_installed_transceivers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EchoSounderTransducer]**](EchoSounderTransducer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

