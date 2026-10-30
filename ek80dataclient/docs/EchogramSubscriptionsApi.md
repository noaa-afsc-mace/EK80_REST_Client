# ek80dataclient.EchogramSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_echogram_subscriptions_get**](EchogramSubscriptionsApi.md#api_sounder_data_output_echogram_subscriptions_get) | **GET** /api/sounder/data-output/echogram-subscriptions | GetEchogramSubscriptions
[**api_sounder_data_output_echogram_subscriptions_post**](EchogramSubscriptionsApi.md#api_sounder_data_output_echogram_subscriptions_post) | **POST** /api/sounder/data-output/echogram-subscriptions | CreateEchogramSubscription
[**api_sounder_data_output_echogram_subscriptions_subscription_id_delete**](EchogramSubscriptionsApi.md#api_sounder_data_output_echogram_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/echogram-subscriptions/{subscriptionId} | DeleteEchogramSubscription
[**api_sounder_data_output_echogram_subscriptions_subscription_id_get**](EchogramSubscriptionsApi.md#api_sounder_data_output_echogram_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/echogram-subscriptions/{subscriptionId} | GetEchogramSubscription
[**api_sounder_data_output_echogram_subscriptions_subscription_id_put**](EchogramSubscriptionsApi.md#api_sounder_data_output_echogram_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/echogram-subscriptions/{subscriptionId} | UpdateEchogramSubscription

# **api_sounder_data_output_echogram_subscriptions_get**
> list[EchogramSubscriptionInfo] api_sounder_data_output_echogram_subscriptions_get()

GetEchogramSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.EchogramSubscriptionsApi()

try:
    # GetEchogramSubscriptions
    api_response = api_instance.api_sounder_data_output_echogram_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->api_sounder_data_output_echogram_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EchogramSubscriptionInfo]**](EchogramSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_echogram_subscriptions_post**
> int api_sounder_data_output_echogram_subscriptions_post(body=body)

CreateEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.EchogramSubscriptionsApi()
body = ek80dataclient.EchogramSubscriptionSpecification() # EchogramSubscriptionSpecification |  (optional)

try:
    # CreateEchogramSubscription
    api_response = api_instance.api_sounder_data_output_echogram_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->api_sounder_data_output_echogram_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EchogramSubscriptionSpecification**](EchogramSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_echogram_subscriptions_subscription_id_delete**
> api_sounder_data_output_echogram_subscriptions_subscription_id_delete(subscription_id)

DeleteEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.EchogramSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteEchogramSubscription
    api_instance.api_sounder_data_output_echogram_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->api_sounder_data_output_echogram_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_echogram_subscriptions_subscription_id_get**
> EchogramSubscriptionSpecification api_sounder_data_output_echogram_subscriptions_subscription_id_get(subscription_id)

GetEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.EchogramSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetEchogramSubscription
    api_response = api_instance.api_sounder_data_output_echogram_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->api_sounder_data_output_echogram_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**EchogramSubscriptionSpecification**](EchogramSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_echogram_subscriptions_subscription_id_put**
> api_sounder_data_output_echogram_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.EchogramSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.EchogramSettings() # EchogramSettings |  (optional)

try:
    # UpdateEchogramSubscription
    api_instance.api_sounder_data_output_echogram_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling EchogramSubscriptionsApi->api_sounder_data_output_echogram_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**EchogramSettings**](EchogramSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

