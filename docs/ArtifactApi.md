# ibutsu_client.ArtifactApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_artifact**](ArtifactApi.md#delete_artifact) | **DELETE** /artifact/{id} | Delete an artifact
[**download_artifact**](ArtifactApi.md#download_artifact) | **GET** /artifact/{id}/download | Download an artifact
[**get_artifact**](ArtifactApi.md#get_artifact) | **GET** /artifact/{id} | Get a single artifact
[**get_artifact_list**](ArtifactApi.md#get_artifact_list) | **GET** /artifact | Get a (filtered) list of artifacts
[**upload_artifact**](ArtifactApi.md#upload_artifact) | **POST** /artifact | Uploads a test run artifact
[**view_artifact**](ArtifactApi.md#view_artifact) | **GET** /artifact/{id}/view | Stream an artifact directly to the client/browser


# **delete_artifact**
> delete_artifact(id)

Delete an artifact

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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    id = 'id_example' # str | ID of artifact to delete

    try:
        # Delete an artifact
        api_instance.delete_artifact(id)
    except Exception as e:
        print("Exception when calling ArtifactApi->delete_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of artifact to delete | 

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
**200** | The artifact was deleted |  -  |
**404** | The artifact was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact**
> bytearray download_artifact(id)

Download an artifact

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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    id = 'id_example' # str | ID of artifact to return

    try:
        # Download an artifact
        api_response = api_instance.download_artifact(id)
        print("The response of ArtifactApi->download_artifact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactApi->download_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of artifact to return | 

### Return type

**bytearray**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, image/jpeg, image/png, image/gif, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File contents |  -  |
**404** | Artifact not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact**
> Artifact get_artifact(id)

Get a single artifact

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.artifact import Artifact
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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    id = 'id_example' # str | ID of artifact to return

    try:
        # Get a single artifact
        api_response = api_instance.get_artifact(id)
        print("The response of ArtifactApi->get_artifact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactApi->get_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of artifact to return | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Artifact object |  -  |
**404** | Artifact not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_list**
> ArtifactList get_artifact_list(result_id=result_id, run_id=run_id, page=page, page_size=page_size)

Get a (filtered) list of artifacts

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.artifact_list import ArtifactList
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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    result_id = 'result_id_example' # str | The result ID to filter by (optional)
    run_id = 'run_id_example' # str | The run ID to filter by (optional)
    page = 56 # int | Set the page of items to return, defaults to 1 (optional)
    page_size = 56 # int | Set the number of items per page, defaults to 25 (optional)

    try:
        # Get a (filtered) list of artifacts
        api_response = api_instance.get_artifact_list(result_id=result_id, run_id=run_id, page=page, page_size=page_size)
        print("The response of ArtifactApi->get_artifact_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactApi->get_artifact_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The result ID to filter by | [optional] 
 **run_id** | **str**| The run ID to filter by | [optional] 
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional] 
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional] 

### Return type

[**ArtifactList**](ArtifactList.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of artifacts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_artifact**
> Artifact upload_artifact(filename, file, result_id=result_id, run_id=run_id, additional_metadata=additional_metadata)

Uploads a test run artifact

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.artifact import Artifact
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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    filename = 'filename_example' # str | name of the file
    file = None # bytearray | file to upload
    result_id = 'result_id_example' # str | ID of result to attach artifact to (optional)
    run_id = 'run_id_example' # str | ID of run to attach artifact to (optional)
    additional_metadata = None # object | Additional data to pass to server (optional)

    try:
        # Uploads a test run artifact
        api_response = api_instance.upload_artifact(filename, file, result_id=result_id, run_id=run_id, additional_metadata=additional_metadata)
        print("The response of ArtifactApi->upload_artifact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactApi->upload_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| name of the file | 
 **file** | **bytearray**| file to upload | 
 **result_id** | **str**| ID of result to attach artifact to | [optional] 
 **run_id** | **str**| ID of run to attach artifact to | [optional] 
 **additional_metadata** | [**object**](object.md)| Additional data to pass to server | [optional] 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An artifact was created |  -  |
**400** | Bad request, not enough parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_artifact**
> bytearray view_artifact(id)

Stream an artifact directly to the client/browser

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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    id = 'id_example' # str | ID of artifact to return

    try:
        # Stream an artifact directly to the client/browser
        api_response = api_instance.view_artifact(id)
        print("The response of ArtifactApi->view_artifact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactApi->view_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of artifact to return | 

### Return type

**bytearray**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, image/jpeg, image/png, image/gif, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File contents |  -  |
**404** | Artifact not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

