# ek80dataclient.AdcpVelocitySubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_adcp_velocity_subscriptions_get**](AdcpVelocitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_subscriptions_get) | **GET** /api/sounder/data-output/adcp-velocity-subscriptions | GetAdcpVelocitySubscriptions
[**api_sounder_data_output_adcp_velocity_subscriptions_post**](AdcpVelocitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_subscriptions_post) | **POST** /api/sounder/data-output/adcp-velocity-subscriptions | CreateAdcpVelocitySubscription
[**api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_delete**](AdcpVelocitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/adcp-velocity-subscriptions/{subscriptionId} | DeleteAdcpVelocitySubscription
[**api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_get**](AdcpVelocitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/adcp-velocity-subscriptions/{subscriptionId} | GetVelocityAdcpSubscription
[**api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_put**](AdcpVelocitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/adcp-velocity-subscriptions/{subscriptionId} | UpdateAdcpVelocitySubscription

# **api_sounder_data_output_adcp_velocity_subscriptions_get**
> list[AdcpVelocitySubscriptionInfo] api_sounder_data_output_adcp_velocity_subscriptions_get()

GetAdcpVelocitySubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocitySubscriptionsApi()

try:
    # GetAdcpVelocitySubscriptions
    api_response = api_instance.api_sounder_data_output_adcp_velocity_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->api_sounder_data_output_adcp_velocity_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpVelocitySubscriptionInfo]**](AdcpVelocitySubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_velocity_subscriptions_post**
> int api_sounder_data_output_adcp_velocity_subscriptions_post(body=body)

CreateAdcpVelocitySubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocitySubscriptionsApi()
body = ek80dataclient.AdcpVelocitySubscriptionSpecification() # AdcpVelocitySubscriptionSpecification |  (optional)

try:
    # CreateAdcpVelocitySubscription
    api_response = api_instance.api_sounder_data_output_adcp_velocity_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->api_sounder_data_output_adcp_velocity_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdcpVelocitySubscriptionSpecification**](AdcpVelocitySubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_delete**
> api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_delete(subscription_id)

DeleteAdcpVelocitySubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocitySubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteAdcpVelocitySubscription
    api_instance.api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_get**
> AdcpVelocitySubscriptionSpecification api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_get(subscription_id)

GetVelocityAdcpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocitySubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetVelocityAdcpSubscription
    api_response = api_instance.api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**AdcpVelocitySubscriptionSpecification**](AdcpVelocitySubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_put**
> api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateAdcpVelocitySubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocitySubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.AdcpVelocitySettings() # AdcpVelocitySettings |  (optional)

try:
    # UpdateAdcpVelocitySubscription
    api_instance.api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling AdcpVelocitySubscriptionsApi->api_sounder_data_output_adcp_velocity_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**AdcpVelocitySettings**](AdcpVelocitySettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

