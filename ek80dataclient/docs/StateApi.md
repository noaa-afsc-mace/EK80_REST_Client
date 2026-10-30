# ek80dataclient.StateApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_state_communication_end_points_get**](StateApi.md#api_sounder_data_output_state_communication_end_points_get) | **GET** /api/sounder/data-output/state/communication-end-points | GetActiveCommunicationEndPoints
[**api_sounder_data_output_state_data_sources_get**](StateApi.md#api_sounder_data_output_state_data_sources_get) | **GET** /api/sounder/data-output/state/data-sources | GetAvailableDataSources
[**api_sounder_data_output_state_get**](StateApi.md#api_sounder_data_output_state_get) | **GET** /api/sounder/data-output/state | GetDataOutputState
[**api_sounder_data_output_state_subscription_summary_get**](StateApi.md#api_sounder_data_output_state_subscription_summary_get) | **GET** /api/sounder/data-output/state/subscription-summary | GetSubscriptionSummaries

# **api_sounder_data_output_state_communication_end_points_get**
> list[CommunicationEndPointInfo] api_sounder_data_output_state_communication_end_points_get()

GetActiveCommunicationEndPoints

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.StateApi()

try:
    # GetActiveCommunicationEndPoints
    api_response = api_instance.api_sounder_data_output_state_communication_end_points_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->api_sounder_data_output_state_communication_end_points_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CommunicationEndPointInfo]**](CommunicationEndPointInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_state_data_sources_get**
> list[str] api_sounder_data_output_state_data_sources_get()

GetAvailableDataSources

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.StateApi()

try:
    # GetAvailableDataSources
    api_response = api_instance.api_sounder_data_output_state_data_sources_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->api_sounder_data_output_state_data_sources_get: %s\n" % e)
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

# **api_sounder_data_output_state_get**
> DataOutputState api_sounder_data_output_state_get()

GetDataOutputState

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.StateApi()

try:
    # GetDataOutputState
    api_response = api_instance.api_sounder_data_output_state_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->api_sounder_data_output_state_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DataOutputState**](DataOutputState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_state_subscription_summary_get**
> list[SubscriptionSummary] api_sounder_data_output_state_subscription_summary_get()

GetSubscriptionSummaries

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.StateApi()

try:
    # GetSubscriptionSummaries
    api_response = api_instance.api_sounder_data_output_state_subscription_summary_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateApi->api_sounder_data_output_state_subscription_summary_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SubscriptionSummary]**](SubscriptionSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

