# ibutsu_client.WidgetApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_widget**](WidgetApi.md#get_widget) | **GET** /widget/{id} | Generate data for a dashboard widget
[**get_widget_types**](WidgetApi.md#get_widget_types) | **GET** /widget/types | Get a list of widget types


# **get_widget**
> object get_widget(id, params=params)

Generate data for a dashboard widget

### Example

```python
from __future__ import print_function
import time
import ibutsu_client
from ibutsu_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.WidgetApi(api_client)
    id = 'id_example' # str | The widget identifier
params = None # object | The parameters for the widget (optional)

    try:
        # Generate data for a dashboard widget
        api_response = api_instance.get_widget(id, params=params)
        pprint(api_response)
    except ApiException as e:
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

No authorization required

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

### Example

```python
from __future__ import print_function
import time
import ibutsu_client
from ibutsu_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.WidgetApi(api_client)
    
    try:
        # Get a list of widget types
        api_response = api_instance.get_widget_types()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WidgetApi->get_widget_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WidgetTypeList**](WidgetTypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of types of widgets available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

