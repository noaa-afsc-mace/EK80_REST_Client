# ek80dataclient.BottomDetectionSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_bottom_detection_subscriptions_get**](BottomDetectionSubscriptionsApi.md#api_sounder_data_output_bottom_detection_subscriptions_get) | **GET** /api/sounder/data-output/bottom-detection-subscriptions | GetBottomDetectionSubscriptions
[**api_sounder_data_output_bottom_detection_subscriptions_post**](BottomDetectionSubscriptionsApi.md#api_sounder_data_output_bottom_detection_subscriptions_post) | **POST** /api/sounder/data-output/bottom-detection-subscriptions | CreateBottomDetectionSubscription
[**api_sounder_data_output_bottom_detection_subscriptions_subscription_id_delete**](BottomDetectionSubscriptionsApi.md#api_sounder_data_output_bottom_detection_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/bottom-detection-subscriptions/{subscriptionId} | DeleteBottomDetectionSubscription
[**api_sounder_data_output_bottom_detection_subscriptions_subscription_id_get**](BottomDetectionSubscriptionsApi.md#api_sounder_data_output_bottom_detection_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/bottom-detection-subscriptions/{subscriptionId} | GetBottomDetectionSubscription
[**api_sounder_data_output_bottom_detection_subscriptions_subscription_id_put**](BottomDetectionSubscriptionsApi.md#api_sounder_data_output_bottom_detection_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/bottom-detection-subscriptions/{subscriptionId} | UpdateBottomDetectionSubscription

# **api_sounder_data_output_bottom_detection_subscriptions_get**
> list[BottomDetectionSubscriptionInfo] api_sounder_data_output_bottom_detection_subscriptions_get()

GetBottomDetectionSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.BottomDetectionSubscriptionsApi()

try:
    # GetBottomDetectionSubscriptions
    api_response = api_instance.api_sounder_data_output_bottom_detection_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->api_sounder_data_output_bottom_detection_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BottomDetectionSubscriptionInfo]**](BottomDetectionSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_bottom_detection_subscriptions_post**
> int api_sounder_data_output_bottom_detection_subscriptions_post(body=body)

CreateBottomDetectionSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.BottomDetectionSubscriptionsApi()
body = ek80dataclient.BottomDetectionSubscriptionSpecification() # BottomDetectionSubscriptionSpecification |  (optional)

try:
    # CreateBottomDetectionSubscription
    api_response = api_instance.api_sounder_data_output_bottom_detection_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->api_sounder_data_output_bottom_detection_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BottomDetectionSubscriptionSpecification**](BottomDetectionSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_bottom_detection_subscriptions_subscription_id_delete**
> api_sounder_data_output_bottom_detection_subscriptions_subscription_id_delete(subscription_id)

DeleteBottomDetectionSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.BottomDetectionSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteBottomDetectionSubscription
    api_instance.api_sounder_data_output_bottom_detection_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->api_sounder_data_output_bottom_detection_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_bottom_detection_subscriptions_subscription_id_get**
> BottomDetectionSubscriptionSpecification api_sounder_data_output_bottom_detection_subscriptions_subscription_id_get(subscription_id)

GetBottomDetectionSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.BottomDetectionSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetBottomDetectionSubscription
    api_response = api_instance.api_sounder_data_output_bottom_detection_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->api_sounder_data_output_bottom_detection_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**BottomDetectionSubscriptionSpecification**](BottomDetectionSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_bottom_detection_subscriptions_subscription_id_put**
> api_sounder_data_output_bottom_detection_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateBottomDetectionSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.BottomDetectionSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.BottomDetectionSettings() # BottomDetectionSettings |  (optional)

try:
    # UpdateBottomDetectionSubscription
    api_instance.api_sounder_data_output_bottom_detection_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling BottomDetectionSubscriptionsApi->api_sounder_data_output_bottom_detection_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**BottomDetectionSettings**](BottomDetectionSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

