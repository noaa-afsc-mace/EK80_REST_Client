# ek80dataclient.OperationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_operation_auto_display_range_get**](OperationApi.md#api_sounder_operation_auto_display_range_get) | **GET** /api/sounder/operation/auto-display-range | GetAutoRange
[**api_sounder_operation_auto_display_range_put**](OperationApi.md#api_sounder_operation_auto_display_range_put) | **PUT** /api/sounder/operation/auto-display-range | PutAutoRange
[**api_sounder_operation_display_range_get**](OperationApi.md#api_sounder_operation_display_range_get) | **GET** /api/sounder/operation/display-range | GetRange
[**api_sounder_operation_display_range_put**](OperationApi.md#api_sounder_operation_display_range_put) | **PUT** /api/sounder/operation/display-range | PutRange
[**api_sounder_operation_external_sync_delay_get**](OperationApi.md#api_sounder_operation_external_sync_delay_get) | **GET** /api/sounder/operation/external-sync/delay | GetExtSyncDelay
[**api_sounder_operation_external_sync_delay_put**](OperationApi.md#api_sounder_operation_external_sync_delay_put) | **PUT** /api/sounder/operation/external-sync/delay | PutExtSyncDelay
[**api_sounder_operation_external_sync_get**](OperationApi.md#api_sounder_operation_external_sync_get) | **GET** /api/sounder/operation/external-sync | GetExtSync
[**api_sounder_operation_external_sync_put**](OperationApi.md#api_sounder_operation_external_sync_put) | **PUT** /api/sounder/operation/external-sync | PutExtSync
[**api_sounder_operation_external_sync_sync_mode_get**](OperationApi.md#api_sounder_operation_external_sync_sync_mode_get) | **GET** /api/sounder/operation/external-sync/sync-mode | GetExtSyncMode
[**api_sounder_operation_external_sync_sync_mode_put**](OperationApi.md#api_sounder_operation_external_sync_sync_mode_put) | **PUT** /api/sounder/operation/external-sync/sync-mode | PutExtSyncMode
[**api_sounder_operation_get**](OperationApi.md#api_sounder_operation_get) | **GET** /api/sounder/operation | GetOperationalState
[**api_sounder_operation_operation_mode_get**](OperationApi.md#api_sounder_operation_operation_mode_get) | **GET** /api/sounder/operation/operation-mode | GetOperationMode
[**api_sounder_operation_operation_mode_put**](OperationApi.md#api_sounder_operation_operation_mode_put) | **PUT** /api/sounder/operation/operation-mode | PutOperationMode
[**api_sounder_operation_ping_interval_get**](OperationApi.md#api_sounder_operation_ping_interval_get) | **GET** /api/sounder/operation/ping-interval | GetPingInterval
[**api_sounder_operation_ping_interval_put**](OperationApi.md#api_sounder_operation_ping_interval_put) | **PUT** /api/sounder/operation/ping-interval | PutPingInterval
[**api_sounder_operation_ping_mode_get**](OperationApi.md#api_sounder_operation_ping_mode_get) | **GET** /api/sounder/operation/ping-mode | GetPingMode
[**api_sounder_operation_ping_mode_put**](OperationApi.md#api_sounder_operation_ping_mode_put) | **PUT** /api/sounder/operation/ping-mode | PutPingMode
[**api_sounder_operation_play_state_get**](OperationApi.md#api_sounder_operation_play_state_get) | **GET** /api/sounder/operation/play-state | GetPlayState
[**api_sounder_operation_play_state_put**](OperationApi.md#api_sounder_operation_play_state_put) | **PUT** /api/sounder/operation/play-state | PutPlayState

# **api_sounder_operation_auto_display_range_get**
> bool api_sounder_operation_auto_display_range_get()

GetAutoRange

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetAutoRange
    api_response = api_instance.api_sounder_operation_auto_display_range_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_auto_display_range_get: %s\n" % e)
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

# **api_sounder_operation_auto_display_range_put**
> api_sounder_operation_auto_display_range_put(auto_display_range=auto_display_range)

PutAutoRange

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()
auto_display_range = true # bool |  (optional)

try:
    # PutAutoRange
    api_instance.api_sounder_operation_auto_display_range_put(auto_display_range=auto_display_range)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_auto_display_range_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_display_range** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_display_range_get**
> float api_sounder_operation_display_range_get()

GetRange

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetRange
    api_response = api_instance.api_sounder_operation_display_range_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_display_range_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_display_range_put**
> api_sounder_operation_display_range_put(display_range=display_range)

PutRange

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()
display_range = 1.2 # float |  (optional)

try:
    # PutRange
    api_instance.api_sounder_operation_display_range_put(display_range=display_range)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_display_range_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_range** | **float**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_external_sync_delay_get**
> int api_sounder_operation_external_sync_delay_get()

GetExtSyncDelay

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetExtSyncDelay
    api_response = api_instance.api_sounder_operation_external_sync_delay_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_external_sync_delay_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_external_sync_delay_put**
> api_sounder_operation_external_sync_delay_put(delay=delay)

PutExtSyncDelay

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()
delay = 56 # int |  (optional)

try:
    # PutExtSyncDelay
    api_instance.api_sounder_operation_external_sync_delay_put(delay=delay)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_external_sync_delay_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delay** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_external_sync_get**
> ExternalSync api_sounder_operation_external_sync_get()

GetExtSync

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetExtSync
    api_response = api_instance.api_sounder_operation_external_sync_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_external_sync_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExternalSync**](ExternalSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_external_sync_put**
> api_sounder_operation_external_sync_put(body=body)

PutExtSync

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()
body = ek80dataclient.ExternalSync() # ExternalSync |  (optional)

try:
    # PutExtSync
    api_instance.api_sounder_operation_external_sync_put(body=body)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_external_sync_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalSync**](ExternalSync.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_external_sync_sync_mode_get**
> str api_sounder_operation_external_sync_sync_mode_get()

GetExtSyncMode

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetExtSyncMode
    api_response = api_instance.api_sounder_operation_external_sync_sync_mode_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_external_sync_sync_mode_get: %s\n" % e)
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

# **api_sounder_operation_external_sync_sync_mode_put**
> api_sounder_operation_external_sync_sync_mode_put(sync_mode=sync_mode)

PutExtSyncMode

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()
sync_mode = 'sync_mode_example' # str |  (optional)

try:
    # PutExtSyncMode
    api_instance.api_sounder_operation_external_sync_sync_mode_put(sync_mode=sync_mode)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_external_sync_sync_mode_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_mode** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_get**
> OperationalState api_sounder_operation_get()

GetOperationalState

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetOperationalState
    api_response = api_instance.api_sounder_operation_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OperationalState**](OperationalState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_operation_mode_get**
> str api_sounder_operation_operation_mode_get()

GetOperationMode

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetOperationMode
    api_response = api_instance.api_sounder_operation_operation_mode_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_operation_mode_get: %s\n" % e)
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

# **api_sounder_operation_operation_mode_put**
> api_sounder_operation_operation_mode_put(operation_mode=operation_mode)

PutOperationMode

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()
operation_mode = 'operation_mode_example' # str |  (optional)

try:
    # PutOperationMode
    api_instance.api_sounder_operation_operation_mode_put(operation_mode=operation_mode)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_operation_mode_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_mode** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_ping_interval_get**
> int api_sounder_operation_ping_interval_get()

GetPingInterval

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetPingInterval
    api_response = api_instance.api_sounder_operation_ping_interval_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_ping_interval_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_ping_interval_put**
> api_sounder_operation_ping_interval_put(ping_interval=ping_interval)

PutPingInterval

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()
ping_interval = 56 # int |  (optional)

try:
    # PutPingInterval
    api_instance.api_sounder_operation_ping_interval_put(ping_interval=ping_interval)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_ping_interval_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ping_interval** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_ping_mode_get**
> str api_sounder_operation_ping_mode_get()

GetPingMode

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetPingMode
    api_response = api_instance.api_sounder_operation_ping_mode_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_ping_mode_get: %s\n" % e)
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

# **api_sounder_operation_ping_mode_put**
> api_sounder_operation_ping_mode_put(ping_mode=ping_mode)

PutPingMode

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()
ping_mode = 'ping_mode_example' # str |  (optional)

try:
    # PutPingMode
    api_instance.api_sounder_operation_ping_mode_put(ping_mode=ping_mode)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_ping_mode_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ping_mode** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_operation_play_state_get**
> str api_sounder_operation_play_state_get()

GetPlayState

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()

try:
    # GetPlayState
    api_response = api_instance.api_sounder_operation_play_state_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_play_state_get: %s\n" % e)
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

# **api_sounder_operation_play_state_put**
> api_sounder_operation_play_state_put(play_state=play_state)

PutPlayState

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.OperationApi()
play_state = 'play_state_example' # str |  (optional)

try:
    # PutPlayState
    api_instance.api_sounder_operation_play_state_put(play_state=play_state)
except ApiException as e:
    print("Exception when calling OperationApi->api_sounder_operation_play_state_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **play_state** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

