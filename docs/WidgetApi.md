# ibutsu_client.WidgetApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_widget**](WidgetApi.md#get_widget) | **GET** /widget/{id} | Generate data for a dashboard widget
[**get_widget_types**](WidgetApi.md#get_widget_types) | **GET** /widget/types | Get a list of widget types


# **get_widget**
> object get_widget(id, params=params)

Generate data for a dashboard widget

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.WidgetApi(api_client)
    id = 'id_example' # str | The widget identifier
    params = None # object | The parameters for the widget (optional)

    try:
        # Generate data for a dashboard widget
        api_response = api_instance.get_widget(id, params=params)
        print("The response of WidgetApi->get_widget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetApi->get_widget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The widget identifier | 
 **params** | [**object**](.md)| The parameters for the widget | [optional] 

### Return type

**object**

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
> WidgetTypeList get_widget_types(type=type)

Get a list of widget types

A list of widget types

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.widget_type_list import WidgetTypeList
from ibutsu_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.WidgetApi(api_client)
    type = 'type_example' # str | Filter by type of widget (optional)

    try:
        # Get a list of widget types
        api_response = api_instance.get_widget_types(type=type)
        print("The response of WidgetApi->get_widget_types:\n")
        pprint(api_response)
    except Exception as e:
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

