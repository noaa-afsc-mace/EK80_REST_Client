# ek80dataclient.SystemStateSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_system_state_subscriptions_get**](SystemStateSubscriptionsApi.md#api_sounder_data_output_system_state_subscriptions_get) | **GET** /api/sounder/data-output/system-state-subscriptions | GetSystemStateSubscriptions
[**api_sounder_data_output_system_state_subscriptions_post**](SystemStateSubscriptionsApi.md#api_sounder_data_output_system_state_subscriptions_post) | **POST** /api/sounder/data-output/system-state-subscriptions | CreateSystemStateSubscription
[**api_sounder_data_output_system_state_subscriptions_subscription_id_delete**](SystemStateSubscriptionsApi.md#api_sounder_data_output_system_state_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/system-state-subscriptions/{subscriptionId} | DeleteSystemStateSubscription
[**api_sounder_data_output_system_state_subscriptions_subscription_id_get**](SystemStateSubscriptionsApi.md#api_sounder_data_output_system_state_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/system-state-subscriptions/{subscriptionId} | GetSystemStateSubscription
[**api_sounder_data_output_system_state_subscriptions_subscription_id_put**](SystemStateSubscriptionsApi.md#api_sounder_data_output_system_state_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/system-state-subscriptions/{subscriptionId} | UpdateSystemStateSubscription

# **api_sounder_data_output_system_state_subscriptions_get**
> list[SystemStateSubscriptionInfo] api_sounder_data_output_system_state_subscriptions_get()

GetSystemStateSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SystemStateSubscriptionsApi()

try:
    # GetSystemStateSubscriptions
    api_response = api_instance.api_sounder_data_output_system_state_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->api_sounder_data_output_system_state_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SystemStateSubscriptionInfo]**](SystemStateSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_system_state_subscriptions_post**
> int api_sounder_data_output_system_state_subscriptions_post(body=body)

CreateSystemStateSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SystemStateSubscriptionsApi()
body = ek80dataclient.SystemStateSubscriptionSpecification() # SystemStateSubscriptionSpecification |  (optional)

try:
    # CreateSystemStateSubscription
    api_response = api_instance.api_sounder_data_output_system_state_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->api_sounder_data_output_system_state_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemStateSubscriptionSpecification**](SystemStateSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_system_state_subscriptions_subscription_id_delete**
> api_sounder_data_output_system_state_subscriptions_subscription_id_delete(subscription_id)

DeleteSystemStateSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SystemStateSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteSystemStateSubscription
    api_instance.api_sounder_data_output_system_state_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->api_sounder_data_output_system_state_subscriptions_subscription_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_system_state_subscriptions_subscription_id_get**
> SubscriptionSpecificationBase api_sounder_data_output_system_state_subscriptions_subscription_id_get(subscription_id)

GetSystemStateSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SystemStateSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetSystemStateSubscription
    api_response = api_instance.api_sounder_data_output_system_state_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->api_sounder_data_output_system_state_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**SubscriptionSpecificationBase**](SubscriptionSpecificationBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_system_state_subscriptions_subscription_id_put**
> api_sounder_data_output_system_state_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateSystemStateSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SystemStateSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.SystemStateSettings() # SystemStateSettings |  (optional)

try:
    # UpdateSystemStateSubscription
    api_instance.api_sounder_data_output_system_state_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->api_sounder_data_output_system_state_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**SystemStateSettings**](SystemStateSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

