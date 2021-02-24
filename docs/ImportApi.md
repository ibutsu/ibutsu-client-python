# ibutsu_client.ImportApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_import**](ImportApi.md#add_import) | **POST** /import | Import a file into Ibutsu. This can be either a JUnit XML file, or an Ibutsu archive
[**get_import**](ImportApi.md#get_import) | **GET** /import/{id} | Get the status of an import


# **add_import**
> ModelImport add_import(import_file)

Import a file into Ibutsu. This can be either a JUnit XML file, or an Ibutsu archive

### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import import_api
from ibutsu_client.model.model_import import ModelImport
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = import_api.ImportApi(api_client)
    import_file = open('/path/to/file', 'rb') # file_type | The file to import
    project = "project_example" # str | The project associated with this import (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import a file into Ibutsu. This can be either a JUnit XML file, or an Ibutsu archive
        api_response = api_instance.add_import(import_file)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ImportApi->add_import: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import a file into Ibutsu. This can be either a JUnit XML file, or an Ibutsu archive
        api_response = api_instance.add_import(import_file, project=project)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ImportApi->add_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_file** | **file_type**| The file to import |
 **project** | **str**| The project associated with this import | [optional]

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

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

```python
import time
import ibutsu_client
from ibutsu_client.api import import_api
from ibutsu_client.model.model_import import ModelImport
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = import_api.ImportApi(api_client)
    id = "id_example" # str | The ID of the import

    # example passing only required values which don't have defaults set
    try:
        # Get the status of an import
        api_response = api_instance.get_import(id)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling ImportApi->get_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the import |

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

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

