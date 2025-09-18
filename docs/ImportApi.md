# ibutsu_client.ImportApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_import**](ImportApi.md#add_import) | **POST** /import | Import a file into Ibutsu. This can be either a JUnit XML file, or an Ibutsu archive
[**get_import**](ImportApi.md#get_import) | **GET** /import/{id} | Get the status of an import


# **add_import**
> ModelImport add_import(import_file, project=project, metadata=metadata, source=source)

Import a file into Ibutsu. This can be either a JUnit XML file, or an Ibutsu archive

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.model_import import ModelImport
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
    api_instance = ibutsu_client.ImportApi(api_client)
    import_file = None # bytearray | The file to import
    project = 'project_example' # str | The project associated with this import (optional)
    metadata = None # object | Additional metadata about imported run (optional)
    source = 'source_example' # str | The source of this import (optional)

    try:
        # Import a file into Ibutsu. This can be either a JUnit XML file, or an Ibutsu archive
        api_response = api_instance.add_import(import_file, project=project, metadata=metadata, source=source)
        print("The response of ImportApi->add_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->add_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_file** | **bytearray**| The file to import | 
 **project** | **str**| The project associated with this import | [optional] 
 **metadata** | [**object**](object.md)| Additional metadata about imported run | [optional] 
 **source** | **str**| The source of this import | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The file has been queued for importing |  -  |
**400** | Bad Request |  -  |
**415** | Unsupported Media Type. This file cannot be imported |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import**
> ModelImport get_import(id)

Get the status of an import

### Example

* Bearer (JWT) Authentication (jwt):

```python
import ibutsu_client
from ibutsu_client.models.model_import import ModelImport
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
    api_instance = ibutsu_client.ImportApi(api_client)
    id = 'id_example' # str | The ID of the import

    try:
        # Get the status of an import
        api_response = api_instance.get_import(id)
        print("The response of ImportApi->get_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->get_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the import | 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file has successfully been imported |  -  |
**202** | The file is currently being imported |  -  |
**404** | The import does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

