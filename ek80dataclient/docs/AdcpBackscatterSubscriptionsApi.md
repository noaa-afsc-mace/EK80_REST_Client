# ek80dataclient.AdcpBackscatterSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_adcp_backscatter_subscriptions_get**](AdcpBackscatterSubscriptionsApi.md#api_sounder_data_output_adcp_backscatter_subscriptions_get) | **GET** /api/sounder/data-output/adcp-backscatter-subscriptions | GetAdcpBackscatterSubscriptions
[**api_sounder_data_output_adcp_backscatter_subscriptions_post**](AdcpBackscatterSubscriptionsApi.md#api_sounder_data_output_adcp_backscatter_subscriptions_post) | **POST** /api/sounder/data-output/adcp-backscatter-subscriptions | CreateAdcpBackscatterSubscription
[**api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_delete**](AdcpBackscatterSubscriptionsApi.md#api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/adcp-backscatter-subscriptions/{subscriptionId} | DeleteAdcpBackscatterSubscription
[**api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_get**](AdcpBackscatterSubscriptionsApi.md#api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/adcp-backscatter-subscriptions/{subscriptionId} | GetBackscatterAdcpSubscription
[**api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_put**](AdcpBackscatterSubscriptionsApi.md#api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/adcp-backscatter-subscriptions/{subscriptionId} | UpdateAdcpBackscatterSubscription

# **api_sounder_data_output_adcp_backscatter_subscriptions_get**
> list[AdcpBackscatterSubscriptionInfo] api_sounder_data_output_adcp_backscatter_subscriptions_get()

GetAdcpBackscatterSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBackscatterSubscriptionsApi()

try:
    # GetAdcpBackscatterSubscriptions
    api_response = api_instance.api_sounder_data_output_adcp_backscatter_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->api_sounder_data_output_adcp_backscatter_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpBackscatterSubscriptionInfo]**](AdcpBackscatterSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_backscatter_subscriptions_post**
> int api_sounder_data_output_adcp_backscatter_subscriptions_post(body=body)

CreateAdcpBackscatterSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBackscatterSubscriptionsApi()
body = ek80dataclient.AdcpBackscatterSubscriptionSpecification() # AdcpBackscatterSubscriptionSpecification |  (optional)

try:
    # CreateAdcpBackscatterSubscription
    api_response = api_instance.api_sounder_data_output_adcp_backscatter_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->api_sounder_data_output_adcp_backscatter_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdcpBackscatterSubscriptionSpecification**](AdcpBackscatterSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_delete**
> api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_delete(subscription_id)

DeleteAdcpBackscatterSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBackscatterSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteAdcpBackscatterSubscription
    api_instance.api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_get**
> AdcpBackscatterSubscriptionSpecification api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_get(subscription_id)

GetBackscatterAdcpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBackscatterSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetBackscatterAdcpSubscription
    api_response = api_instance.api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**AdcpBackscatterSubscriptionSpecification**](AdcpBackscatterSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_put**
> api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateAdcpBackscatterSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpBackscatterSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.AdcpBackscatterSettings() # AdcpBackscatterSettings |  (optional)

try:
    # UpdateAdcpBackscatterSubscription
    api_instance.api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling AdcpBackscatterSubscriptionsApi->api_sounder_data_output_adcp_backscatter_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**AdcpBackscatterSettings**](AdcpBackscatterSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

