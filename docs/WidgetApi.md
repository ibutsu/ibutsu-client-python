# ibutsu_client.WidgetApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_widget**](WidgetApi.md#get_widget) | **GET** /widget/{id} | Generate data for a dashboard widget
[**get_widget_types**](WidgetApi.md#get_widget_types) | **GET** /widget/types | Get a list of widget types


# **get_widget**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_widget(id)

Generate data for a dashboard widget

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import widget_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwt
configuration = ibutsu_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = widget_api.WidgetApi(api_client)
    id = "id_example" # str | The widget identifier
    params = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | The parameters for the widget (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generate data for a dashboard widget
        api_response = api_instance.get_widget(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling WidgetApi->get_widget: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate data for a dashboard widget
        api_response = api_instance.get_widget(id, params=params)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling WidgetApi->get_widget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The widget identifier |
 **params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| The parameters for the widget | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data returned for the widget |  -  |
**404** | No widget of this type exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_types**
> WidgetTypeList get_widget_types()

Get a list of widget types

A list of widget types

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import widget_api
from ibutsu_client.model.widget_type_list import WidgetTypeList
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): jwt
configuration = ibutsu_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = widget_api.WidgetApi(api_client)
    type = "type_example" # str | Filter by type of widget (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of widget types
        api_response = api_instance.get_widget_types(type=type)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling WidgetApi->get_widget_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter by type of widget | [optional]

### Return type

[**WidgetTypeList**](WidgetTypeList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of types of widgets available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

