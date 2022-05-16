# ibutsu_client.AdminProjectManagementApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_add_project**](AdminProjectManagementApi.md#admin_add_project) | **POST** /admin/project | Administration endpoint to manually add a project. Only accessible to superadmins.
[**admin_delete_project**](AdminProjectManagementApi.md#admin_delete_project) | **DELETE** /admin/project/{id} | Administration endpoint to delete a project. Only accessible to superadmins.
[**admin_get_project**](AdminProjectManagementApi.md#admin_get_project) | **GET** /admin/project/{id} | Administration endpoint to return a project. Only accessible to superadmins.
[**admin_get_project_list**](AdminProjectManagementApi.md#admin_get_project_list) | **GET** /admin/project | Administration endpoint to return a list of projects. Only accessible to superadmins.
[**admin_update_project**](AdminProjectManagementApi.md#admin_update_project) | **PUT** /admin/project/{id} | Administration endpoint to update a project. Only accessible to superadmins.


# **admin_add_project**
> Project admin_add_project()

Administration endpoint to manually add a project. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_project_management_api
from ibutsu_client.model.project import Project
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
    api_instance = admin_project_management_api.AdminProjectManagementApi(api_client)
    project = Project(
        id="44941c55-9736-42f6-acce-ca3c4739d0f3",
        name="my-project",
        title="My project",
        owner_id="6b8b01ad-a17e-4ca1-8df5-fadb41439567",
        group_id="a16ad60e-bf23-4195-99dc-594858ad3e5e",
    ) # Project | A project (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Administration endpoint to manually add a project. Only accessible to superadmins.
        api_response = api_instance.admin_add_project(project=project)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminProjectManagementApi->admin_add_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)| A project | [optional]

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A project was created |  -  |
**400** | Bad request, JSON required |  -  |
**401** | The user needs to be logged in |  -  |
**403** | The user needs to be a superadmin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_project**
> admin_delete_project(id)

Administration endpoint to delete a project. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_project_management_api
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
    api_instance = admin_project_management_api.AdminProjectManagementApi(api_client)
    id = "id_example" # str | The ID of the project to delete

    # example passing only required values which don't have defaults set
    try:
        # Administration endpoint to delete a project. Only accessible to superadmins.
        api_instance.admin_delete_project(id)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminProjectManagementApi->admin_delete_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the project to delete |

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified project was deleted |  -  |
**401** | The user needs to be logged in |  -  |
**403** | The user needs to be a superadmin |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_project**
> Project admin_get_project(id)

Administration endpoint to return a project. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_project_management_api
from ibutsu_client.model.project import Project
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
    api_instance = admin_project_management_api.AdminProjectManagementApi(api_client)
    id = "id_example" # str | The id of a project

    # example passing only required values which don't have defaults set
    try:
        # Administration endpoint to return a project. Only accessible to superadmins.
        api_response = api_instance.admin_get_project(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminProjectManagementApi->admin_get_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of a project |

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a projects |  -  |
**401** | The user needs to be logged in |  -  |
**403** | The user needs to be a superadmin |  -  |
**404** | The project does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_project_list**
> ProjectList admin_get_project_list()

Administration endpoint to return a list of projects. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_project_management_api
from ibutsu_client.model.project_list import ProjectList
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
    api_instance = admin_project_management_api.AdminProjectManagementApi(api_client)
    filter = [
        "filter_example",
    ] # [str] | Fields to filter by (optional)
    page = 1 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 1 # int | Set the number of items per page, defaults to 25 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Administration endpoint to return a list of projects. Only accessible to superadmins.
        api_response = api_instance.admin_get_project_list(filter=filter, page=page, page_size=page_size)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminProjectManagementApi->admin_get_project_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **[str]**| Fields to filter by | [optional]
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional]
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional]

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of projects |  -  |
**401** | The user needs to be logged in |  -  |
**403** | The user needs to be a superadmin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_project**
> Project admin_update_project(id)

Administration endpoint to update a project. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_project_management_api
from ibutsu_client.model.project import Project
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
    api_instance = admin_project_management_api.AdminProjectManagementApi(api_client)
    id = "id_example" # str | The ID of the project to update
    project = Project(
        id="44941c55-9736-42f6-acce-ca3c4739d0f3",
        name="my-project",
        title="My project",
        owner_id="6b8b01ad-a17e-4ca1-8df5-fadb41439567",
        group_id="a16ad60e-bf23-4195-99dc-594858ad3e5e",
    ) # Project |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Administration endpoint to update a project. Only accessible to superadmins.
        api_response = api_instance.admin_update_project(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminProjectManagementApi->admin_update_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Administration endpoint to update a project. Only accessible to superadmins.
        api_response = api_instance.admin_update_project(id, project=project)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminProjectManagementApi->admin_update_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the project to update |
 **project** | [**Project**](Project.md)|  | [optional]

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad reqest, JSON required or not enough parameters |  -  |
**401** | The user needs to be logged in |  -  |
**403** | The user needs to be a superadmin |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

