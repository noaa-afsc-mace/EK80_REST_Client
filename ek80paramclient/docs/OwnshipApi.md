# ek80paramclient.OwnshipApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_ownship_dimension_get**](OwnshipApi.md#api_ownship_dimension_get) | **GET** /api/ownship/dimension | 
[**api_ownship_get**](OwnshipApi.md#api_ownship_get) | **GET** /api/ownship | 
[**api_ownship_installation_transducer_id_put**](OwnshipApi.md#api_ownship_installation_transducer_id_put) | **PUT** /api/ownship/installation/{transducerId} | 
[**api_ownship_installation_transducers_get**](OwnshipApi.md#api_ownship_installation_transducers_get) | **GET** /api/ownship/installation/transducers | 
[**api_ownship_manual_settings_drop_keel_offset_get**](OwnshipApi.md#api_ownship_manual_settings_drop_keel_offset_get) | **GET** /api/ownship/manual-settings/drop-keel-offset | 
[**api_ownship_manual_settings_drop_keel_offset_put**](OwnshipApi.md#api_ownship_manual_settings_drop_keel_offset_put) | **PUT** /api/ownship/manual-settings/drop-keel-offset | 
[**api_ownship_manual_settings_get**](OwnshipApi.md#api_ownship_manual_settings_get) | **GET** /api/ownship/manual-settings | 
[**api_ownship_manual_settings_vessel_speed_get**](OwnshipApi.md#api_ownship_manual_settings_vessel_speed_get) | **GET** /api/ownship/manual-settings/vessel-speed | 
[**api_ownship_manual_settings_vessel_speed_put**](OwnshipApi.md#api_ownship_manual_settings_vessel_speed_put) | **PUT** /api/ownship/manual-settings/vessel-speed | 
[**api_ownship_manual_settings_water_level_get**](OwnshipApi.md#api_ownship_manual_settings_water_level_get) | **GET** /api/ownship/manual-settings/water-level | 
[**api_ownship_manual_settings_water_level_put**](OwnshipApi.md#api_ownship_manual_settings_water_level_put) | **PUT** /api/ownship/manual-settings/water-level | 
[**api_ownship_motion_get**](OwnshipApi.md#api_ownship_motion_get) | **GET** /api/ownship/motion | 
[**api_ownship_navigation_get**](OwnshipApi.md#api_ownship_navigation_get) | **GET** /api/ownship/navigation | 

# **api_ownship_dimension_get**
> Dimension api_ownship_dimension_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()

try:
    api_response = api_instance.api_ownship_dimension_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_dimension_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Dimension**](Dimension.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_get**
> Ownship api_ownship_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()

try:
    api_response = api_instance.api_ownship_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Ownship**](Ownship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_installation_transducer_id_put**
> api_ownship_installation_transducer_id_put(transducer_id, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()
transducer_id = 'transducer_id_example' # str | 
body = ek80paramclient.Installation() # Installation |  (optional)

try:
    api_instance.api_ownship_installation_transducer_id_put(transducer_id, body=body)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_installation_transducer_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transducer_id** | **str**|  | 
 **body** | [**Installation**](Installation.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_installation_transducers_get**
> dict(str, Installation) api_ownship_installation_transducers_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()

try:
    api_response = api_instance.api_ownship_installation_transducers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_installation_transducers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, Installation)**](Installation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_manual_settings_drop_keel_offset_get**
> ManualSetting api_ownship_manual_settings_drop_keel_offset_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()

try:
    api_response = api_instance.api_ownship_manual_settings_drop_keel_offset_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_manual_settings_drop_keel_offset_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManualSetting**](ManualSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_manual_settings_drop_keel_offset_put**
> api_ownship_manual_settings_drop_keel_offset_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()
body = ek80paramclient.ManualSetting() # ManualSetting |  (optional)

try:
    api_instance.api_ownship_manual_settings_drop_keel_offset_put(body=body)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_manual_settings_drop_keel_offset_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManualSetting**](ManualSetting.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_manual_settings_get**
> dict(str, ManualSetting) api_ownship_manual_settings_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()

try:
    api_response = api_instance.api_ownship_manual_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_manual_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, ManualSetting)**](ManualSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_manual_settings_vessel_speed_get**
> ManualSetting api_ownship_manual_settings_vessel_speed_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()

try:
    api_response = api_instance.api_ownship_manual_settings_vessel_speed_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_manual_settings_vessel_speed_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManualSetting**](ManualSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_manual_settings_vessel_speed_put**
> api_ownship_manual_settings_vessel_speed_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()
body = ek80paramclient.ManualSetting() # ManualSetting |  (optional)

try:
    api_instance.api_ownship_manual_settings_vessel_speed_put(body=body)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_manual_settings_vessel_speed_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManualSetting**](ManualSetting.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_manual_settings_water_level_get**
> ManualSetting api_ownship_manual_settings_water_level_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()

try:
    api_response = api_instance.api_ownship_manual_settings_water_level_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_manual_settings_water_level_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManualSetting**](ManualSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_manual_settings_water_level_put**
> api_ownship_manual_settings_water_level_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()
body = ek80paramclient.ManualSetting() # ManualSetting |  (optional)

try:
    api_instance.api_ownship_manual_settings_water_level_put(body=body)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_manual_settings_water_level_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManualSetting**](ManualSetting.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_motion_get**
> MotionData api_ownship_motion_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()

try:
    api_response = api_instance.api_ownship_motion_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_motion_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MotionData**](MotionData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_ownship_navigation_get**
> NavigationData api_ownship_navigation_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.OwnshipApi()

try:
    api_response = api_instance.api_ownship_navigation_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnshipApi->api_ownship_navigation_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NavigationData**](NavigationData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

