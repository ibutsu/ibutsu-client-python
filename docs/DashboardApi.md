# ibutsu_client.DashboardApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dashboard**](DashboardApi.md#add_dashboard) | **POST** /dashboard | Create a dashboard
[**delete_dashboard**](DashboardApi.md#delete_dashboard) | **DELETE** /dashboard/{id} | Delete a dashboard
[**get_dashboard**](DashboardApi.md#get_dashboard) | **GET** /dashboard/{id} | Get a single dashboard by ID
[**get_dashboard_list**](DashboardApi.md#get_dashboard_list) | **GET** /dashboard | Get a list of dashboards
[**update_dashboard**](DashboardApi.md#update_dashboard) | **PUT** /dashboard/{id} | Update a dashboard


# **add_dashboard**
> Dashboard add_dashboard(dashboard)

Create a dashboard

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import dashboard_api
from ibutsu_client.model.dashboard import Dashboard
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
    api_instance = dashboard_api.DashboardApi(api_client)
    dashboard = Dashboard(
        id="62faa4ce-d264-46c2-813e-579949c8ab9b",
        title="My Dashboard",
        description="A dashboard for me",
        filters="",
        project_id="44941c55-9736-42f6-acce-ca3c4739d0f3",
        user_id="90be2a4a-1a4d-4779-b40f-f08ccd7101d5",
    ) # Dashboard | Dashboard

    # example passing only required values which don't have defaults set
    try:
        # Create a dashboard
        api_response = api_instance.add_dashboard(dashboard)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling DashboardApi->add_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard** | [**Dashboard**](Dashboard.md)| Dashboard |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A dashboard was created |  -  |
**400** | Bad request, JSON required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> delete_dashboard(id)

Delete a dashboard

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import dashboard_api
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
    api_instance = dashboard_api.DashboardApi(api_client)
    id = "id_example" # str | ID of dashboard to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a dashboard
        api_instance.delete_dashboard(id)
    except ibutsu_client.ApiException as e:
        print("Exception when calling DashboardApi->delete_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of dashboard to delete |

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
**200** | The dashboard was deleted |  -  |
**404** | The dashboard was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> Dashboard get_dashboard(id)

Get a single dashboard by ID

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import dashboard_api
from ibutsu_client.model.dashboard import Dashboard
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
    api_instance = dashboard_api.DashboardApi(api_client)
    id = "id_example" # str | ID of test dashboard

    # example passing only required values which don't have defaults set
    try:
        # Get a single dashboard by ID
        api_response = api_instance.get_dashboard(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling DashboardApi->get_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of test dashboard |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard object |  -  |
**404** | Dashboard not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_list**
> DashboardList get_dashboard_list()

Get a list of dashboards

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import dashboard_api
from ibutsu_client.model.dashboard_list import DashboardList
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
    api_instance = dashboard_api.DashboardApi(api_client)
    filter = [
        "filter_example",
    ] # [str] | Fields to filter by (optional)
    project_id = "project_id_example" # str | Filter dashboards by project ID (optional)
    user_id = "user_id_example" # str | Filter dashboards by user ID (optional)
    page = 1 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 1 # int | Set the number of items per page, defaults to 25 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of dashboards
        api_response = api_instance.get_dashboard_list(filter=filter, project_id=project_id, user_id=user_id, page=page, page_size=page_size)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling DashboardApi->get_dashboard_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **[str]**| Fields to filter by | [optional]
 **project_id** | **str**| Filter dashboards by project ID | [optional]
 **user_id** | **str**| Filter dashboards by user ID | [optional]
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional]
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional]

### Return type

[**DashboardList**](DashboardList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of dashboards |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> Dashboard update_dashboard(id)

Update a dashboard

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import dashboard_api
from ibutsu_client.model.dashboard import Dashboard
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
    api_instance = dashboard_api.DashboardApi(api_client)
    id = "id_example" # str | ID of test dashboard
    dashboard = Dashboard(
        id="62faa4ce-d264-46c2-813e-579949c8ab9b",
        title="My Dashboard",
        description="A dashboard for me",
        filters="",
        project_id="44941c55-9736-42f6-acce-ca3c4739d0f3",
        user_id="90be2a4a-1a4d-4779-b40f-f08ccd7101d5",
    ) # Dashboard | Dashboard (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a dashboard
        api_response = api_instance.update_dashboard(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling DashboardApi->update_dashboard: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a dashboard
        api_response = api_instance.update_dashboard(id, dashboard=dashboard)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling DashboardApi->update_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of test dashboard |
 **dashboard** | [**Dashboard**](Dashboard.md)| Dashboard | [optional]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard object |  -  |
**400** | Bad request, JSON required or not enough parameters |  -  |
**404** | Dashboard not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

