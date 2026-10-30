# ek80paramclient.PingConfigurationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_ping_configuration_channel_list_get**](PingConfigurationApi.md#api_sounder_ping_configuration_channel_list_get) | **GET** /api/sounder/ping-configuration/channel-list | 
[**api_sounder_ping_configuration_channelid_adcp_get**](PingConfigurationApi.md#api_sounder_ping_configuration_channelid_adcp_get) | **GET** /api/sounder/ping-configuration/{channelid}/adcp | 
[**api_sounder_ping_configuration_channelid_adcp_put**](PingConfigurationApi.md#api_sounder_ping_configuration_channelid_adcp_put) | **PUT** /api/sounder/ping-configuration/{channelid}/adcp | 
[**api_sounder_ping_configuration_channelid_pulse_settings_get**](PingConfigurationApi.md#api_sounder_ping_configuration_channelid_pulse_settings_get) | **GET** /api/sounder/ping-configuration/{channelid}/pulse-settings | 
[**api_sounder_ping_configuration_channelid_pulse_settings_put**](PingConfigurationApi.md#api_sounder_ping_configuration_channelid_pulse_settings_put) | **PUT** /api/sounder/ping-configuration/{channelid}/pulse-settings | 
[**api_sounder_ping_configuration_channelid_transmit_power_get**](PingConfigurationApi.md#api_sounder_ping_configuration_channelid_transmit_power_get) | **GET** /api/sounder/ping-configuration/{channelid}/transmit-power | 
[**api_sounder_ping_configuration_channelid_transmit_power_put**](PingConfigurationApi.md#api_sounder_ping_configuration_channelid_transmit_power_put) | **PUT** /api/sounder/ping-configuration/{channelid}/transmit-power | 
[**api_sounder_ping_configuration_sequencing_get**](PingConfigurationApi.md#api_sounder_ping_configuration_sequencing_get) | **GET** /api/sounder/ping-configuration/sequencing | 
[**api_sounder_ping_configuration_sequencing_put**](PingConfigurationApi.md#api_sounder_ping_configuration_sequencing_put) | **PUT** /api/sounder/ping-configuration/sequencing | 

# **api_sounder_ping_configuration_channel_list_get**
> list[str] api_sounder_ping_configuration_channel_list_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingConfigurationApi()

try:
    api_response = api_instance.api_sounder_ping_configuration_channel_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->api_sounder_ping_configuration_channel_list_get: %s\n" % e)
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

# **api_sounder_ping_configuration_channelid_adcp_get**
> AdcpConfigurationEc150 api_sounder_ping_configuration_channelid_adcp_get(channelid)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingConfigurationApi()
channelid = 'channelid_example' # str | 

try:
    api_response = api_instance.api_sounder_ping_configuration_channelid_adcp_get(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->api_sounder_ping_configuration_channelid_adcp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 

### Return type

[**AdcpConfigurationEc150**](AdcpConfigurationEc150.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_ping_configuration_channelid_adcp_put**
> api_sounder_ping_configuration_channelid_adcp_put(channelid, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingConfigurationApi()
channelid = 'channelid_example' # str | 
body = ek80paramclient.AdcpConfigurationEc150() # AdcpConfigurationEc150 |  (optional)

try:
    api_instance.api_sounder_ping_configuration_channelid_adcp_put(channelid, body=body)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->api_sounder_ping_configuration_channelid_adcp_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 
 **body** | [**AdcpConfigurationEc150**](AdcpConfigurationEc150.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_ping_configuration_channelid_pulse_settings_get**
> PulseSettings api_sounder_ping_configuration_channelid_pulse_settings_get(channelid)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingConfigurationApi()
channelid = 'channelid_example' # str | 

try:
    api_response = api_instance.api_sounder_ping_configuration_channelid_pulse_settings_get(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->api_sounder_ping_configuration_channelid_pulse_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 

### Return type

[**PulseSettings**](PulseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_ping_configuration_channelid_pulse_settings_put**
> api_sounder_ping_configuration_channelid_pulse_settings_put(channelid, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingConfigurationApi()
channelid = 'channelid_example' # str | 
body = ek80paramclient.PulseSettings() # PulseSettings |  (optional)

try:
    api_instance.api_sounder_ping_configuration_channelid_pulse_settings_put(channelid, body=body)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->api_sounder_ping_configuration_channelid_pulse_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 
 **body** | [**PulseSettings**](PulseSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_ping_configuration_channelid_transmit_power_get**
> float api_sounder_ping_configuration_channelid_transmit_power_get(channelid)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingConfigurationApi()
channelid = 'channelid_example' # str | 

try:
    api_response = api_instance.api_sounder_ping_configuration_channelid_transmit_power_get(channelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->api_sounder_ping_configuration_channelid_transmit_power_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_ping_configuration_channelid_transmit_power_put**
> api_sounder_ping_configuration_channelid_transmit_power_put(channelid, body=body)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingConfigurationApi()
channelid = 'channelid_example' # str | 
body = 3.4 # float |  (optional)

try:
    api_instance.api_sounder_ping_configuration_channelid_transmit_power_put(channelid, body=body)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->api_sounder_ping_configuration_channelid_transmit_power_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelid** | **str**|  | 
 **body** | [**float**](float.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_ping_configuration_sequencing_get**
> bool api_sounder_ping_configuration_sequencing_get()



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingConfigurationApi()

try:
    api_response = api_instance.api_sounder_ping_configuration_sequencing_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->api_sounder_ping_configuration_sequencing_get: %s\n" % e)
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

# **api_sounder_ping_configuration_sequencing_put**
> api_sounder_ping_configuration_sequencing_put(sequencing=sequencing)



### Example
```python
from __future__ import print_function
import time
import ek80paramclient
from ek80paramclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80paramclient.PingConfigurationApi()
sequencing = true # bool |  (optional)

try:
    api_instance.api_sounder_ping_configuration_sequencing_put(sequencing=sequencing)
except ApiException as e:
    print("Exception when calling PingConfigurationApi->api_sounder_ping_configuration_sequencing_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequencing** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

