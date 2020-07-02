# ibutsu_client.RunApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_run**](RunApi.md#add_run) | **POST** /run | Create a run
[**get_run**](RunApi.md#get_run) | **GET** /run/{id} | Get a single run by ID
[**get_run_list**](RunApi.md#get_run_list) | **GET** /run | Get a list of the test runs
[**update_run**](RunApi.md#update_run) | **PUT** /run/{id} | Update a single run


# **add_run**
> Run add_run(run=run)

Create a run

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
    api_instance = ibutsu_client.RunApi(api_client)
    run = ibutsu_client.Run() # Run | Run item (optional)

    try:
        # Create a run
        api_response = api_instance.add_run(run=run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunApi->add_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run** | [**Run**](Run.md)| Run item | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Run was created |  -  |
**400** | Bad request, JSON required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run**
> Run get_run(id)

Get a single run by ID

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
    api_instance = ibutsu_client.RunApi(api_client)
    id = 'id_example' # str | ID of test run

    try:
        # Get a single run by ID
        api_response = api_instance.get_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunApi->get_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of test run | 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

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
> RunList get_run_list(filter=filter, page=page, page_size=page_size)

Get a list of the test runs

The `filter` parameter takes a list of filters to apply in the form of:       {name}{operator}{value}   where:    - `name` is any valid column in the database   - `operator` is one of `=`, `!`, `＞`, `＜`, `)`, `(`, `~`, `*`   - `value` is what you want to filter by  Operators are simple correspondents to MongoDB's query selectors:    - `=` becomes `$eq`   - `!` becomes `$ne`   - `＞` becomes `$gt`   - `＜` becomes `$lt`   - `)` becomes `$gte`   - `(` becomes `$lte`   - `~` becomes `$regex`   - `*` becomes `$in`   - `@` becomes `$exists`  Notes:  - For the `$exists` operator, \"true\", \"t\", \"yes\", \"y\" and `1` will all be considered true,   all other values are considered false.  Example queries:       /result?filter=metadata.run=63fe5     /result?filter=test_id~neg     /result?filter=result!passed 

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
    api_instance = ibutsu_client.RunApi(api_client)
    filter = ['filter_example'] # list[str] | Fields to filter by (optional)
page = 56 # int | Set the page of items to return, defaults to 1 (optional)
page_size = 56 # int | Set the number of items per page, defaults to 25 (optional)

    try:
        # Get a list of the test runs
        api_response = api_instance.get_run_list(filter=filter, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunApi->get_run_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**list[str]**](str.md)| Fields to filter by | [optional] 
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional] 
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional] 

### Return type

[**RunList**](RunList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Runs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run**
> Run update_run(id, run)

Update a single run

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
    api_instance = ibutsu_client.RunApi(api_client)
    id = 'id_example' # str | ID of the test run
run = ibutsu_client.Run() # Run | The updated test run

    try:
        # Update a single run
        api_response = api_instance.update_run(id, run)
        pprint(api_response)
    except ApiException as e:
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

No authorization required

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

