# ibutsu_client.WidgetConfigApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_widget_config**](WidgetConfigApi.md#add_widget_config) | **POST** /widget-config | Create a widget configuration
[**delete_widget_config**](WidgetConfigApi.md#delete_widget_config) | **DELETE** /widget-config/{id} | Delete a widget configuration
[**get_widget_config**](WidgetConfigApi.md#get_widget_config) | **GET** /widget-config/{id} | Get a single widget configuration
[**get_widget_config_list**](WidgetConfigApi.md#get_widget_config_list) | **GET** /widget-config | Get the list of widget configurations
[**update_widget_config**](WidgetConfigApi.md#update_widget_config) | **PUT** /widget-config/{id} | Updates a single widget configuration


# **add_widget_config**
> WidgetConfig add_widget_config(widget_config=widget_config)

Create a widget configuration

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
    api_instance = ibutsu_client.WidgetConfigApi(api_client)
    widget_config = ibutsu_client.WidgetConfig() # WidgetConfig | Widget configuration (optional)

    try:
        # Create a widget configuration
        api_response = api_instance.add_widget_config(widget_config=widget_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WidgetConfigApi->add_widget_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_config** | [**WidgetConfig**](WidgetConfig.md)| Widget configuration | [optional] 

### Return type

[**WidgetConfig**](WidgetConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request, JSON required or not enough parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_widget_config**
> delete_widget_config(id)

Delete a widget configuration

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
    api_instance = ibutsu_client.WidgetConfigApi(api_client)
    id = 'id_example' # str | ID of widget configuration to delete

    try:
        # Delete a widget configuration
        api_instance.delete_widget_config(id)
    except ApiException as e:
        print("Exception when calling WidgetConfigApi->delete_widget_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of widget configuration to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The widget configuration was deleted |  -  |
**404** | The widget configuration was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_config**
> WidgetConfig get_widget_config(id)

Get a single widget configuration

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
    api_instance = ibutsu_client.WidgetConfigApi(api_client)
    id = 'id_example' # str | ID of widget config to return

    try:
        # Get a single widget configuration
        api_response = api_instance.get_widget_config(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WidgetConfigApi->get_widget_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of widget config to return | 

### Return type

[**WidgetConfig**](WidgetConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WidgetConfig item |  -  |
**404** | WidgetConfig not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_config_list**
> WidgetConfigList get_widget_config_list(filter=filter, page=page, page_size=page_size)

Get the list of widget configurations

A list of widget configurations

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
    api_instance = ibutsu_client.WidgetConfigApi(api_client)
    filter = ['filter_example'] # list[str] | Fields to filter by (optional)
page = 56 # int | Set the page of items to return, defaults to 1 (optional)
page_size = 56 # int | Set the number of items per page, defaults to 25 (optional)

    try:
        # Get the list of widget configurations
        api_response = api_instance.get_widget_config_list(filter=filter, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WidgetConfigApi->get_widget_config_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**list[str]**](str.md)| Fields to filter by | [optional] 
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional] 
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional] 

### Return type

[**WidgetConfigList**](WidgetConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_widget_config**
> WidgetConfig update_widget_config(id, widget_config=widget_config)

Updates a single widget configuration

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
    api_instance = ibutsu_client.WidgetConfigApi(api_client)
    id = 'id_example' # str | ID of widget configuration to update
widget_config = ibutsu_client.WidgetConfig() # WidgetConfig | Widget configuration (optional)

    try:
        # Updates a single widget configuration
        api_response = api_instance.update_widget_config(id, widget_config=widget_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WidgetConfigApi->update_widget_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of widget configuration to update | 
 **widget_config** | [**WidgetConfig**](WidgetConfig.md)| Widget configuration | [optional] 

### Return type

[**WidgetConfig**](WidgetConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad reqest, JSON required or not enough parameters |  -  |
**404** | Widget configuration not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

