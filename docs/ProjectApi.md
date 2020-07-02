# ibutsu_client.ProjectApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project**](ProjectApi.md#add_project) | **POST** /project | Create a project
[**get_project**](ProjectApi.md#get_project) | **GET** /project/{id} | Get a single project by ID
[**get_project_list**](ProjectApi.md#get_project_list) | **GET** /project | Get a list of projects
[**update_project**](ProjectApi.md#update_project) | **PUT** /project/{id} | Update a project


# **add_project**
> Project add_project(project)

Create a project

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
    api_instance = ibutsu_client.ProjectApi(api_client)
    project = ibutsu_client.Project() # Project | Project

    try:
        # Create a project
        api_response = api_instance.add_project(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->add_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)| Project | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A project was created |  -  |
**400** | Bad request, JSON required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(id)

Get a single project by ID

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
    api_instance = ibutsu_client.ProjectApi(api_client)
    id = 'id_example' # str | ID of test project

    try:
        # Get a single project by ID
        api_response = api_instance.get_project(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of test project | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project object |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_list**
> ProjectList get_project_list(owner_id=owner_id, group_id=group_id, page=page, page_size=page_size)

Get a list of projects

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
    api_instance = ibutsu_client.ProjectApi(api_client)
    owner_id = 'owner_id_example' # str | Filter projects by owner ID (optional)
group_id = 'group_id_example' # str | Filter projects by group ID (optional)
page = 56 # int | Set the page of items to return, defaults to 1 (optional)
page_size = 56 # int | Set the number of items per page, defaults to 25 (optional)

    try:
        # Get a list of projects
        api_response = api_instance.get_project_list(owner_id=owner_id, group_id=group_id, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_project_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| Filter projects by owner ID | [optional] 
 **group_id** | **str**| Filter projects by group ID | [optional] 
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional] 
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional] 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(id, project=project)

Update a project

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
    api_instance = ibutsu_client.ProjectApi(api_client)
    id = 'id_example' # str | ID of test project
project = ibutsu_client.Project() # Project | Project (optional)

    try:
        # Update a project
        api_response = api_instance.update_project(id, project=project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of test project | 
 **project** | [**Project**](Project.md)| Project | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project object |  -  |
**400** | Bad request, JSON required or not enough parameters |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

