# ibutsu_client.GroupApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](GroupApi.md#add_group) | **POST** /group | Create a new group
[**get_group**](GroupApi.md#get_group) | **GET** /group/{id} | Get a group
[**get_group_list**](GroupApi.md#get_group_list) | **GET** /group | Get a list of groups
[**update_group**](GroupApi.md#update_group) | **PUT** /group/{id} | Update a group


# **add_group**
> Group add_group(group)

Create a new group

### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import group_api
from ibutsu_client.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_api.GroupApi(api_client)
    group = Group(
        id="a16ad60e-bf23-4195-99dc-594858ad3e5e",
        name="Group A",
    ) # Group | The group

    # example passing only required values which don't have defaults set
    try:
        # Create a new group
        api_response = api_instance.add_group(group)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling GroupApi->add_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**Group**](Group.md)| The group |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Group created |  -  |
**400** | Bad request, probably not enough parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(id)

Get a group

### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import group_api
from ibutsu_client.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_api.GroupApi(api_client)
    id = "id_example" # str | The ID of the group

    # example passing only required values which don't have defaults set
    try:
        # Get a group
        api_response = api_instance.get_group(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling GroupApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the group |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group item |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_list**
> GroupList get_group_list()

Get a list of groups

### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import group_api
from ibutsu_client.model.group_list import GroupList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_api.GroupApi(api_client)
    page = 1 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 1 # int | Set the number of items per page, defaults to 25 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of groups
        api_response = api_instance.get_group_list(page=page, page_size=page_size)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling GroupApi->get_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional]
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional]

### Return type

[**GroupList**](GroupList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(id, group)

Update a group

### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import group_api
from ibutsu_client.model.group import Group
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = group_api.GroupApi(api_client)
    id = "id_example" # str | The ID of the group
    group = Group(
        id="a16ad60e-bf23-4195-99dc-594858ad3e5e",
        name="Group A",
    ) # Group | The updated group

    # example passing only required values which don't have defaults set
    try:
        # Update a group
        api_response = api_instance.update_group(id, group)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling GroupApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the group |
 **group** | [**Group**](Group.md)| The updated group |

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group item |  -  |
**400** | Bad request, probably not enough parameters |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

