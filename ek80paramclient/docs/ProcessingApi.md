# ek80paramclient.ProcessingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_processing_adcp_get**](ProcessingApi.md#api_sounder_processing_adcp_get) | **GET** /api/sounder/processing/adcp | 
[**api_sounder_processing_calculation_interval_get**](ProcessingApi.md#api_sounder_processing_calculation_interval_get) | **GET** /api/sounder/processing/calculation-interval | 
[**api_sounder_processing_calculation_interval_put**](ProcessingApi.md#api_sounder_processing_calculation_interval_put) | **PUT** /api/sounder/processing/calculation-interval | 
[**api_sounder_processing_channel_name_adcp_correlation_limit_percentage_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_correlation_limit_percentage_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/correlation-limit-percentage | 
[**api_sounder_processing_channel_name_adcp_error_velocity_limit_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_error_velocity_limit_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/error-velocity-limit | 
[**api_sounder_processing_channel_name_adcp_get**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_get) | **GET** /api/sounder/processing/{channel_name}/adcp | 
[**api_sounder_processing_channel_name_adcp_is_correlation_limit_percentage_active_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_is_correlation_limit_percentage_active_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-correlation-limit-percentage-active | 
[**api_sounder_processing_channel_name_adcp_is_error_velocity_limit_active_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_is_error_velocity_limit_active_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-error-velocity-limit-active | 
[**api_sounder_processing_channel_name_adcp_is_min_quality_average_data_factor_active_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_is_min_quality_average_data_factor_active_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-min-quality-average-data-factor-active | 
[**api_sounder_processing_channel_name_adcp_is_sv_db_high_limit_active_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_is_sv_db_high_limit_active_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-sv-dB-high-limit-active | 
[**api_sounder_processing_channel_name_adcp_is_sv_db_low_limit_active_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_is_sv_db_low_limit_active_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/is-sv-dB-low-limit-active | 
[**api_sounder_processing_channel_name_adcp_min_quality_average_data_percentage_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_min_quality_average_data_percentage_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/min-quality-average-data-percentage | 
[**api_sounder_processing_channel_name_adcp_sv_db_high_limit_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_sv_db_high_limit_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/sv-dB-high-limit | 
[**api_sounder_processing_channel_name_adcp_sv_db_low_limit_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_sv_db_low_limit_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/sv-dB-low-limit | 
[**api_sounder_processing_channel_name_adcp_use_epoch_time_put**](ProcessingApi.md#api_sounder_processing_channel_name_adcp_use_epoch_time_put) | **PUT** /api/sounder/processing/{channel_name}/adcp/use-epoch-time | 
[**api_sounder_processing_channel_name_bottom_detection_bottom_backstep_put**](ProcessingApi.md#api_sounder_processing_channel_name_bottom_detection_bottom_backstep_put) | **PUT** /api/sounder/processing/{channel_name}/bottom-detection/bottom-backstep | 
[**api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_get**](ProcessingApi.md#api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_get) | **GET** /api/sounder/processing/{channel_name}/bottom-detection/bottom-detection-active | 
[**api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_put**](ProcessingApi.md#api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_put) | **PUT** /api/sounder/processing/{channel_name}/bottom-detection/bottom-detection-active | 
[**api_sounder_processing_channel_name_bottom_detection_get**](ProcessingApi.md#api_sounder_processing_channel_name_bottom_detection_get) | **GET** /api/sounder/processing/{channel_name}/bottom-detection | 
[**api_sounder_processing_channel_name_bottom_detection_maximum_depth_put**](ProcessingApi.md#api_sounder_processing_channel_name_bottom_detection_maximum_depth_put) | **PUT** /api/sounder/processing/{channel_name}/bottom-detection/maximum-depth | 
[**api_sounder_processing_channel_name_bottom_detection_minimum_depth_put**](ProcessingApi.md#api_sounder_processing_channel_name_bottom_detection_minimum_depth_put) | **PUT** /api/sounder/processing/{channel_name}/bottom-detection/minimum-depth | 
[**api_sounder_processing_channel_name_bottom_detection_put**](ProcessingApi.md#api_sounder_processing_channel_name_bottom_detection_put) | **PUT** /api/sounder/processing/{channel_name}/bottom-detection | 

# **api_sounder_processing_adcp_get**
> ProcessingAdcp api_sounder_processing_adcp_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()

try:
    api_response = api_instance.api_sounder_processing_adcp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_adcp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessingAdcp**](ProcessingAdcp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_calculation_interval_get**
> SounderCalculationInterval api_sounder_processing_calculation_interval_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()

try:
    api_response = api_instance.api_sounder_processing_calculation_interval_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_calculation_interval_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SounderCalculationInterval**](SounderCalculationInterval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_calculation_interval_put**
> api_sounder_processing_calculation_interval_put(body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
body = ek80paramclient.SounderCalculationInterval() # SounderCalculationInterval |  (optional)

try:
    api_instance.api_sounder_processing_calculation_interval_put(body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_calculation_interval_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SounderCalculationInterval**](SounderCalculationInterval.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_correlation_limit_percentage_put**
> api_sounder_processing_channel_name_adcp_correlation_limit_percentage_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = 3.4 # float |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_correlation_limit_percentage_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_correlation_limit_percentage_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**float**](float.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_error_velocity_limit_put**
> api_sounder_processing_channel_name_adcp_error_velocity_limit_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = 3.4 # float |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_error_velocity_limit_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_error_velocity_limit_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**float**](float.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_get**
> ProcessingAdcp api_sounder_processing_channel_name_adcp_get(channel_name)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 

try:
    api_response = api_instance.api_sounder_processing_channel_name_adcp_get(channel_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 

### Return type

[**ProcessingAdcp**](ProcessingAdcp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_is_correlation_limit_percentage_active_put**
> api_sounder_processing_channel_name_adcp_is_correlation_limit_percentage_active_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = True # bool |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_is_correlation_limit_percentage_active_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_is_correlation_limit_percentage_active_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**bool**](bool.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_is_error_velocity_limit_active_put**
> api_sounder_processing_channel_name_adcp_is_error_velocity_limit_active_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = True # bool |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_is_error_velocity_limit_active_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_is_error_velocity_limit_active_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**bool**](bool.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_is_min_quality_average_data_factor_active_put**
> api_sounder_processing_channel_name_adcp_is_min_quality_average_data_factor_active_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = True # bool |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_is_min_quality_average_data_factor_active_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_is_min_quality_average_data_factor_active_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**bool**](bool.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_is_sv_db_high_limit_active_put**
> api_sounder_processing_channel_name_adcp_is_sv_db_high_limit_active_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = True # bool |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_is_sv_db_high_limit_active_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_is_sv_db_high_limit_active_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**bool**](bool.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_is_sv_db_low_limit_active_put**
> api_sounder_processing_channel_name_adcp_is_sv_db_low_limit_active_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = True # bool |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_is_sv_db_low_limit_active_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_is_sv_db_low_limit_active_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**bool**](bool.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_min_quality_average_data_percentage_put**
> api_sounder_processing_channel_name_adcp_min_quality_average_data_percentage_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = 3.4 # float |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_min_quality_average_data_percentage_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_min_quality_average_data_percentage_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**float**](float.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_sv_db_high_limit_put**
> api_sounder_processing_channel_name_adcp_sv_db_high_limit_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = 56 # int |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_sv_db_high_limit_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_sv_db_high_limit_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**int**](int.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_sv_db_low_limit_put**
> api_sounder_processing_channel_name_adcp_sv_db_low_limit_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = 56 # int |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_sv_db_low_limit_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_sv_db_low_limit_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**int**](int.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_adcp_use_epoch_time_put**
> api_sounder_processing_channel_name_adcp_use_epoch_time_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = True # bool |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_adcp_use_epoch_time_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_adcp_use_epoch_time_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**bool**](bool.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_bottom_detection_bottom_backstep_put**
> api_sounder_processing_channel_name_bottom_detection_bottom_backstep_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = 3.4 # float |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_bottom_detection_bottom_backstep_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_bottom_detection_bottom_backstep_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**float**](float.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_get**
> bool api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_get(channel_name)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 

try:
    api_response = api_instance.api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_get(channel_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_put**
> api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = True # bool |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_bottom_detection_bottom_detection_active_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**bool**](bool.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_bottom_detection_get**
> SounderBottomDetection api_sounder_processing_channel_name_bottom_detection_get(channel_name)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 

try:
    api_response = api_instance.api_sounder_processing_channel_name_bottom_detection_get(channel_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_bottom_detection_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 

### Return type

[**SounderBottomDetection**](SounderBottomDetection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_bottom_detection_maximum_depth_put**
> api_sounder_processing_channel_name_bottom_detection_maximum_depth_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = 3.4 # float |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_bottom_detection_maximum_depth_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_bottom_detection_maximum_depth_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**float**](float.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_bottom_detection_minimum_depth_put**
> api_sounder_processing_channel_name_bottom_detection_minimum_depth_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = 3.4 # float |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_bottom_detection_minimum_depth_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_bottom_detection_minimum_depth_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**float**](float.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_processing_channel_name_bottom_detection_put**
> api_sounder_processing_channel_name_bottom_detection_put(channel_name, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.ProcessingApi()
channel_name = 'channel_name_example' # str | 
body = ek80paramclient.SounderBottomDetection() # SounderBottomDetection |  (optional)

try:
    api_instance.api_sounder_processing_channel_name_bottom_detection_put(channel_name, body=body)
except ApiException as e:
    print("Exception when calling ProcessingApi->api_sounder_processing_channel_name_bottom_detection_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_name** | **str**|  | 
 **body** | [**SounderBottomDetection**](SounderBottomDetection.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

