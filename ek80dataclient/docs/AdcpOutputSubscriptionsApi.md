# ek80dataclient.AdcpOutputSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_adcp_output_subscriptions_get**](AdcpOutputSubscriptionsApi.md#api_sounder_data_output_adcp_output_subscriptions_get) | **GET** /api/sounder/data-output/adcp-output-subscriptions | GetAdcpOutputSubscriptions
[**api_sounder_data_output_adcp_output_subscriptions_post**](AdcpOutputSubscriptionsApi.md#api_sounder_data_output_adcp_output_subscriptions_post) | **POST** /api/sounder/data-output/adcp-output-subscriptions | CreateAdcpOutputSubscription
[**api_sounder_data_output_adcp_output_subscriptions_subscription_id_delete**](AdcpOutputSubscriptionsApi.md#api_sounder_data_output_adcp_output_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/adcp-output-subscriptions/{subscriptionId} | DeleteAdcpOutputSubscription
[**api_sounder_data_output_adcp_output_subscriptions_subscription_id_get**](AdcpOutputSubscriptionsApi.md#api_sounder_data_output_adcp_output_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/adcp-output-subscriptions/{subscriptionId} | GetOutputAdcpSubscription
[**api_sounder_data_output_adcp_output_subscriptions_subscription_id_put**](AdcpOutputSubscriptionsApi.md#api_sounder_data_output_adcp_output_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/adcp-output-subscriptions/{subscriptionId} | UpdateAdcpOutputSubscription

# **api_sounder_data_output_adcp_output_subscriptions_get**
> list[AdcpOutputSubscriptionInfo] api_sounder_data_output_adcp_output_subscriptions_get()

GetAdcpOutputSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpOutputSubscriptionsApi()

try:
    # GetAdcpOutputSubscriptions
    api_response = api_instance.api_sounder_data_output_adcp_output_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpOutputSubscriptionsApi->api_sounder_data_output_adcp_output_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpOutputSubscriptionInfo]**](AdcpOutputSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_output_subscriptions_post**
> int api_sounder_data_output_adcp_output_subscriptions_post(body=body)

CreateAdcpOutputSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpOutputSubscriptionsApi()
body = ek80dataclient.AdcpOutputSubscriptionSpecification() # AdcpOutputSubscriptionSpecification |  (optional)

try:
    # CreateAdcpOutputSubscription
    api_response = api_instance.api_sounder_data_output_adcp_output_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpOutputSubscriptionsApi->api_sounder_data_output_adcp_output_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdcpOutputSubscriptionSpecification**](AdcpOutputSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_output_subscriptions_subscription_id_delete**
> api_sounder_data_output_adcp_output_subscriptions_subscription_id_delete(subscription_id)

DeleteAdcpOutputSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpOutputSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteAdcpOutputSubscription
    api_instance.api_sounder_data_output_adcp_output_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpOutputSubscriptionsApi->api_sounder_data_output_adcp_output_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_adcp_output_subscriptions_subscription_id_get**
> AdcpOutputSubscriptionSpecification api_sounder_data_output_adcp_output_subscriptions_subscription_id_get(subscription_id)

GetOutputAdcpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpOutputSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetOutputAdcpSubscription
    api_response = api_instance.api_sounder_data_output_adcp_output_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpOutputSubscriptionsApi->api_sounder_data_output_adcp_output_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**AdcpOutputSubscriptionSpecification**](AdcpOutputSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_output_subscriptions_subscription_id_put**
> api_sounder_data_output_adcp_output_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateAdcpOutputSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpOutputSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.AdcpOutputSettings() # AdcpOutputSettings |  (optional)

try:
    # UpdateAdcpOutputSubscription
    api_instance.api_sounder_data_output_adcp_output_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling AdcpOutputSubscriptionsApi->api_sounder_data_output_adcp_output_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**AdcpOutputSettings**](AdcpOutputSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

