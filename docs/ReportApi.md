# ibutsu_client.ReportApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_report**](ReportApi.md#add_report) | **POST** /report | Create a new report
[**delete_report**](ReportApi.md#delete_report) | **DELETE** /report/{id} | Delete a report
[**download_report**](ReportApi.md#download_report) | **GET** /report/{id}/download/{filename} | Download a report
[**get_report**](ReportApi.md#get_report) | **GET** /report/{id} | Get a report
[**get_report_list**](ReportApi.md#get_report_list) | **GET** /report | Get a list of reports
[**get_report_types**](ReportApi.md#get_report_types) | **GET** /report/types | Get a list of report types
[**view_report**](ReportApi.md#view_report) | **GET** /report/{id}/view/{filename} | View a report


# **add_report**
> Report add_report(report_parameters)

Create a new report

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import report_api
from ibutsu_client.model.report_parameters import ReportParameters
from ibutsu_client.model.report import Report
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
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
    api_instance = report_api.ReportApi(api_client)
    report_parameters = ReportParameters(
        type="dashboard",
        filter="test_navigation",
        source="iqe-jenkins",
    ) # ReportParameters | The parameters for the report

    # example passing only required values which don't have defaults set
    try:
        # Create a new report
        api_response = api_instance.add_report(report_parameters)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ReportApi->add_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_parameters** | [**ReportParameters**](ReportParameters.md)| The parameters for the report |

### Return type

[**Report**](Report.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Report created |  -  |
**400** | Bad request, probably not enough parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report**
> delete_report(id)

Delete a report

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import report_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
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
    api_instance = report_api.ReportApi(api_client)
    id = "id_example" # str | ID of report to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a report
        api_instance.delete_report(id)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ReportApi->delete_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of report to delete |

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
**200** | The report was deleted |  -  |
**404** | The report was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_report**
> file_type download_report(id, filename)

Download a report

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import report_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
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
    api_instance = report_api.ReportApi(api_client)
    id = "id_example" # str | The ID of the report
    filename = "filename_example" # str | The file name of the downloadable report

    # example passing only required values which don't have defaults set
    try:
        # Download a report
        api_response = api_instance.download_report(id, filename)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ReportApi->download_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the report |
 **filename** | **str**| The file name of the downloadable report |

### Return type

**file_type**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/csv, application/json, text/html, application/zip


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File contents |  -  |
**404** | Artifact not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> Report get_report(id)

Get a report

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import report_api
from ibutsu_client.model.report import Report
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
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
    api_instance = report_api.ReportApi(api_client)
    id = "id_example" # str | The ID of the report

    # example passing only required values which don't have defaults set
    try:
        # Get a report
        api_response = api_instance.get_report(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ReportApi->get_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the report |

### Return type

[**Report**](Report.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report item |  -  |
**404** | Report not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_list**
> ReportList get_report_list()

Get a list of reports

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import report_api
from ibutsu_client.model.report_list import ReportList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
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
    api_instance = report_api.ReportApi(api_client)
    page = 1 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 1 # int | Set the number of items per page, defaults to 25 (optional)
    project = "project_example" # str | Filter reports by project ID (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of reports
        api_response = api_instance.get_report_list(page=page, page_size=page_size, project=project)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ReportApi->get_report_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional]
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional]
 **project** | **str**| Filter reports by project ID | [optional]

### Return type

[**ReportList**](ReportList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of reports |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_types**
> [InlineResponse200] get_report_types()

Get a list of report types

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import report_api
from ibutsu_client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
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
    api_instance = report_api.ReportApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of report types
        api_response = api_instance.get_report_types()
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ReportApi->get_report_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of types of reports available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_report**
> file_type view_report(id, filename)

View a report

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import report_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
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
    api_instance = report_api.ReportApi(api_client)
    id = "id_example" # str | The ID of the report
    filename = "filename_example" # str | The file name of the downloadable report

    # example passing only required values which don't have defaults set
    try:
        # View a report
        api_response = api_instance.view_report(id, filename)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ReportApi->view_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the report |
 **filename** | **str**| The file name of the downloadable report |

### Return type

**file_type**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/csv, application/json, text/html, application/zip


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File contents |  -  |
**404** | Artifact not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

