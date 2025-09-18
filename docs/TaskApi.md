# ibutsu_client.TaskApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](TaskApi.md#get_task) | **GET** /task/{id} | Get the status or result of a task


# **get_task**
> object get_task(id)

Get the status or result of a task

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
    api_instance = ibutsu_client.TaskApi(api_client)
    id = 'id_example' # str | The ID of the task

    try:
        # Get the status or result of a task
        api_response = api_instance.get_task(id)
        print("The response of TaskApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the task | 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The task has completed and the data has been returned |  -  |
**206** | The task either doesn&#39;t exist or hasn&#39;t finished |  -  |
**203** | Error occurred in the task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

