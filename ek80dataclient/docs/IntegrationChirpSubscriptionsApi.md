# ek80dataclient.IntegrationChirpSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_integration_chirp_subscriptions_get**](IntegrationChirpSubscriptionsApi.md#api_sounder_data_output_integration_chirp_subscriptions_get) | **GET** /api/sounder/data-output/integration-chirp-subscriptions | GetIntegrationChirpSubscriptions
[**api_sounder_data_output_integration_chirp_subscriptions_post**](IntegrationChirpSubscriptionsApi.md#api_sounder_data_output_integration_chirp_subscriptions_post) | **POST** /api/sounder/data-output/integration-chirp-subscriptions | CreateIntegrationChirpSubscription
[**api_sounder_data_output_integration_chirp_subscriptions_subscription_id_delete**](IntegrationChirpSubscriptionsApi.md#api_sounder_data_output_integration_chirp_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId} | DeleteIntegrationChirpSubscription
[**api_sounder_data_output_integration_chirp_subscriptions_subscription_id_get**](IntegrationChirpSubscriptionsApi.md#api_sounder_data_output_integration_chirp_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId} | GetIntegrationChirpSubscription
[**api_sounder_data_output_integration_chirp_subscriptions_subscription_id_integration_state_put**](IntegrationChirpSubscriptionsApi.md#api_sounder_data_output_integration_chirp_subscriptions_subscription_id_integration_state_put) | **PUT** /api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId}/integration-state | UpdateIntegrationState
[**api_sounder_data_output_integration_chirp_subscriptions_subscription_id_put**](IntegrationChirpSubscriptionsApi.md#api_sounder_data_output_integration_chirp_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/integration-chirp-subscriptions/{subscriptionId} | UpdateIntegrationChirpSubscription

# **api_sounder_data_output_integration_chirp_subscriptions_get**
> list[IntegrationChirpSubscriptionInfo] api_sounder_data_output_integration_chirp_subscriptions_get()

GetIntegrationChirpSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationChirpSubscriptionsApi()

try:
    # GetIntegrationChirpSubscriptions
    api_response = api_instance.api_sounder_data_output_integration_chirp_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->api_sounder_data_output_integration_chirp_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IntegrationChirpSubscriptionInfo]**](IntegrationChirpSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_integration_chirp_subscriptions_post**
> int api_sounder_data_output_integration_chirp_subscriptions_post(body=body)

CreateIntegrationChirpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationChirpSubscriptionsApi()
body = ek80dataclient.IntegrationChirpSubscriptionSpecification() # IntegrationChirpSubscriptionSpecification |  (optional)

try:
    # CreateIntegrationChirpSubscription
    api_response = api_instance.api_sounder_data_output_integration_chirp_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->api_sounder_data_output_integration_chirp_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntegrationChirpSubscriptionSpecification**](IntegrationChirpSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_integration_chirp_subscriptions_subscription_id_delete**
> api_sounder_data_output_integration_chirp_subscriptions_subscription_id_delete(subscription_id)

DeleteIntegrationChirpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationChirpSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteIntegrationChirpSubscription
    api_instance.api_sounder_data_output_integration_chirp_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->api_sounder_data_output_integration_chirp_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_integration_chirp_subscriptions_subscription_id_get**
> IntegrationChirpSubscriptionSpecification api_sounder_data_output_integration_chirp_subscriptions_subscription_id_get(subscription_id)

GetIntegrationChirpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationChirpSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetIntegrationChirpSubscription
    api_response = api_instance.api_sounder_data_output_integration_chirp_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->api_sounder_data_output_integration_chirp_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**IntegrationChirpSubscriptionSpecification**](IntegrationChirpSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_integration_chirp_subscriptions_subscription_id_integration_state_put**
> api_sounder_data_output_integration_chirp_subscriptions_subscription_id_integration_state_put(subscription_id, state=state)

UpdateIntegrationState

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationChirpSubscriptionsApi()
subscription_id = 789 # int | 
state = 'state_example' # str |  (optional)

try:
    # UpdateIntegrationState
    api_instance.api_sounder_data_output_integration_chirp_subscriptions_subscription_id_integration_state_put(subscription_id, state=state)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->api_sounder_data_output_integration_chirp_subscriptions_subscription_id_integration_state_put: %s\n" % e)
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

# **api_sounder_data_output_integration_chirp_subscriptions_subscription_id_put**
> api_sounder_data_output_integration_chirp_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateIntegrationChirpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.IntegrationChirpSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.IntegrationChirpSettings() # IntegrationChirpSettings |  (optional)

try:
    # UpdateIntegrationChirpSubscription
    api_instance.api_sounder_data_output_integration_chirp_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling IntegrationChirpSubscriptionsApi->api_sounder_data_output_integration_chirp_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**IntegrationChirpSettings**](IntegrationChirpSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

