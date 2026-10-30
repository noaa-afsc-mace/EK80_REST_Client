# ek80dataclient.CommunicationEndPointsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_delete**](CommunicationEndPointsApi.md#api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_delete) | **DELETE** /api/sounder/data-output/communication-end-points/{endPointId}/data-subscriptions | RemoveSubscriptionFromEndPoint
[**api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_get**](CommunicationEndPointsApi.md#api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_get) | **GET** /api/sounder/data-output/communication-end-points/{endPointId}/data-subscriptions | GetSubscriptionsByEndPoint
[**api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_post**](CommunicationEndPointsApi.md#api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_post) | **POST** /api/sounder/data-output/communication-end-points/{endPointId}/data-subscriptions | AddSubscriptionToEndPoint
[**api_sounder_data_output_communication_end_points_end_point_id_delete**](CommunicationEndPointsApi.md#api_sounder_data_output_communication_end_points_end_point_id_delete) | **DELETE** /api/sounder/data-output/communication-end-points/{endPointId} | DeleteCommunicationEndPoint
[**api_sounder_data_output_communication_end_points_get**](CommunicationEndPointsApi.md#api_sounder_data_output_communication_end_points_get) | **GET** /api/sounder/data-output/communication-end-points | GetActiveCommunicationEndPoints
[**api_sounder_data_output_communication_end_points_post**](CommunicationEndPointsApi.md#api_sounder_data_output_communication_end_points_post) | **POST** /api/sounder/data-output/communication-end-points | CreateCommunicationEndPoint

# **api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_delete**
> api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_delete(end_point_id, subscription_id=subscription_id)

RemoveSubscriptionFromEndPoint

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CommunicationEndPointsApi()
end_point_id = 789 # int | 
subscription_id = 789 # int |  (optional)

try:
    # RemoveSubscriptionFromEndPoint
    api_instance.api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_delete(end_point_id, subscription_id=subscription_id)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_point_id** | **int**|  | 
 **subscription_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_get**
> list[SubscriptionSummary] api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_get(end_point_id)

GetSubscriptionsByEndPoint

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CommunicationEndPointsApi()
end_point_id = 789 # int | 

try:
    # GetSubscriptionsByEndPoint
    api_response = api_instance.api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_get(end_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_point_id** | **int**|  | 

### Return type

[**list[SubscriptionSummary]**](SubscriptionSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_post**
> api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_post(end_point_id, body=body)

AddSubscriptionToEndPoint

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CommunicationEndPointsApi()
end_point_id = 789 # int | 
body = ek80dataclient.SubscriptionOutputArgs() # SubscriptionOutputArgs |  (optional)

try:
    # AddSubscriptionToEndPoint
    api_instance.api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_post(end_point_id, body=body)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->api_sounder_data_output_communication_end_points_end_point_id_data_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_point_id** | **int**|  | 
 **body** | [**SubscriptionOutputArgs**](SubscriptionOutputArgs.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_communication_end_points_end_point_id_delete**
> api_sounder_data_output_communication_end_points_end_point_id_delete(end_point_id)

DeleteCommunicationEndPoint

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CommunicationEndPointsApi()
end_point_id = 789 # int | 

try:
    # DeleteCommunicationEndPoint
    api_instance.api_sounder_data_output_communication_end_points_end_point_id_delete(end_point_id)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->api_sounder_data_output_communication_end_points_end_point_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_point_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_communication_end_points_get**
> list[CommunicationEndPointInfo] api_sounder_data_output_communication_end_points_get()

GetActiveCommunicationEndPoints

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CommunicationEndPointsApi()

try:
    # GetActiveCommunicationEndPoints
    api_response = api_instance.api_sounder_data_output_communication_end_points_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->api_sounder_data_output_communication_end_points_get: %s\n" % e)
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

# **api_sounder_data_output_communication_end_points_post**
> int api_sounder_data_output_communication_end_points_post(body=body)

CreateCommunicationEndPoint

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CommunicationEndPointsApi()
body = ek80dataclient.CommunicationEndPointSettings() # CommunicationEndPointSettings |  (optional)

try:
    # CreateCommunicationEndPoint
    api_response = api_instance.api_sounder_data_output_communication_end_points_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationEndPointsApi->api_sounder_data_output_communication_end_points_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommunicationEndPointSettings**](CommunicationEndPointSettings.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

