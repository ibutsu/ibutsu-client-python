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
> Project admin_add_project(project=project)

Administration endpoint to manually add a project. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.project import Project
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
    api_instance = ibutsu_client.AdminProjectManagementApi(api_client)
    project = ibutsu_client.Project() # Project | A project object (optional)

    try:
        # Administration endpoint to manually add a project. Only accessible to superadmins.
        api_response = api_instance.admin_add_project(project=project)
        print("The response of AdminProjectManagementApi->admin_add_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminProjectManagementApi->admin_add_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)| A project object | [optional] 

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
    api_instance = ibutsu_client.AdminProjectManagementApi(api_client)
    id = 'id_example' # str | The ID of the project to delete

    try:
        # Administration endpoint to delete a project. Only accessible to superadmins.
        api_instance.admin_delete_project(id)
    except Exception as e:
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
import ibutsu_client
from ibutsu_client.models.project import Project
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
    api_instance = ibutsu_client.AdminProjectManagementApi(api_client)
    id = 'id_example' # str | The id of a project

    try:
        # Administration endpoint to return a project. Only accessible to superadmins.
        api_response = api_instance.admin_get_project(id)
        print("The response of AdminProjectManagementApi->admin_get_project:\n")
        pprint(api_response)
    except Exception as e:
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
> ProjectList admin_get_project_list(filter=filter, page=page, page_size=page_size)

Administration endpoint to return a list of projects. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.project_list import ProjectList
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
    api_instance = ibutsu_client.AdminProjectManagementApi(api_client)
    filter = ['filter_example'] # List[str] | Fields to filter by (optional)
    page = 56 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 56 # int | Set the number of items per page, defaults to 25 (optional)

    try:
        # Administration endpoint to return a list of projects. Only accessible to superadmins.
        api_response = api_instance.admin_get_project_list(filter=filter, page=page, page_size=page_size)
        print("The response of AdminProjectManagementApi->admin_get_project_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminProjectManagementApi->admin_get_project_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**List[str]**](str.md)| Fields to filter by | [optional] 
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
> Project admin_update_project(id, project=project)

Administration endpoint to update a project. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.project import Project
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
    api_instance = ibutsu_client.AdminProjectManagementApi(api_client)
    id = 'id_example' # str | The ID of the project to update
    project = ibutsu_client.Project() # Project | A project object (optional)

    try:
        # Administration endpoint to update a project. Only accessible to superadmins.
        api_response = api_instance.admin_update_project(id, project=project)
        print("The response of AdminProjectManagementApi->admin_update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminProjectManagementApi->admin_update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the project to update | 
 **project** | [**Project**](Project.md)| A project object | [optional] 

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

