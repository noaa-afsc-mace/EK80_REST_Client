# ek80paramclient.SystemApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_system_active_user_settings_get**](SystemApi.md#api_system_active_user_settings_get) | **GET** /api/system/active-user-settings | 
[**api_system_active_user_settings_put**](SystemApi.md#api_system_active_user_settings_put) | **PUT** /api/system/active-user-settings | 
[**api_system_application_details_get**](SystemApi.md#api_system_application_details_get) | **GET** /api/system/application-details | 
[**api_system_external_sync_delay_get**](SystemApi.md#api_system_external_sync_delay_get) | **GET** /api/system/external-sync/delay | 
[**api_system_external_sync_delay_put**](SystemApi.md#api_system_external_sync_delay_put) | **PUT** /api/system/external-sync/delay | 
[**api_system_external_sync_get**](SystemApi.md#api_system_external_sync_get) | **GET** /api/system/external-sync | 
[**api_system_external_sync_mode_get**](SystemApi.md#api_system_external_sync_mode_get) | **GET** /api/system/external-sync/mode | 
[**api_system_external_sync_mode_put**](SystemApi.md#api_system_external_sync_mode_put) | **PUT** /api/system/external-sync/mode | 
[**api_system_external_sync_put**](SystemApi.md#api_system_external_sync_put) | **PUT** /api/system/external-sync | 
[**api_system_get**](SystemApi.md#api_system_get) | **GET** /api/system | 
[**api_system_operation_mode_get**](SystemApi.md#api_system_operation_mode_get) | **GET** /api/system/operation-mode | 
[**api_system_operation_mode_put**](SystemApi.md#api_system_operation_mode_put) | **PUT** /api/system/operation-mode | 
[**api_system_operational_state_get**](SystemApi.md#api_system_operational_state_get) | **GET** /api/system/operational-state | 
[**api_system_ping_interval_get**](SystemApi.md#api_system_ping_interval_get) | **GET** /api/system/ping-interval | 
[**api_system_ping_interval_put**](SystemApi.md#api_system_ping_interval_put) | **PUT** /api/system/ping-interval | 
[**api_system_ping_mode_get**](SystemApi.md#api_system_ping_mode_get) | **GET** /api/system/ping-mode | 
[**api_system_ping_mode_put**](SystemApi.md#api_system_ping_mode_put) | **PUT** /api/system/ping-mode | 
[**api_system_play_state_get**](SystemApi.md#api_system_play_state_get) | **GET** /api/system/play-state | 
[**api_system_play_state_put**](SystemApi.md#api_system_play_state_put) | **PUT** /api/system/play-state | 

# **api_system_active_user_settings_get**
> str api_system_active_user_settings_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_active_user_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_active_user_settings_get: %s\n" % e)
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

# **api_system_active_user_settings_put**
> api_system_active_user_settings_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.api_system_active_user_settings_put(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_active_user_settings_put: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_application_details_get**
> ApplicationDetails api_system_application_details_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_application_details_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_application_details_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationDetails**](ApplicationDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_external_sync_delay_get**
> int api_system_external_sync_delay_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_external_sync_delay_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_external_sync_delay_get: %s\n" % e)
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

# **api_system_external_sync_delay_put**
> api_system_external_sync_delay_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()
body = 56 # int |  (optional)

try:
    api_instance.api_system_external_sync_delay_put(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_external_sync_delay_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**int**](int.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_external_sync_get**
> ExternalSync api_system_external_sync_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_external_sync_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_external_sync_get: %s\n" % e)
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

# **api_system_external_sync_mode_get**
> str api_system_external_sync_mode_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_external_sync_mode_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_external_sync_mode_get: %s\n" % e)
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

# **api_system_external_sync_mode_put**
> api_system_external_sync_mode_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.api_system_external_sync_mode_put(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_external_sync_mode_put: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_external_sync_put**
> api_system_external_sync_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()
body = ek80paramclient.ExternalSync() # ExternalSync |  (optional)

try:
    api_instance.api_system_external_sync_put(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_external_sync_put: %s\n" % e)
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

# **api_system_get**
> OperationalState api_system_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_get: %s\n" % e)
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

# **api_system_operation_mode_get**
> str api_system_operation_mode_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_operation_mode_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_operation_mode_get: %s\n" % e)
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

# **api_system_operation_mode_put**
> api_system_operation_mode_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.api_system_operation_mode_put(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_operation_mode_put: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_operational_state_get**
> OperationalState api_system_operational_state_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_operational_state_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_operational_state_get: %s\n" % e)
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

# **api_system_ping_interval_get**
> int api_system_ping_interval_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_ping_interval_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_ping_interval_get: %s\n" % e)
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

# **api_system_ping_interval_put**
> api_system_ping_interval_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()
body = 56 # int |  (optional)

try:
    api_instance.api_system_ping_interval_put(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_ping_interval_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**int**](int.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_ping_mode_get**
> str api_system_ping_mode_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_ping_mode_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_ping_mode_get: %s\n" % e)
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

# **api_system_ping_mode_put**
> api_system_ping_mode_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.api_system_ping_mode_put(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_ping_mode_put: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_system_play_state_get**
> str api_system_play_state_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()

try:
    api_response = api_instance.api_system_play_state_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_play_state_get: %s\n" % e)
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

# **api_system_play_state_put**
> api_system_play_state_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.SystemApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.api_system_play_state_put(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->api_system_play_state_put: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

