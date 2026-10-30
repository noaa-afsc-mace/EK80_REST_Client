# ek80dataclient.TsDetectionChirpSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_ts_detection_chirp_subscriptions_get**](TsDetectionChirpSubscriptionsApi.md#api_sounder_data_output_ts_detection_chirp_subscriptions_get) | **GET** /api/sounder/data-output/ts-detection-chirp-subscriptions | GetTsDetectionChirpSubscriptions
[**api_sounder_data_output_ts_detection_chirp_subscriptions_post**](TsDetectionChirpSubscriptionsApi.md#api_sounder_data_output_ts_detection_chirp_subscriptions_post) | **POST** /api/sounder/data-output/ts-detection-chirp-subscriptions | CreateTsDetectionChirpSubscription
[**api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_delete**](TsDetectionChirpSubscriptionsApi.md#api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/ts-detection-chirp-subscriptions/{subscriptionId} | DeleteTsDetectionChirpSubscription
[**api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_get**](TsDetectionChirpSubscriptionsApi.md#api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/ts-detection-chirp-subscriptions/{subscriptionId} | GetTsDetectionChirpSubscription
[**api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_put**](TsDetectionChirpSubscriptionsApi.md#api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/ts-detection-chirp-subscriptions/{subscriptionId} | UpdateTsDetectionChirpSubscription

# **api_sounder_data_output_ts_detection_chirp_subscriptions_get**
> list[TsDetectionChirpSubscriptionInfo] api_sounder_data_output_ts_detection_chirp_subscriptions_get()

GetTsDetectionChirpSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionChirpSubscriptionsApi()

try:
    # GetTsDetectionChirpSubscriptions
    api_response = api_instance.api_sounder_data_output_ts_detection_chirp_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->api_sounder_data_output_ts_detection_chirp_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TsDetectionChirpSubscriptionInfo]**](TsDetectionChirpSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_ts_detection_chirp_subscriptions_post**
> int api_sounder_data_output_ts_detection_chirp_subscriptions_post(body=body)

CreateTsDetectionChirpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionChirpSubscriptionsApi()
body = ek80dataclient.TsDetectionChirpSubscriptionSpecification() # TsDetectionChirpSubscriptionSpecification |  (optional)

try:
    # CreateTsDetectionChirpSubscription
    api_response = api_instance.api_sounder_data_output_ts_detection_chirp_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->api_sounder_data_output_ts_detection_chirp_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TsDetectionChirpSubscriptionSpecification**](TsDetectionChirpSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_delete**
> api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_delete(subscription_id)

DeleteTsDetectionChirpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionChirpSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteTsDetectionChirpSubscription
    api_instance.api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_get**
> TsDetectionChirpSubscriptionSpecification api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_get(subscription_id)

GetTsDetectionChirpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionChirpSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetTsDetectionChirpSubscription
    api_response = api_instance.api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**TsDetectionChirpSubscriptionSpecification**](TsDetectionChirpSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_put**
> api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateTsDetectionChirpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.TsDetectionChirpSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.TsDetectionChirpSettings() # TsDetectionChirpSettings |  (optional)

try:
    # UpdateTsDetectionChirpSubscription
    api_instance.api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling TsDetectionChirpSubscriptionsApi->api_sounder_data_output_ts_detection_chirp_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**TsDetectionChirpSettings**](TsDetectionChirpSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

