# ibutsu_client.ArtifactApi

All URIs are relative to *http://localhost/api*

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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    id = 'id_example' # str | ID of artifact to delete

    try:
        # Delete an artifact
        api_instance.delete_artifact(id)
    except ApiException as e:
        print("Exception when calling ArtifactApi->delete_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of artifact to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

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
> file download_artifact(id)

Download an artifact

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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    id = 'id_example' # str | ID of artifact to return

    try:
        # Download an artifact
        api_response = api_instance.download_artifact(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactApi->download_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of artifact to return | 

### Return type

**file**

### Authorization

No authorization required

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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    id = 'id_example' # str | ID of artifact to return

    try:
        # Get a single artifact
        api_response = api_instance.get_artifact(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactApi->get_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of artifact to return | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

No authorization required

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
> ArtifactList get_artifact_list(result_id=result_id, page=page, page_size=page_size)

Get a (filtered) list of artifacts

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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    result_id = 'result_id_example' # str | The result ID to filter by (optional)
page = 56 # int | Set the page of items to return, defaults to 1 (optional)
page_size = 56 # int | Set the number of items per page, defaults to 25 (optional)

    try:
        # Get a (filtered) list of artifacts
        api_response = api_instance.get_artifact_list(result_id=result_id, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactApi->get_artifact_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| The result ID to filter by | [optional] 
 **page** | **int**| Set the page of items to return, defaults to 1 | [optional] 
 **page_size** | **int**| Set the number of items per page, defaults to 25 | [optional] 

### Return type

[**ArtifactList**](ArtifactList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of artifacts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_artifact**
> Artifact upload_artifact(result_id, filename, file, additional_metadata=additional_metadata)

Uploads a test run artifact

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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    result_id = 'result_id_example' # str | ID of result to attach artifact to
filename = 'filename_example' # str | ID of pet to update
file = '/path/to/file' # file | file to upload
additional_metadata = None # object | Additional data to pass to server (optional)

    try:
        # Uploads a test run artifact
        api_response = api_instance.upload_artifact(result_id, filename, file, additional_metadata=additional_metadata)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactApi->upload_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_id** | **str**| ID of result to attach artifact to | 
 **filename** | **str**| ID of pet to update | 
 **file** | **file**| file to upload | 
 **additional_metadata** | [**object**](object.md)| Additional data to pass to server | [optional] 

### Return type

[**Artifact**](Artifact.md)

### Authorization

No authorization required

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
> file view_artifact(id)

Stream an artifact directly to the client/browser

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
    api_instance = ibutsu_client.ArtifactApi(api_client)
    id = 'id_example' # str | ID of artifact to return

    try:
        # Stream an artifact directly to the client/browser
        api_response = api_instance.view_artifact(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactApi->view_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of artifact to return | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, image/jpeg, image/png, image/gif, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File contents |  -  |
**404** | Artifact not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

