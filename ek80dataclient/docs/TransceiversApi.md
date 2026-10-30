# ek80dataclient.TransceiversApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_transceivers_get**](TransceiversApi.md#api_sounder_transceivers_get) | **GET** /api/sounder/transceivers | GetInstalledTransceivers

# **api_sounder_transceivers_get**
> list[EchoSounderTransducer] api_sounder_transceivers_get()

GetInstalledTransceivers

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TransceiversApi()

try:
    # GetInstalledTransceivers
    api_response = api_instance.api_sounder_transceivers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransceiversApi->api_sounder_transceivers_get: %s\n" % e)
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

