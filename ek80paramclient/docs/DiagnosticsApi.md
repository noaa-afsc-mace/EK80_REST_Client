# ek80paramclient.DiagnosticsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_diagnostics_impedance_calculations_on_get**](DiagnosticsApi.md#api_diagnostics_impedance_calculations_on_get) | **GET** /api/diagnostics/impedance/calculations-on | 
[**api_diagnostics_impedance_calculations_on_put**](DiagnosticsApi.md#api_diagnostics_impedance_calculations_on_put) | **PUT** /api/diagnostics/impedance/calculations-on | 
[**api_diagnostics_impedance_channelid_get**](DiagnosticsApi.md#api_diagnostics_impedance_channelid_get) | **GET** /api/diagnostics/impedance/{channelid} | 
[**api_diagnostics_ping_time_monitor_get**](DiagnosticsApi.md#api_diagnostics_ping_time_monitor_get) | **GET** /api/diagnostics/ping-time-monitor | 
[**api_diagnostics_ping_time_monitor_is_enabled_get**](DiagnosticsApi.md#api_diagnostics_ping_time_monitor_is_enabled_get) | **GET** /api/diagnostics/ping-time-monitor/is-enabled | 
[**api_diagnostics_ping_time_monitor_is_enabled_put**](DiagnosticsApi.md#api_diagnostics_ping_time_monitor_is_enabled_put) | **PUT** /api/diagnostics/ping-time-monitor/is-enabled | 
[**api_diagnostics_transceiver_info_get**](DiagnosticsApi.md#api_diagnostics_transceiver_info_get) | **GET** /api/diagnostics/transceiver-info | 

# **api_diagnostics_impedance_calculations_on_get**
> bool api_diagnostics_impedance_calculations_on_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DiagnosticsApi()

try:
    api_response = api_instance.api_diagnostics_impedance_calculations_on_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->api_diagnostics_impedance_calculations_on_get: %s\n" % e)
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

# **api_diagnostics_impedance_calculations_on_put**
> api_diagnostics_impedance_calculations_on_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DiagnosticsApi()
body = True # bool |  (optional)

try:
    api_instance.api_diagnostics_impedance_calculations_on_put(body=body)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->api_diagnostics_impedance_calculations_on_put: %s\n" % e)
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

# **api_diagnostics_impedance_channelid_get**
> PingImpedanceData api_diagnostics_impedance_channelid_get(channelid)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DiagnosticsApi()
channelid = 'channelid_example' # str | 

try:
    api_response = api_instance.api_diagnostics_impedance_channelid_get(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->api_diagnostics_impedance_channelid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 

### Return type

[**PingImpedanceData**](PingImpedanceData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_diagnostics_ping_time_monitor_get**
> SystemPingMonitoringInfo api_diagnostics_ping_time_monitor_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DiagnosticsApi()

try:
    api_response = api_instance.api_diagnostics_ping_time_monitor_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->api_diagnostics_ping_time_monitor_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemPingMonitoringInfo**](SystemPingMonitoringInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_diagnostics_ping_time_monitor_is_enabled_get**
> bool api_diagnostics_ping_time_monitor_is_enabled_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DiagnosticsApi()

try:
    api_response = api_instance.api_diagnostics_ping_time_monitor_is_enabled_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->api_diagnostics_ping_time_monitor_is_enabled_get: %s\n" % e)
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

# **api_diagnostics_ping_time_monitor_is_enabled_put**
> api_diagnostics_ping_time_monitor_is_enabled_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DiagnosticsApi()
body = True # bool |  (optional)

try:
    api_instance.api_diagnostics_ping_time_monitor_is_enabled_put(body=body)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->api_diagnostics_ping_time_monitor_is_enabled_put: %s\n" % e)
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

# **api_diagnostics_transceiver_info_get**
> list[TransceiverParameters] api_diagnostics_transceiver_info_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DiagnosticsApi()

try:
    api_response = api_instance.api_diagnostics_transceiver_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagnosticsApi->api_diagnostics_transceiver_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TransceiverParameters]**](TransceiverParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

