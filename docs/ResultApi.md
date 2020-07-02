# ibutsu_client.ResultApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_result**](ResultApi.md#add_result) | **POST** /result | Create a test result
[**get_result**](ResultApi.md#get_result) | **GET** /result/{id} | Get a single result
[**get_result_list**](ResultApi.md#get_result_list) | **GET** /result | Get the list of results.
[**update_result**](ResultApi.md#update_result) | **PUT** /result/{id} | Updates a single result


# **add_result**
> Result add_result(result=result)

Create a test result

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
    api_instance = ibutsu_client.ResultApi(api_client)
    result = ibutsu_client.Result() # Result | Result item (optional)

    try:
        # Create a test result
        api_response = api_instance.add_result(result=result)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResultApi->add_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result** | [**Result**](Result.md)| Result item | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

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
    api_instance = ibutsu_client.ResultApi(api_client)
    id = 'id_example' # str | ID of pet to return

    try:
        # Get a single result
        api_response = api_instance.get_result(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResultApi->get_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of pet to return | 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

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
> ResultList get_result_list(filter=filter, page=page, page_size=page_size)

Get the list of results.

The `filter` parameter takes a list of filters to apply in the form of:      {name}{operator}{value}  where:    - `name` is any valid column in the database   - `operator` is one of `=`, `!`, `＞`, `＜`, `)`, `(`, `~`, `*`   - `value` is what you want to filter by  Operators are simple correspondents to MongoDB's query selectors:    - `=` becomes `$eq`   - `!` becomes `$ne`   - `＞` becomes `$gt`   - `＜` becomes `$lt`   - `)` becomes `$gte`   - `(` becomes `$lte`   - `~` becomes `$regex`   - `*` becomes `$in`   - `@` becomes `$exists`  Notes:  - For the `$exists` operator, \"true\", \"t\", \"yes\", \"y\" and `1` will all be considered true,   all other values are considered false.  Example queries:      /result?filter=metadata.run=63fe5     /result?filter=test_id~neg     /result?filter=result!passed 

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
    api_instance = ibutsu_client.ResultApi(api_client)
    filter = ['filter_example'] # list[str] | Fields to filter by (optional)
page = 56 # int | Set the page of items to return, defaults to 1 (optional)
page_size = 56 # int | Set the number of items per page, defaults to 25 (optional)

    try:
        # Get the list of results.
        api_response = api_instance.get_result_list(filter=filter, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResultApi->get_result_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**list[str]**](str.md)| Fields to filter by | [optional] 
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional] 
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional] 

### Return type

[**ResultList**](ResultList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_result**
> Result update_result(id, result=result)

Updates a single result

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
    api_instance = ibutsu_client.ResultApi(api_client)
    id = 'id_example' # str | ID of result to update
result = ibutsu_client.Result() # Result | Result item (optional)

    try:
        # Updates a single result
        api_response = api_instance.update_result(id, result=result)
        pprint(api_response)
    except ApiException as e:
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

No authorization required

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

