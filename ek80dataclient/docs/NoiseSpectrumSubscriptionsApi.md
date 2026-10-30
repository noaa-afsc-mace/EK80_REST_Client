# ek80dataclient.NoiseSpectrumSubscriptionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_noise_spectrum_subscriptions_get**](NoiseSpectrumSubscriptionsApi.md#api_sounder_data_output_noise_spectrum_subscriptions_get) | **GET** /api/sounder/data-output/noise-spectrum-subscriptions | GetNoiseSpectrumSubscriptions
[**api_sounder_data_output_noise_spectrum_subscriptions_post**](NoiseSpectrumSubscriptionsApi.md#api_sounder_data_output_noise_spectrum_subscriptions_post) | **POST** /api/sounder/data-output/noise-spectrum-subscriptions | CreateNoiseSpectrumSubscription
[**api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_delete**](NoiseSpectrumSubscriptionsApi.md#api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_delete) | **DELETE** /api/sounder/data-output/noise-spectrum-subscriptions/{subscriptionId} | DeleteNoiseSpectrumSubscription
[**api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_get**](NoiseSpectrumSubscriptionsApi.md#api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_get) | **GET** /api/sounder/data-output/noise-spectrum-subscriptions/{subscriptionId} | GetNoiseSpectrumSubscription
[**api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_put**](NoiseSpectrumSubscriptionsApi.md#api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_put) | **PUT** /api/sounder/data-output/noise-spectrum-subscriptions/{subscriptionId} | UpdateNoiseSpectrumSubscription

# **api_sounder_data_output_noise_spectrum_subscriptions_get**
> list[NoiseSpectrumSubscriptionInfo] api_sounder_data_output_noise_spectrum_subscriptions_get()

GetNoiseSpectrumSubscriptions

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.NoiseSpectrumSubscriptionsApi()

try:
    # GetNoiseSpectrumSubscriptions
    api_response = api_instance.api_sounder_data_output_noise_spectrum_subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->api_sounder_data_output_noise_spectrum_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NoiseSpectrumSubscriptionInfo]**](NoiseSpectrumSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_noise_spectrum_subscriptions_post**
> int api_sounder_data_output_noise_spectrum_subscriptions_post(body=body)

CreateNoiseSpectrumSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.NoiseSpectrumSubscriptionsApi()
body = ek80dataclient.NoiseSpectrumSubscriptionSpecification() # NoiseSpectrumSubscriptionSpecification |  (optional)

try:
    # CreateNoiseSpectrumSubscription
    api_response = api_instance.api_sounder_data_output_noise_spectrum_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->api_sounder_data_output_noise_spectrum_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NoiseSpectrumSubscriptionSpecification**](NoiseSpectrumSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_delete**
> api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_delete(subscription_id)

DeleteNoiseSpectrumSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.NoiseSpectrumSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # DeleteNoiseSpectrumSubscription
    api_instance.api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_delete(subscription_id)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_delete: %s\n" % e)
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

# **api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_get**
> NoiseSpectrumSubscriptionSpecification api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_get(subscription_id)

GetNoiseSpectrumSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.NoiseSpectrumSubscriptionsApi()
subscription_id = 789 # int | 

try:
    # GetNoiseSpectrumSubscription
    api_response = api_instance.api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**NoiseSpectrumSubscriptionSpecification**](NoiseSpectrumSubscriptionSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_put**
> api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_put(subscription_id, body=body)

UpdateNoiseSpectrumSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.NoiseSpectrumSubscriptionsApi()
subscription_id = 789 # int | 
body = ek80dataclient.NoiseSpectrumSettings() # NoiseSpectrumSettings |  (optional)

try:
    # UpdateNoiseSpectrumSubscription
    api_instance.api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_put(subscription_id, body=body)
except ApiException as e:
    print("Exception when calling NoiseSpectrumSubscriptionsApi->api_sounder_data_output_noise_spectrum_subscriptions_subscription_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **body** | [**NoiseSpectrumSettings**](NoiseSpectrumSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

