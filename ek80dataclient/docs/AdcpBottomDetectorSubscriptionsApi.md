# ek80dataclient.AdcpBottomDetectorSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_adcp_bottom_detector_subscriptions_get**](AdcpBottomDetectorSubscriptionsApi.md#api_sounder_data_output_adcp_bottom_detector_subscriptions_get) | **GET** /api/sounder/data-output/adcp-bottom-detector-subscriptions | GetAdcpBottomDetectorSubscriptions
[**api_sounder_data_output_adcp_bottom_detector_subscriptions_post**](AdcpBottomDetectorSubscriptionsApi.md#api_sounder_data_output_adcp_bottom_detector_subscriptions_post) | **POST** /api/sounder/data-output/adcp-bottom-detector-subscriptions | CreateAdcpBottomDetectorSubscription
[**api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_delete**](AdcpBottomDetectorSubscriptionsApi.md#api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/adcp-bottom-detector-subscriptions/{subscriptionId} | DeleteAdcpBottomDetectorSubscription
[**api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_get**](AdcpBottomDetectorSubscriptionsApi.md#api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/adcp-bottom-detector-subscriptions/{subscriptionId} | GetBottomDetectorAdcpSubscription
[**api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_put**](AdcpBottomDetectorSubscriptionsApi.md#api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/adcp-bottom-detector-subscriptions/{subscriptionId} | UpdateAdcpBottomDetectorSubscription

# **api_sounder_data_output_adcp_bottom_detector_subscriptions_get**
> list[AdcpBottomDetectorSubscriptionInfo] api_sounder_data_output_adcp_bottom_detector_subscriptions_get()

GetAdcpBottomDetectorSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBottomDetectorSubscriptionsApi()

try:
    # GetAdcpBottomDetectorSubscriptions
    api_response = api_instance.api_sounder_data_output_adcp_bottom_detector_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->api_sounder_data_output_adcp_bottom_detector_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpBottomDetectorSubscriptionInfo]**](AdcpBottomDetectorSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_bottom_detector_subscriptions_post**
> int api_sounder_data_output_adcp_bottom_detector_subscriptions_post(body=body)

CreateAdcpBottomDetectorSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBottomDetectorSubscriptionsApi()
body = ek80dataclient.AdcpBottomDetectorSubscriptionSpecification() # AdcpBottomDetectorSubscriptionSpecification |  (optional)

try:
    # CreateAdcpBottomDetectorSubscription
    api_response = api_instance.api_sounder_data_output_adcp_bottom_detector_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->api_sounder_data_output_adcp_bottom_detector_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdcpBottomDetectorSubscriptionSpecification**](AdcpBottomDetectorSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_delete**
> api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_delete(subscription_id)

DeleteAdcpBottomDetectorSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBottomDetectorSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteAdcpBottomDetectorSubscription
    api_instance.api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_get**
> AdcpBottomDetectorSubscriptionSpecification api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_get(subscription_id)

GetBottomDetectorAdcpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBottomDetectorSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetBottomDetectorAdcpSubscription
    api_response = api_instance.api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**AdcpBottomDetectorSubscriptionSpecification**](AdcpBottomDetectorSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_put**
> api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateAdcpBottomDetectorSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBottomDetectorSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.AdcpBottomDetectorSettings() # AdcpBottomDetectorSettings |  (optional)

try:
    # UpdateAdcpBottomDetectorSubscription
    api_instance.api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling AdcpBottomDetectorSubscriptionsApi->api_sounder_data_output_adcp_bottom_detector_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**AdcpBottomDetectorSettings**](AdcpBottomDetectorSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

