# ek80_data_client.SystemStateSubscriptionsApi

All URIs are relative to *http://localhost:12346*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_system_state_subscription**](SystemStateSubscriptionsApi.md#create_system_state_subscription) | **POST** /api/sounder/data-output/system-state-subscriptions | Create a system state data subscription
[**delete_system_state_subscription**](SystemStateSubscriptionsApi.md#delete_system_state_subscription) | **DELETE** /api/sounder/data-output/system-state-subscriptions/{subscriptionId} | Delete a system state detection data subscription
[**get_system_state_subscription**](SystemStateSubscriptionsApi.md#get_system_state_subscription) | **GET** /api/sounder/data-output/system-state-subscriptions/{subscriptionId} | Get a system state subscription specification
[**get_system_state_subscriptions**](SystemStateSubscriptionsApi.md#get_system_state_subscriptions) | **GET** /api/sounder/data-output/system-state-subscriptions | Get all system state data subscriptions
[**update_system_state_subscription**](SystemStateSubscriptionsApi.md#update_system_state_subscription) | **PUT** /api/sounder/data-output/system-state-subscriptions/{subscriptionId} | Update a system state data subscription


# **create_system_state_subscription**
> int create_system_state_subscription(specification)

Create a system state data subscription

Subscription online help:   <a href=\"https://simrad.online/ek80/interface_en/subscr_type_system_state.html\" target=\"foo\">parameter description</a>.

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SystemStateSubscriptionsApi()
specification = ek80_data_client.SystemStateSubscriptionSpecification() # SystemStateSubscriptionSpecification | Specification of the data requested

try:
    # Create a system state data subscription
    api_response = api_instance.create_system_state_subscription(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->create_system_state_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**SystemStateSubscriptionSpecification**](SystemStateSubscriptionSpecification.md)| Specification of the data requested | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_state_subscription**
> delete_system_state_subscription(subscription_id)

Delete a system state detection data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SystemStateSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # Delete a system state detection data subscription
    api_instance.delete_system_state_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->delete_system_state_subscription: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_state_subscription**
> SubscriptionSpecificationBase get_system_state_subscription(subscription_id)

Get a system state subscription specification

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SystemStateSubscriptionsApi()
subscription_id = 789 # int | The unique id of the subscription

try:
    # Get a system state subscription specification
    api_response = api_instance.get_system_state_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->get_system_state_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The unique id of the subscription | 

### Return type

[**SubscriptionSpecificationBase**](SubscriptionSpecificationBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_state_subscriptions**
> list[SystemStateSubscriptionInfo] get_system_state_subscriptions()

Get all system state data subscriptions

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SystemStateSubscriptionsApi()

try:
    # Get all system state data subscriptions
    api_response = api_instance.get_system_state_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->get_system_state_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SystemStateSubscriptionInfo]**](SystemStateSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system_state_subscription**
> update_system_state_subscription(subscription_id, settings)

Update a system state data subscription

### Example
```python
from __future__ import print_function
import time
import ek80_data_client
from ek80_data_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80_data_client.SystemStateSubscriptionsApi()
subscription_id = 789 # int | Id of the subscription
settings = ek80_data_client.SystemStateSettings() # SystemStateSettings | New subscription settings

try:
    # Update a system state data subscription
    api_instance.update_system_state_subscription(subscription_id, settings)
except ApiException as e:
    print("Exception when calling SystemStateSubscriptionsApi->update_system_state_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| Id of the subscription | 
 **settings** | [**SystemStateSettings**](SystemStateSettings.md)| New subscription settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

