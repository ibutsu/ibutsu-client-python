# ibutsu_client.AdminUserManagementApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_add_user**](AdminUserManagementApi.md#admin_add_user) | **POST** /admin/user | Administration endpoint to manually add a user. Only accessible to superadmins.
[**admin_delete_user**](AdminUserManagementApi.md#admin_delete_user) | **DELETE** /admin/user/{id} | Administration endpoint to delete a user. Only accessible to superadmins.
[**admin_get_user**](AdminUserManagementApi.md#admin_get_user) | **GET** /admin/user/{id} | Administration endpoint to return a user. Only accessible to superadmins.
[**admin_get_user_list**](AdminUserManagementApi.md#admin_get_user_list) | **GET** /admin/user | Administration endpoint to return a list of users. Only accessible to superadmins.
[**admin_update_user**](AdminUserManagementApi.md#admin_update_user) | **PUT** /admin/user/{id} | Administration endpoint to update a user. Only accessible to superadmins.


# **admin_add_user**
> User admin_add_user()

Administration endpoint to manually add a user. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_user_management_api
from ibutsu_client.model.user import User
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
    api_instance = admin_user_management_api.AdminUserManagementApi(api_client)
    user = User(
        id="81e2c9d6-1593-4559-af4f-90f6f1f8fa03",
        email="user@domain.com",
        name="Namey McNameface",
        is_superadmin=False,
        is_active=True,
        group_id="a16ad60e-bf23-4195-99dc-594858ad3e5e",
    ) # User | A user (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Administration endpoint to manually add a user. Only accessible to superadmins.
        api_response = api_instance.admin_add_user(user=user)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminUserManagementApi->admin_add_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| A user | [optional]

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A user was created |  -  |
**400** | Bad request, JSON required |  -  |
**401** | The user needs to be logged in |  -  |
**403** | The user needs to be a superadmin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_user**
> admin_delete_user(id)

Administration endpoint to delete a user. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_user_management_api
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
    api_instance = admin_user_management_api.AdminUserManagementApi(api_client)
    id = "id_example" # str | The ID of the user to delete

    # example passing only required values which don't have defaults set
    try:
        # Administration endpoint to delete a user. Only accessible to superadmins.
        api_instance.admin_delete_user(id)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminUserManagementApi->admin_delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the user to delete |

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
**200** | The specified user was deleted |  -  |
**401** | The user needs to be logged in |  -  |
**403** | The user needs to be a superadmin |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_user**
> User admin_get_user(id)

Administration endpoint to return a user. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_user_management_api
from ibutsu_client.model.user import User
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
    api_instance = admin_user_management_api.AdminUserManagementApi(api_client)
    id = "id_example" # str | The id of a user

    # example passing only required values which don't have defaults set
    try:
        # Administration endpoint to return a user. Only accessible to superadmins.
        api_response = api_instance.admin_get_user(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminUserManagementApi->admin_get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of a user |

### Return type

[**User**](User.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a user |  -  |
**401** | The querying user needs to be logged in |  -  |
**403** | The querying user needs to be a superadmin |  -  |
**404** | The requested user does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_user_list**
> UserList admin_get_user_list()

Administration endpoint to return a list of users. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_user_management_api
from ibutsu_client.model.user_list import UserList
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
    api_instance = admin_user_management_api.AdminUserManagementApi(api_client)
    filter = [
        "filter_example",
    ] # [str] | Fields to filter by (optional)
    page = 1 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 1 # int | Set the number of items per page, defaults to 25 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Administration endpoint to return a list of users. Only accessible to superadmins.
        api_response = api_instance.admin_get_user_list(filter=filter, page=page, page_size=page_size)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminUserManagementApi->admin_get_user_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **[str]**| Fields to filter by | [optional]
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional]
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional]

### Return type

[**UserList**](UserList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of users |  -  |
**401** | The user needs to be logged in |  -  |
**403** | The user needs to be a superadmin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_user**
> User admin_update_user(id)

Administration endpoint to update a user. Only accessible to superadmins.

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import admin_user_management_api
from ibutsu_client.model.user import User
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
    api_instance = admin_user_management_api.AdminUserManagementApi(api_client)
    id = "id_example" # str | The ID of the user to update
    user = User(
        id="81e2c9d6-1593-4559-af4f-90f6f1f8fa03",
        email="user@domain.com",
        name="Namey McNameface",
        is_superadmin=False,
        is_active=True,
        group_id="a16ad60e-bf23-4195-99dc-594858ad3e5e",
    ) # User |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Administration endpoint to update a user. Only accessible to superadmins.
        api_response = api_instance.admin_update_user(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminUserManagementApi->admin_update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Administration endpoint to update a user. Only accessible to superadmins.
        api_response = api_instance.admin_update_user(id, user=user)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling AdminUserManagementApi->admin_update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the user to update |
 **user** | [**User**](User.md)|  | [optional]

### Return type

[**User**](User.md)

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
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

