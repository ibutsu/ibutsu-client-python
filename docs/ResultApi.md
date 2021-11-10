# ibutsu_client.ResultApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_result**](ResultApi.md#add_result) | **POST** /result | Create a test result
[**get_result**](ResultApi.md#get_result) | **GET** /result/{id} | Get a single result
[**get_result_list**](ResultApi.md#get_result_list) | **GET** /result | Get the list of results.
[**update_result**](ResultApi.md#update_result) | **PUT** /result/{id} | Updates a single result


# **add_result**
> Result add_result()

Create a test result

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import result_api
from ibutsu_client.model.result import Result
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
    api_instance = result_api.ResultApi(api_client)
    result = Result(
        id="a16ad60e-bf23-4195-99dc-594858ad3e5e",
        test_id="test_click_on_button",
        start_time="start_time_example",
        duration=3.14,
        result="passed",
        component="login",
        env="qa",
        run_id="64c2ab9e-cd64-4815-bf73-83b00c2e650f",
        project_id="44941c55-9736-42f6-acce-ca3c4739d0f3",
        metadata={},
        params={},
        source="source_example",
    ) # Result | Result item (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a test result
        api_response = api_instance.add_result(result=result)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ResultApi->add_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result** | [**Result**](Result.md)| Result item | [optional]

### Return type

[**Result**](Result.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request, JSON required or not enough parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result**
> Result get_result(id)

Get a single result

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import result_api
from ibutsu_client.model.result import Result
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
    api_instance = result_api.ResultApi(api_client)
    id = "id_example" # str | ID of result to return (uuid required)

    # example passing only required values which don't have defaults set
    try:
        # Get a single result
        api_response = api_instance.get_result(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ResultApi->get_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of result to return (uuid required) |

### Return type

[**Result**](Result.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result item |  -  |
**404** | Result not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_list**
> ResultList get_result_list()

Get the list of results.

The `filter` parameter takes a list of filters to apply in the form of:      {name}{operator}{value}  where:    - `name` is any valid column in the database   - `operator` is one of `=`, `!`, `＞`, `＜`, `)`, `(`, `~`, `*`   - `value` is what you want to filter by  Operators are simple correspondents to MongoDB's query selectors:    - `=` becomes `$eq`   - `!` becomes `$ne`   - `＞` becomes `$gt`   - `＜` becomes `$lt`   - `)` becomes `$gte`   - `(` becomes `$lte`   - `~` becomes `$regex`   - `*` becomes `$in`   - `@` becomes `$exists`  Notes:  - For the `$exists` operator, \"true\", \"t\", \"yes\", \"y\" and `1` will all be considered true,   all other values are considered false.  Example queries:      /result?filter=metadata.run=63fe5     /result?filter=test_id~neg     /result?filter=result!passed 

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import result_api
from ibutsu_client.model.result_list import ResultList
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
    api_instance = result_api.ResultApi(api_client)
    filter = [
        "filter_example",
    ] # [str] | Fields to filter by (optional)
    estimate = True # bool | Return an estimated count (optional)
    page = 1 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 1 # int | Set the number of items per page, defaults to 25 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of results.
        api_response = api_instance.get_result_list(filter=filter, estimate=estimate, page=page, page_size=page_size)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ResultApi->get_result_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **[str]**| Fields to filter by | [optional]
 **estimate** | **bool**| Return an estimated count | [optional]
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional]
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional]

### Return type

[**ResultList**](ResultList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**201** | Query being evaluated in a celery task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_result**
> Result update_result(id)

Updates a single result

### Example

* Bearer (JWT) Authentication (jwt):

```python
import time
import ibutsu_client
from ibutsu_client.api import result_api
from ibutsu_client.model.result import Result
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
    api_instance = result_api.ResultApi(api_client)
    id = "id_example" # str | ID of result to update
    result = Result(
        id="a16ad60e-bf23-4195-99dc-594858ad3e5e",
        test_id="test_click_on_button",
        start_time="start_time_example",
        duration=3.14,
        result="passed",
        component="login",
        env="qa",
        run_id="64c2ab9e-cd64-4815-bf73-83b00c2e650f",
        project_id="44941c55-9736-42f6-acce-ca3c4739d0f3",
        metadata={},
        params={},
        source="source_example",
    ) # Result | Result item (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a single result
        api_response = api_instance.update_result(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ResultApi->update_result: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a single result
        api_response = api_instance.update_result(id, result=result)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ResultApi->update_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of result to update |
 **result** | [**Result**](Result.md)| Result item | [optional]

### Return type

[**Result**](Result.md)

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
**404** | Result not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

