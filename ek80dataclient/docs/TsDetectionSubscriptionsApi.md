# ek80dataclient.TsDetectionSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_ts_detection_subscriptions_get**](TsDetectionSubscriptionsApi.md#api_sounder_data_output_ts_detection_subscriptions_get) | **GET** /api/sounder/data-output/ts-detection-subscriptions | GetTsDetectionSubscriptions
[**api_sounder_data_output_ts_detection_subscriptions_post**](TsDetectionSubscriptionsApi.md#api_sounder_data_output_ts_detection_subscriptions_post) | **POST** /api/sounder/data-output/ts-detection-subscriptions | CreateTsDetectionSubscription
[**api_sounder_data_output_ts_detection_subscriptions_subscription_id_delete**](TsDetectionSubscriptionsApi.md#api_sounder_data_output_ts_detection_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/ts-detection-subscriptions/{subscriptionId} | DeleteTsDetectionSubscription
[**api_sounder_data_output_ts_detection_subscriptions_subscription_id_get**](TsDetectionSubscriptionsApi.md#api_sounder_data_output_ts_detection_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/ts-detection-subscriptions/{subscriptionId} | GetTsDetectionSubscription
[**api_sounder_data_output_ts_detection_subscriptions_subscription_id_put**](TsDetectionSubscriptionsApi.md#api_sounder_data_output_ts_detection_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/ts-detection-subscriptions/{subscriptionId} | UpdateTsDetectionSubscription

# **api_sounder_data_output_ts_detection_subscriptions_get**
> list[TsDetectionSubscriptionInfo] api_sounder_data_output_ts_detection_subscriptions_get()

GetTsDetectionSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionSubscriptionsApi()

try:
    # GetTsDetectionSubscriptions
    api_response = api_instance.api_sounder_data_output_ts_detection_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->api_sounder_data_output_ts_detection_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TsDetectionSubscriptionInfo]**](TsDetectionSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_ts_detection_subscriptions_post**
> int api_sounder_data_output_ts_detection_subscriptions_post(body=body)

CreateTsDetectionSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionSubscriptionsApi()
body = ek80dataclient.TsDetectionSubscriptionSpecification() # TsDetectionSubscriptionSpecification |  (optional)

try:
    # CreateTsDetectionSubscription
    api_response = api_instance.api_sounder_data_output_ts_detection_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->api_sounder_data_output_ts_detection_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TsDetectionSubscriptionSpecification**](TsDetectionSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_ts_detection_subscriptions_subscription_id_delete**
> api_sounder_data_output_ts_detection_subscriptions_subscription_id_delete(subscription_id)

DeleteTsDetectionSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteTsDetectionSubscription
    api_instance.api_sounder_data_output_ts_detection_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->api_sounder_data_output_ts_detection_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_ts_detection_subscriptions_subscription_id_get**
> TsDetectionSubscriptionSpecification api_sounder_data_output_ts_detection_subscriptions_subscription_id_get(subscription_id)

GetTsDetectionSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetTsDetectionSubscription
    api_response = api_instance.api_sounder_data_output_ts_detection_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->api_sounder_data_output_ts_detection_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**TsDetectionSubscriptionSpecification**](TsDetectionSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_ts_detection_subscriptions_subscription_id_put**
> api_sounder_data_output_ts_detection_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateTsDetectionSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.TsDetectionSettings() # TsDetectionSettings |  (optional)

try:
    # UpdateTsDetectionSubscription
    api_instance.api_sounder_data_output_ts_detection_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling TsDetectionSubscriptionsApi->api_sounder_data_output_ts_detection_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**TsDetectionSettings**](TsDetectionSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

