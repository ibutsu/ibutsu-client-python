# ibutsu_client.RunApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_run**](RunApi.md#add_run) | **POST** /run | Create a run
[**bulk_update**](RunApi.md#bulk_update) | **POST** /runs/bulk-update | Update multiple runs with common metadata
[**get_run**](RunApi.md#get_run) | **GET** /run/{id} | Get a single run by ID (uuid required)
[**get_run_list**](RunApi.md#get_run_list) | **GET** /run | Get a list of the test runs
[**update_run**](RunApi.md#update_run) | **PUT** /run/{id} | Update a single run


# **add_run**
> Run add_run()

Create a run

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import run_api
from ibutsu_client.model.run import Run
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
    api_instance = run_api.RunApi(api_client)
    run = Run(
        id="64c2ab9e-cd64-4815-bf73-83b00c2e650f",
        created="2020-05-15T16:18:32.014053",
        duration=154.778524555,
        source="my-tests",
        start_time="2020-05-15T16:18:32.014053",
        component="login",
        env="qa",
        project_id="44941c55-9736-42f6-acce-ca3c4739d0f3",
        summary={},
        metadata={},
    ) # Run | Run item (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a run
        api_response = api_instance.add_run(run=run)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling RunApi->add_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run** | [**Run**](Run.md)| Run item | [optional]

### Return type

[**Run**](Run.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Run was created |  -  |
**400** | Bad request, JSON required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update**
> RunList bulk_update(update_run)

Update multiple runs with common metadata

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import run_api
from ibutsu_client.model.run_list import RunList
from ibutsu_client.model.update_run import UpdateRun
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
    api_instance = run_api.RunApi(api_client)
    update_run = UpdateRun(
        metadata={},
    ) # UpdateRun | The metadata to add to the test runs
    filter = [
        "filter_example",
    ] # [str] | Fields to filter by (optional)
    page_size = 1 # int | Set the number of items per page, defaults to 25 (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update multiple runs with common metadata
        api_response = api_instance.bulk_update(update_run)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling RunApi->bulk_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update multiple runs with common metadata
        api_response = api_instance.bulk_update(update_run, filter=filter, page_size=page_size)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling RunApi->bulk_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_run** | [**UpdateRun**](UpdateRun.md)| The metadata to add to the test runs |
 **filter** | **[str]**| Fields to filter by | [optional]
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional]

### Return type

[**RunList**](RunList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Run |  -  |
**400** | Bad request, JSON required |  -  |
**401** | Bad request, can only update metadata |  -  |
**404** | Filter(s) returned no Runs |  -  |
**405** | Bad request, cannot update more than 25 runs at a time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run**
> Run get_run(id)

Get a single run by ID (uuid required)

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import run_api
from ibutsu_client.model.run import Run
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
    api_instance = run_api.RunApi(api_client)
    id = "id_example" # str | ID of test run

    # example passing only required values which don't have defaults set
    try:
        # Get a single run by ID (uuid required)
        api_response = api_instance.get_run(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling RunApi->get_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of test run |

### Return type

[**Run**](Run.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run item |  -  |
**404** | Run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_list**
> RunList get_run_list()

Get a list of the test runs

The `filter` parameter takes a list of filters to apply in the form of:       {name}{operator}{value}   where:    - `name` is any valid column in the database   - `operator` is one of `=`, `!`, `＞`, `＜`, `)`, `(`, `~`, `*`   - `value` is what you want to filter by  Operators are simple correspondents to MongoDB's query selectors:    - `=` becomes `$eq`   - `!` becomes `$ne`   - `＞` becomes `$gt`   - `＜` becomes `$lt`   - `)` becomes `$gte`   - `(` becomes `$lte`   - `~` becomes `$regex`   - `*` becomes `$in`   - `@` becomes `$exists`  Notes:  - For the `$exists` operator, \"true\", \"t\", \"yes\", \"y\" and `1` will all be considered true,   all other values are considered false.  Example queries:      /run?filter=metadata.jenkins.job_name=jenkins_job     /run?filter=summary.failures>0 

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import run_api
from ibutsu_client.model.run_list import RunList
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
    api_instance = run_api.RunApi(api_client)
    filter = [
        "filter_example",
    ] # [str] | Fields to filter by (optional)
    estimate = True # bool | Return an estimated count (optional)
    page = 1 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 1 # int | Set the number of items per page, defaults to 25 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of the test runs
        api_response = api_instance.get_run_list(filter=filter, estimate=estimate, page=page, page_size=page_size)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling RunApi->get_run_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **[str]**| Fields to filter by | [optional]
 **estimate** | **bool**| Return an estimated count | [optional]
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional]
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional]

### Return type

[**RunList**](RunList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Runs |  -  |
**201** | Query being evaluated in a celery task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run**
> Run update_run(id, run)

Update a single run

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import run_api
from ibutsu_client.model.run import Run
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
    api_instance = run_api.RunApi(api_client)
    id = "id_example" # str | ID of the test run
    run = Run(
        id="64c2ab9e-cd64-4815-bf73-83b00c2e650f",
        created="2020-05-15T16:18:32.014053",
        duration=154.778524555,
        source="my-tests",
        start_time="2020-05-15T16:18:32.014053",
        component="login",
        env="qa",
        project_id="44941c55-9736-42f6-acce-ca3c4739d0f3",
        summary={},
        metadata={},
    ) # Run | The updated test run

    # example passing only required values which don't have defaults set
    try:
        # Update a single run
        api_response = api_instance.update_run(id, run)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling RunApi->update_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the test run |
 **run** | [**Run**](Run.md)| The updated test run |

### Return type

[**Run**](Run.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Run |  -  |
**400** | Bad request, JSON required |  -  |
**404** | Run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

