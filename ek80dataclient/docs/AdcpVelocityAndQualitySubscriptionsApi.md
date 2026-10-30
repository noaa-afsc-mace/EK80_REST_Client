# ek80dataclient.AdcpVelocityAndQualitySubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_adcp_velocity_and_quality_subscriptions_get**](AdcpVelocityAndQualitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_and_quality_subscriptions_get) | **GET** /api/sounder/data-output/adcp-velocity-and-quality-subscriptions | GetAdcpVelocityAndQualitySubscriptions
[**api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post**](AdcpVelocityAndQualitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post) | **POST** /api/sounder/data-output/adcp-velocity-and-quality-subscriptions | CreateAdcpVelocityAndQualitySubscription
[**api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_delete**](AdcpVelocityAndQualitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/adcp-velocity-and-quality-subscriptions/{subscriptionId} | DeleteAdcpVelocityAndQualityubscription
[**api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_get**](AdcpVelocityAndQualitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/adcp-velocity-and-quality-subscriptions/{subscriptionId} | GetAdcpVelocityAndQualityubscription
[**api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_put**](AdcpVelocityAndQualitySubscriptionsApi.md#api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/adcp-velocity-and-quality-subscriptions/{subscriptionId} | UpdateAdcpVelocityAndQualitySubscription

# **api_sounder_data_output_adcp_velocity_and_quality_subscriptions_get**
> list[AdcpVelocityAndQualitySubscriptionInfo] api_sounder_data_output_adcp_velocity_and_quality_subscriptions_get()

GetAdcpVelocityAndQualitySubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocityAndQualitySubscriptionsApi()

try:
    # GetAdcpVelocityAndQualitySubscriptions
    api_response = api_instance.api_sounder_data_output_adcp_velocity_and_quality_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpVelocityAndQualitySubscriptionsApi->api_sounder_data_output_adcp_velocity_and_quality_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpVelocityAndQualitySubscriptionInfo]**](AdcpVelocityAndQualitySubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post**
> int api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post(body=body)

CreateAdcpVelocityAndQualitySubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocityAndQualitySubscriptionsApi()
body = ek80dataclient.AdcpVelocityAndQualitySubscriptionSpecification() # AdcpVelocityAndQualitySubscriptionSpecification |  (optional)

try:
    # CreateAdcpVelocityAndQualitySubscription
    api_response = api_instance.api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpVelocityAndQualitySubscriptionsApi->api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdcpVelocityAndQualitySubscriptionSpecification**](AdcpVelocityAndQualitySubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_delete**
> api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_delete(subscription_id)

DeleteAdcpVelocityAndQualityubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocityAndQualitySubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteAdcpVelocityAndQualityubscription
    api_instance.api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpVelocityAndQualitySubscriptionsApi->api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_get**
> AdcpVelocityAndQualitySubscriptionSpecification api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_get(subscription_id)

GetAdcpVelocityAndQualityubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocityAndQualitySubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetAdcpVelocityAndQualityubscription
    api_response = api_instance.api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpVelocityAndQualitySubscriptionsApi->api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**AdcpVelocityAndQualitySubscriptionSpecification**](AdcpVelocityAndQualitySubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_put**
> api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateAdcpVelocityAndQualitySubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpVelocityAndQualitySubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.AdcpVelocityAndQualitySettings() # AdcpVelocityAndQualitySettings |  (optional)

try:
    # UpdateAdcpVelocityAndQualitySubscription
    api_instance.api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling AdcpVelocityAndQualitySubscriptionsApi->api_sounder_data_output_adcp_velocity_and_quality_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**AdcpVelocityAndQualitySettings**](AdcpVelocityAndQualitySettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

