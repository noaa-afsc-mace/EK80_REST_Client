# ek80paramclient.DisplayApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_display_display_palette_get**](DisplayApi.md#api_display_display_palette_get) | **GET** /api/display/display-palette | 
[**api_display_display_palette_put**](DisplayApi.md#api_display_display_palette_put) | **PUT** /api/display/display-palette | 
[**api_display_echo_colours_get**](DisplayApi.md#api_display_echo_colours_get) | **GET** /api/display/echo-colours | 
[**api_display_echo_colours_put**](DisplayApi.md#api_display_echo_colours_put) | **PUT** /api/display/echo-colours | 
[**api_display_full_screen_get**](DisplayApi.md#api_display_full_screen_get) | **GET** /api/display/full-screen | 
[**api_display_full_screen_put**](DisplayApi.md#api_display_full_screen_put) | **PUT** /api/display/full-screen | 
[**api_display_get**](DisplayApi.md#api_display_get) | **GET** /api/display | 
[**api_display_gui_locked_get**](DisplayApi.md#api_display_gui_locked_get) | **GET** /api/display/gui-locked | 
[**api_display_gui_locked_put**](DisplayApi.md#api_display_gui_locked_put) | **PUT** /api/display/gui-locked | 
[**api_display_screen_brightness_get**](DisplayApi.md#api_display_screen_brightness_get) | **GET** /api/display/screen-brightness | 
[**api_display_screen_brightness_put**](DisplayApi.md#api_display_screen_brightness_put) | **PUT** /api/display/screen-brightness | 
[**api_display_settings_get**](DisplayApi.md#api_display_settings_get) | **GET** /api/display/settings | 
[**api_display_settings_put**](DisplayApi.md#api_display_settings_put) | **PUT** /api/display/settings | 

# **api_display_display_palette_get**
> str api_display_display_palette_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()

try:
    api_response = api_instance.api_display_display_palette_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_display_palette_get: %s\n" % e)
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

# **api_display_display_palette_put**
> api_display_display_palette_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.api_display_display_palette_put(body=body)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_display_palette_put: %s\n" % e)
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

# **api_display_echo_colours_get**
> str api_display_echo_colours_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()

try:
    api_response = api_instance.api_display_echo_colours_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_echo_colours_get: %s\n" % e)
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

# **api_display_echo_colours_put**
> api_display_echo_colours_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()
body = 'body_example' # str |  (optional)

try:
    api_instance.api_display_echo_colours_put(body=body)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_echo_colours_put: %s\n" % e)
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

# **api_display_full_screen_get**
> bool api_display_full_screen_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()

try:
    api_response = api_instance.api_display_full_screen_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_full_screen_get: %s\n" % e)
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

# **api_display_full_screen_put**
> api_display_full_screen_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()
body = True # bool |  (optional)

try:
    api_instance.api_display_full_screen_put(body=body)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_full_screen_put: %s\n" % e)
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

# **api_display_get**
> DisplaySettings api_display_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()

try:
    api_response = api_instance.api_display_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplaySettings**](DisplaySettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_display_gui_locked_get**
> api_display_gui_locked_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()

try:
    api_instance.api_display_gui_locked_get()
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_gui_locked_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_display_gui_locked_put**
> api_display_gui_locked_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()
body = True # bool |  (optional)

try:
    api_instance.api_display_gui_locked_put(body=body)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_gui_locked_put: %s\n" % e)
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

# **api_display_screen_brightness_get**
> int api_display_screen_brightness_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()

try:
    api_response = api_instance.api_display_screen_brightness_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_screen_brightness_get: %s\n" % e)
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

# **api_display_screen_brightness_put**
> api_display_screen_brightness_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()
body = 56 # int |  (optional)

try:
    api_instance.api_display_screen_brightness_put(body=body)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_screen_brightness_put: %s\n" % e)
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

# **api_display_settings_get**
> DisplaySettings api_display_settings_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()

try:
    api_response = api_instance.api_display_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DisplaySettings**](DisplaySettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_display_settings_put**
> api_display_settings_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.DisplayApi()
body = ek80paramclient.DisplaySettings() # DisplaySettings |  (optional)

try:
    api_instance.api_display_settings_put(body=body)
except ApiException as e:
    print("Exception when calling DisplayApi->api_display_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DisplaySettings**](DisplaySettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

