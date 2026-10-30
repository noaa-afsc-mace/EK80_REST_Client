# ek80dataclient.SampleDataSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_sample_data_subscriptions_get**](SampleDataSubscriptionsApi.md#api_sounder_data_output_sample_data_subscriptions_get) | **GET** /api/sounder/data-output/sample-data-subscriptions | GetSampleDataSubscriptions
[**api_sounder_data_output_sample_data_subscriptions_post**](SampleDataSubscriptionsApi.md#api_sounder_data_output_sample_data_subscriptions_post) | **POST** /api/sounder/data-output/sample-data-subscriptions | CreateSampleDataSubscription
[**api_sounder_data_output_sample_data_subscriptions_subscription_id_delete**](SampleDataSubscriptionsApi.md#api_sounder_data_output_sample_data_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/sample-data-subscriptions/{subscriptionId} | DeleteSampleDataSubscription
[**api_sounder_data_output_sample_data_subscriptions_subscription_id_get**](SampleDataSubscriptionsApi.md#api_sounder_data_output_sample_data_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/sample-data-subscriptions/{subscriptionId} | GetSampleDataSubscription
[**api_sounder_data_output_sample_data_subscriptions_subscription_id_put**](SampleDataSubscriptionsApi.md#api_sounder_data_output_sample_data_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/sample-data-subscriptions/{subscriptionId} | UpdateSampleDataSubscription

# **api_sounder_data_output_sample_data_subscriptions_get**
> list[SampleDataSubscriptionInfo] api_sounder_data_output_sample_data_subscriptions_get()

GetSampleDataSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SampleDataSubscriptionsApi()

try:
    # GetSampleDataSubscriptions
    api_response = api_instance.api_sounder_data_output_sample_data_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->api_sounder_data_output_sample_data_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SampleDataSubscriptionInfo]**](SampleDataSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_sample_data_subscriptions_post**
> int api_sounder_data_output_sample_data_subscriptions_post(body=body)

CreateSampleDataSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SampleDataSubscriptionsApi()
body = ek80dataclient.SampleDataSubscriptionSpecification() # SampleDataSubscriptionSpecification |  (optional)

try:
    # CreateSampleDataSubscription
    api_response = api_instance.api_sounder_data_output_sample_data_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->api_sounder_data_output_sample_data_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SampleDataSubscriptionSpecification**](SampleDataSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_sample_data_subscriptions_subscription_id_delete**
> api_sounder_data_output_sample_data_subscriptions_subscription_id_delete(subscription_id)

DeleteSampleDataSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SampleDataSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteSampleDataSubscription
    api_instance.api_sounder_data_output_sample_data_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->api_sounder_data_output_sample_data_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_sample_data_subscriptions_subscription_id_get**
> SampleDataSubscriptionSpecification api_sounder_data_output_sample_data_subscriptions_subscription_id_get(subscription_id)

GetSampleDataSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SampleDataSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetSampleDataSubscription
    api_response = api_instance.api_sounder_data_output_sample_data_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->api_sounder_data_output_sample_data_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**SampleDataSubscriptionSpecification**](SampleDataSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_sample_data_subscriptions_subscription_id_put**
> api_sounder_data_output_sample_data_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateSampleDataSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.SampleDataSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.SampleDataSettings() # SampleDataSettings |  (optional)

try:
    # UpdateSampleDataSubscription
    api_instance.api_sounder_data_output_sample_data_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling SampleDataSubscriptionsApi->api_sounder_data_output_sample_data_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**SampleDataSettings**](SampleDataSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

