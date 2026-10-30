# ek80dataclient.IntegrationSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_integration_subscriptions_get**](IntegrationSubscriptionsApi.md#api_sounder_data_output_integration_subscriptions_get) | **GET** /api/sounder/data-output/integration-subscriptions | GetIntegrationSubscriptions
[**api_sounder_data_output_integration_subscriptions_post**](IntegrationSubscriptionsApi.md#api_sounder_data_output_integration_subscriptions_post) | **POST** /api/sounder/data-output/integration-subscriptions | CreateIntegrationSubscription
[**api_sounder_data_output_integration_subscriptions_subscription_id_delete**](IntegrationSubscriptionsApi.md#api_sounder_data_output_integration_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/integration-subscriptions/{subscriptionId} | DeleteIntegrationSubscription
[**api_sounder_data_output_integration_subscriptions_subscription_id_get**](IntegrationSubscriptionsApi.md#api_sounder_data_output_integration_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/integration-subscriptions/{subscriptionId} | GetIntegrationSubscription
[**api_sounder_data_output_integration_subscriptions_subscription_id_integration_state_put**](IntegrationSubscriptionsApi.md#api_sounder_data_output_integration_subscriptions_subscription_id_integration_state_put) | **PUT** /api/sounder/data-output/integration-subscriptions/{subscriptionId}/integration-state | UpdateIntegrationState
[**api_sounder_data_output_integration_subscriptions_subscription_id_put**](IntegrationSubscriptionsApi.md#api_sounder_data_output_integration_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/integration-subscriptions/{subscriptionId} | UpdateIntegrationSubscription

# **api_sounder_data_output_integration_subscriptions_get**
> list[IntegrationSubscriptionInfo] api_sounder_data_output_integration_subscriptions_get()

GetIntegrationSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationSubscriptionsApi()

try:
    # GetIntegrationSubscriptions
    api_response = api_instance.api_sounder_data_output_integration_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->api_sounder_data_output_integration_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IntegrationSubscriptionInfo]**](IntegrationSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_integration_subscriptions_post**
> int api_sounder_data_output_integration_subscriptions_post(body=body)

CreateIntegrationSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationSubscriptionsApi()
body = ek80dataclient.IntegrationSubscriptionSpecification() # IntegrationSubscriptionSpecification |  (optional)

try:
    # CreateIntegrationSubscription
    api_response = api_instance.api_sounder_data_output_integration_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->api_sounder_data_output_integration_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntegrationSubscriptionSpecification**](IntegrationSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_integration_subscriptions_subscription_id_delete**
> api_sounder_data_output_integration_subscriptions_subscription_id_delete(subscription_id)

DeleteIntegrationSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteIntegrationSubscription
    api_instance.api_sounder_data_output_integration_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->api_sounder_data_output_integration_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_integration_subscriptions_subscription_id_get**
> IntegrationSubscriptionSpecification api_sounder_data_output_integration_subscriptions_subscription_id_get(subscription_id)

GetIntegrationSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetIntegrationSubscription
    api_response = api_instance.api_sounder_data_output_integration_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->api_sounder_data_output_integration_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**IntegrationSubscriptionSpecification**](IntegrationSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_integration_subscriptions_subscription_id_integration_state_put**
> api_sounder_data_output_integration_subscriptions_subscription_id_integration_state_put(subscription_id, state=state)

UpdateIntegrationState

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationSubscriptionsApi()
subscription_id = 789 # int | 
state = 'state_example' # str |  (optional)

try:
    # UpdateIntegrationState
    api_instance.api_sounder_data_output_integration_subscriptions_subscription_id_integration_state_put(subscription_id, state=state)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->api_sounder_data_output_integration_subscriptions_subscription_id_integration_state_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **state** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_integration_subscriptions_subscription_id_put**
> api_sounder_data_output_integration_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateIntegrationSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.IntegrationSettings() # IntegrationSettings |  (optional)

try:
    # UpdateIntegrationSubscription
    api_instance.api_sounder_data_output_integration_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling IntegrationSubscriptionsApi->api_sounder_data_output_integration_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**IntegrationSettings**](IntegrationSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

