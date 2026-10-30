# ek80dataclient.CreateADataSubscriptionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sounder_data_output_adcp_backscatter_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_adcp_backscatter_subscriptions_post) | **POST** /api/sounder/data-output/adcp-backscatter-subscriptions | CreateAdcpBackscatterSubscription
[**api_sounder_data_output_adcp_beam_data_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_adcp_beam_data_subscriptions_post) | **POST** /api/sounder/data-output/adcp-beam-data-subscriptions | CreateAdcpBeamDataSubscription
[**api_sounder_data_output_adcp_bottom_detector_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_adcp_bottom_detector_subscriptions_post) | **POST** /api/sounder/data-output/adcp-bottom-detector-subscriptions | CreateAdcpBottomDetectorSubscription
[**api_sounder_data_output_adcp_output_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_adcp_output_subscriptions_post) | **POST** /api/sounder/data-output/adcp-output-subscriptions | CreateAdcpOutputSubscription
[**api_sounder_data_output_adcp_quality_factor_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_adcp_quality_factor_subscriptions_post) | **POST** /api/sounder/data-output/adcp-quality-factor-subscriptions | CreateAdcpQualityFactorSubscription
[**api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post) | **POST** /api/sounder/data-output/adcp-velocity-and-quality-subscriptions | CreateAdcpVelocityAndQualitySubscription
[**api_sounder_data_output_adcp_velocity_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_adcp_velocity_subscriptions_post) | **POST** /api/sounder/data-output/adcp-velocity-subscriptions | CreateAdcpVelocitySubscription
[**api_sounder_data_output_bottom_detection_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_bottom_detection_subscriptions_post) | **POST** /api/sounder/data-output/bottom-detection-subscriptions | CreateBottomDetectionSubscription
[**api_sounder_data_output_echogram_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_echogram_subscriptions_post) | **POST** /api/sounder/data-output/echogram-subscriptions | CreateEchogramSubscription
[**api_sounder_data_output_integration_chirp_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_integration_chirp_subscriptions_post) | **POST** /api/sounder/data-output/integration-chirp-subscriptions | CreateIntegrationChirpSubscription
[**api_sounder_data_output_integration_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_integration_subscriptions_post) | **POST** /api/sounder/data-output/integration-subscriptions | CreateIntegrationSubscription
[**api_sounder_data_output_noise_spectrum_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_noise_spectrum_subscriptions_post) | **POST** /api/sounder/data-output/noise-spectrum-subscriptions | CreateNoiseSpectrumSubscription
[**api_sounder_data_output_sample_data_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_sample_data_subscriptions_post) | **POST** /api/sounder/data-output/sample-data-subscriptions | CreateSampleDataSubscription
[**api_sounder_data_output_system_state_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_system_state_subscriptions_post) | **POST** /api/sounder/data-output/system-state-subscriptions | CreateSystemStateSubscription
[**api_sounder_data_output_targets_echogram_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_targets_echogram_subscriptions_post) | **POST** /api/sounder/data-output/targets-echogram-subscriptions | CreateTargetsEchogramSubscription
[**api_sounder_data_output_targets_integration_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_targets_integration_subscriptions_post) | **POST** /api/sounder/data-output/targets-integration-subscriptions | CreateTargetsIntegrationSubscription
[**api_sounder_data_output_ts_detection_chirp_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_ts_detection_chirp_subscriptions_post) | **POST** /api/sounder/data-output/ts-detection-chirp-subscriptions | CreateTsDetectionChirpSubscription
[**api_sounder_data_output_ts_detection_subscriptions_post**](CreateADataSubscriptionApi.md#api_sounder_data_output_ts_detection_subscriptions_post) | **POST** /api/sounder/data-output/ts-detection-subscriptions | CreateTsDetectionSubscription

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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.AdcpBackscatterSubscriptionSpecification() # AdcpBackscatterSubscriptionSpecification |  (optional)

try:
    # CreateAdcpBackscatterSubscription
    api_response = api_instance.api_sounder_data_output_adcp_backscatter_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_adcp_backscatter_subscriptions_post: %s\n" % e)
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

# **api_sounder_data_output_adcp_beam_data_subscriptions_post**
> int api_sounder_data_output_adcp_beam_data_subscriptions_post(body=body)

CreateAdcpBeamDataSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.AdcpBeamDataSubscriptionSpecification() # AdcpBeamDataSubscriptionSpecification |  (optional)

try:
    # CreateAdcpBeamDataSubscription
    api_response = api_instance.api_sounder_data_output_adcp_beam_data_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_adcp_beam_data_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdcpBeamDataSubscriptionSpecification**](AdcpBeamDataSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.AdcpBottomDetectorSubscriptionSpecification() # AdcpBottomDetectorSubscriptionSpecification |  (optional)

try:
    # CreateAdcpBottomDetectorSubscription
    api_response = api_instance.api_sounder_data_output_adcp_bottom_detector_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_adcp_bottom_detector_subscriptions_post: %s\n" % e)
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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.AdcpOutputSubscriptionSpecification() # AdcpOutputSubscriptionSpecification |  (optional)

try:
    # CreateAdcpOutputSubscription
    api_response = api_instance.api_sounder_data_output_adcp_output_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_adcp_output_subscriptions_post: %s\n" % e)
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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.AdcpQualityFactorSubscriptionSpecification() # AdcpQualityFactorSubscriptionSpecification |  (optional)

try:
    # CreateAdcpQualityFactorSubscription
    api_response = api_instance.api_sounder_data_output_adcp_quality_factor_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_adcp_quality_factor_subscriptions_post: %s\n" % e)
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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.AdcpVelocityAndQualitySubscriptionSpecification() # AdcpVelocityAndQualitySubscriptionSpecification |  (optional)

try:
    # CreateAdcpVelocityAndQualitySubscription
    api_response = api_instance.api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_adcp_velocity_and_quality_subscriptions_post: %s\n" % e)
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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.AdcpVelocitySubscriptionSpecification() # AdcpVelocitySubscriptionSpecification |  (optional)

try:
    # CreateAdcpVelocitySubscription
    api_response = api_instance.api_sounder_data_output_adcp_velocity_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_adcp_velocity_subscriptions_post: %s\n" % e)
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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.BottomDetectionSubscriptionSpecification() # BottomDetectionSubscriptionSpecification |  (optional)

try:
    # CreateBottomDetectionSubscription
    api_response = api_instance.api_sounder_data_output_bottom_detection_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_bottom_detection_subscriptions_post: %s\n" % e)
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

# **api_sounder_data_output_echogram_subscriptions_post**
> int api_sounder_data_output_echogram_subscriptions_post(body=body)

CreateEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.EchogramSubscriptionSpecification() # EchogramSubscriptionSpecification |  (optional)

try:
    # CreateEchogramSubscription
    api_response = api_instance.api_sounder_data_output_echogram_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_echogram_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EchogramSubscriptionSpecification**](EchogramSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_integration_chirp_subscriptions_post**
> int api_sounder_data_output_integration_chirp_subscriptions_post(body=body)

CreateIntegrationChirpSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.IntegrationChirpSubscriptionSpecification() # IntegrationChirpSubscriptionSpecification |  (optional)

try:
    # CreateIntegrationChirpSubscription
    api_response = api_instance.api_sounder_data_output_integration_chirp_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_integration_chirp_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntegrationChirpSubscriptionSpecification**](IntegrationChirpSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_integration_subscriptions_post**
> int api_sounder_data_output_integration_subscriptions_post(body=body)

CreateIntegrationSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.IntegrationSubscriptionSpecification() # IntegrationSubscriptionSpecification |  (optional)

try:
    # CreateIntegrationSubscription
    api_response = api_instance.api_sounder_data_output_integration_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_integration_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntegrationSubscriptionSpecification**](IntegrationSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.NoiseSpectrumSubscriptionSpecification() # NoiseSpectrumSubscriptionSpecification |  (optional)

try:
    # CreateNoiseSpectrumSubscription
    api_response = api_instance.api_sounder_data_output_noise_spectrum_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_noise_spectrum_subscriptions_post: %s\n" % e)
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

# **api_sounder_data_output_sample_data_subscriptions_post**
> int api_sounder_data_output_sample_data_subscriptions_post(body=body)

CreateSampleDataSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.SampleDataSubscriptionSpecification() # SampleDataSubscriptionSpecification |  (optional)

try:
    # CreateSampleDataSubscription
    api_response = api_instance.api_sounder_data_output_sample_data_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_sample_data_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SampleDataSubscriptionSpecification**](SampleDataSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_system_state_subscriptions_post**
> int api_sounder_data_output_system_state_subscriptions_post(body=body)

CreateSystemStateSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.SystemStateSubscriptionSpecification() # SystemStateSubscriptionSpecification |  (optional)

try:
    # CreateSystemStateSubscription
    api_response = api_instance.api_sounder_data_output_system_state_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_system_state_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemStateSubscriptionSpecification**](SystemStateSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_targets_echogram_subscriptions_post**
> int api_sounder_data_output_targets_echogram_subscriptions_post(body=body)

CreateTargetsEchogramSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.TargetsEchogramSubscriptionSpecification() # TargetsEchogramSubscriptionSpecification |  (optional)

try:
    # CreateTargetsEchogramSubscription
    api_response = api_instance.api_sounder_data_output_targets_echogram_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_targets_echogram_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TargetsEchogramSubscriptionSpecification**](TargetsEchogramSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sounder_data_output_targets_integration_subscriptions_post**
> int api_sounder_data_output_targets_integration_subscriptions_post(body=body)

CreateTargetsIntegrationSubscription

### Example
```python
from __future__ import print_function
import time
import ek80dataclient
from ek80dataclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.TargetsIntegrationSubscriptionSpecification() # TargetsIntegrationSubscriptionSpecification |  (optional)

try:
    # CreateTargetsIntegrationSubscription
    api_response = api_instance.api_sounder_data_output_targets_integration_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_targets_integration_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TargetsIntegrationSubscriptionSpecification**](TargetsIntegrationSubscriptionSpecification.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.TsDetectionChirpSubscriptionSpecification() # TsDetectionChirpSubscriptionSpecification |  (optional)

try:
    # CreateTsDetectionChirpSubscription
    api_response = api_instance.api_sounder_data_output_ts_detection_chirp_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_ts_detection_chirp_subscriptions_post: %s\n" % e)
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
api_instance = ek80dataclient.CreateADataSubscriptionApi()
body = ek80dataclient.TsDetectionSubscriptionSpecification() # TsDetectionSubscriptionSpecification |  (optional)

try:
    # CreateTsDetectionSubscription
    api_response = api_instance.api_sounder_data_output_ts_detection_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateADataSubscriptionApi->api_sounder_data_output_ts_detection_subscriptions_post: %s\n" % e)
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

