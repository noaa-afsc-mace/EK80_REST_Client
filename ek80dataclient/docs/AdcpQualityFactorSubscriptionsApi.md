# ek80dataclient.AdcpQualityFactorSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_adcp_quality_factor_subscriptions_get**](AdcpQualityFactorSubscriptionsApi.md#api_sounder_data_output_adcp_quality_factor_subscriptions_get) | **GET** /api/sounder/data-output/adcp-quality-factor-subscriptions | GetAdcpQualityFactorSubscriptions
[**api_sounder_data_output_adcp_quality_factor_subscriptions_post**](AdcpQualityFactorSubscriptionsApi.md#api_sounder_data_output_adcp_quality_factor_subscriptions_post) | **POST** /api/sounder/data-output/adcp-quality-factor-subscriptions | CreateAdcpQualityFactorSubscription
[**api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_delete**](AdcpQualityFactorSubscriptionsApi.md#api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/adcp-quality-factor-subscriptions/{subscriptionId} | DeleteAdcpQualityFactorSubscription
[**api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_get**](AdcpQualityFactorSubscriptionsApi.md#api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/adcp-quality-factor-subscriptions/{subscriptionId} | GetQualityFactorAdcpSubscription
[**api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_put**](AdcpQualityFactorSubscriptionsApi.md#api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/adcp-quality-factor-subscriptions/{subscriptionId} | UpdateAdcpQualityFactorSubscription

# **api_sounder_data_output_adcp_quality_factor_subscriptions_get**
> list[AdcpQualityFactorSubscriptionInfo] api_sounder_data_output_adcp_quality_factor_subscriptions_get()

GetAdcpQualityFactorSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpQualityFactorSubscriptionsApi()

try:
    # GetAdcpQualityFactorSubscriptions
    api_response = api_instance.api_sounder_data_output_adcp_quality_factor_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->api_sounder_data_output_adcp_quality_factor_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AdcpQualityFactorSubscriptionInfo]**](AdcpQualityFactorSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_quality_factor_subscriptions_post**
> int api_sounder_data_output_adcp_quality_factor_subscriptions_post(body=body)

CreateAdcpQualityFactorSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpQualityFactorSubscriptionsApi()
body = ek80dataclient.AdcpQualityFactorSubscriptionSpecification() # AdcpQualityFactorSubscriptionSpecification |  (optional)

try:
    # CreateAdcpQualityFactorSubscription
    api_response = api_instance.api_sounder_data_output_adcp_quality_factor_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->api_sounder_data_output_adcp_quality_factor_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdcpQualityFactorSubscriptionSpecification**](AdcpQualityFactorSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_delete**
> api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_delete(subscription_id)

DeleteAdcpQualityFactorSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpQualityFactorSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteAdcpQualityFactorSubscription
    api_instance.api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_get**
> AdcpQualityFactorSubscriptionSpecification api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_get(subscription_id)

GetQualityFactorAdcpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpQualityFactorSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetQualityFactorAdcpSubscription
    api_response = api_instance.api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**AdcpQualityFactorSubscriptionSpecification**](AdcpQualityFactorSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_put**
> api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateAdcpQualityFactorSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.AdcpQualityFactorSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.AdcpQualitySettings() # AdcpQualitySettings |  (optional)

try:
    # UpdateAdcpQualityFactorSubscription
    api_instance.api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling AdcpQualityFactorSubscriptionsApi->api_sounder_data_output_adcp_quality_factor_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**AdcpQualitySettings**](AdcpQualitySettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

