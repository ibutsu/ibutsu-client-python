# ibutsu_client.ReportApi

All URIs are relative to */api*

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
import ibutsu_client
from ibutsu_client.models.report import Report
from ibutsu_client.models.report_parameters import ReportParameters
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
    api_instance = ibutsu_client.ReportApi(api_client)
    report_parameters = ibutsu_client.ReportParameters() # ReportParameters | The parameters for the report

    try:
        # Create a new report
        api_response = api_instance.add_report(report_parameters)
        print("The response of ReportApi->add_report:\n")
        pprint(api_response)
    except Exception as e:
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
    api_instance = ibutsu_client.ReportApi(api_client)
    id = 'id_example' # str | ID of report to delete

    try:
        # Delete a report
        api_instance.delete_report(id)
    except Exception as e:
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
> bytearray download_report(id, filename)

Download a report

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
    api_instance = ibutsu_client.ReportApi(api_client)
    id = 'id_example' # str | The ID of the report
    filename = 'filename_example' # str | The file name of the downloadable report

    try:
        # Download a report
        api_response = api_instance.download_report(id, filename)
        print("The response of ReportApi->download_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->download_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the report | 
 **filename** | **str**| The file name of the downloadable report | 

### Return type

**bytearray**

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
import ibutsu_client
from ibutsu_client.models.report import Report
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
    api_instance = ibutsu_client.ReportApi(api_client)
    id = 'id_example' # str | The ID of the report

    try:
        # Get a report
        api_response = api_instance.get_report(id)
        print("The response of ReportApi->get_report:\n")
        pprint(api_response)
    except Exception as e:
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
> ReportList get_report_list(page=page, page_size=page_size, project=project)

Get a list of reports

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.report_list import ReportList
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
    api_instance = ibutsu_client.ReportApi(api_client)
    page = 56 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 56 # int | Set the number of items per page, defaults to 25 (optional)
    project = 'project_example' # str | Filter reports by project ID (optional)

    try:
        # Get a list of reports
        api_response = api_instance.get_report_list(page=page, page_size=page_size, project=project)
        print("The response of ReportApi->get_report_list:\n")
        pprint(api_response)
    except Exception as e:
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
> List[GetReportTypes200ResponseInner] get_report_types()

Get a list of report types

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.get_report_types200_response_inner import GetReportTypes200ResponseInner
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
    api_instance = ibutsu_client.ReportApi(api_client)

    try:
        # Get a list of report types
        api_response = api_instance.get_report_types()
        print("The response of ReportApi->get_report_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->get_report_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetReportTypes200ResponseInner]**](GetReportTypes200ResponseInner.md)

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
> bytearray view_report(id, filename)

View a report

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
    api_instance = ibutsu_client.ReportApi(api_client)
    id = 'id_example' # str | The ID of the report
    filename = 'filename_example' # str | The file name of the downloadable report

    try:
        # View a report
        api_response = api_instance.view_report(id, filename)
        print("The response of ReportApi->view_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->view_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the report | 
 **filename** | **str**| The file name of the downloadable report | 

### Return type

**bytearray**

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

