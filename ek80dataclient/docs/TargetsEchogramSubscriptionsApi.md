# ek80dataclient.TargetsEchogramSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_targets_echogram_subscriptions_get**](TargetsEchogramSubscriptionsApi.md#api_sounder_data_output_targets_echogram_subscriptions_get) | **GET** /api/sounder/data-output/targets-echogram-subscriptions | GetTargetsEchogramSubscriptions
[**api_sounder_data_output_targets_echogram_subscriptions_post**](TargetsEchogramSubscriptionsApi.md#api_sounder_data_output_targets_echogram_subscriptions_post) | **POST** /api/sounder/data-output/targets-echogram-subscriptions | CreateTargetsEchogramSubscription
[**api_sounder_data_output_targets_echogram_subscriptions_subscription_id_delete**](TargetsEchogramSubscriptionsApi.md#api_sounder_data_output_targets_echogram_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/targets-echogram-subscriptions/{subscriptionId} | DeleteTargetsEchogramSubscription
[**api_sounder_data_output_targets_echogram_subscriptions_subscription_id_get**](TargetsEchogramSubscriptionsApi.md#api_sounder_data_output_targets_echogram_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/targets-echogram-subscriptions/{subscriptionId} | GetTargetsEchogramSubscription
[**api_sounder_data_output_targets_echogram_subscriptions_subscription_id_put**](TargetsEchogramSubscriptionsApi.md#api_sounder_data_output_targets_echogram_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/targets-echogram-subscriptions/{subscriptionId} | UpdateTargetsEchogramSubscription

# **api_sounder_data_output_targets_echogram_subscriptions_get**
> list[TargetsEchogramSubscriptionInfo] api_sounder_data_output_targets_echogram_subscriptions_get()

GetTargetsEchogramSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TargetsEchogramSubscriptionsApi()

try:
    # GetTargetsEchogramSubscriptions
    api_response = api_instance.api_sounder_data_output_targets_echogram_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->api_sounder_data_output_targets_echogram_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TargetsEchogramSubscriptionInfo]**](TargetsEchogramSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_targets_echogram_subscriptions_post**
> int api_sounder_data_output_targets_echogram_subscriptions_post(body=body)

CreateTargetsEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TargetsEchogramSubscriptionsApi()
body = ek80dataclient.TargetsEchogramSubscriptionSpecification() # TargetsEchogramSubscriptionSpecification |  (optional)

try:
    # CreateTargetsEchogramSubscription
    api_response = api_instance.api_sounder_data_output_targets_echogram_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->api_sounder_data_output_targets_echogram_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TargetsEchogramSubscriptionSpecification**](TargetsEchogramSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_targets_echogram_subscriptions_subscription_id_delete**
> api_sounder_data_output_targets_echogram_subscriptions_subscription_id_delete(subscription_id)

DeleteTargetsEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TargetsEchogramSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteTargetsEchogramSubscription
    api_instance.api_sounder_data_output_targets_echogram_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->api_sounder_data_output_targets_echogram_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_targets_echogram_subscriptions_subscription_id_get**
> TargetsEchogramSubscriptionSpecification api_sounder_data_output_targets_echogram_subscriptions_subscription_id_get(subscription_id)

GetTargetsEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TargetsEchogramSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetTargetsEchogramSubscription
    api_response = api_instance.api_sounder_data_output_targets_echogram_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->api_sounder_data_output_targets_echogram_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**TargetsEchogramSubscriptionSpecification**](TargetsEchogramSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_targets_echogram_subscriptions_subscription_id_put**
> api_sounder_data_output_targets_echogram_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateTargetsEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TargetsEchogramSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.TargetsEchogramSettings() # TargetsEchogramSettings |  (optional)

try:
    # UpdateTargetsEchogramSubscription
    api_instance.api_sounder_data_output_targets_echogram_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling TargetsEchogramSubscriptionsApi->api_sounder_data_output_targets_echogram_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**TargetsEchogramSettings**](TargetsEchogramSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

