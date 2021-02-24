# ibutsu_client.HealthApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_database_health**](HealthApi.md#get_database_health) | **GET** /health/database | Get a health report for the database
[**get_health**](HealthApi.md#get_health) | **GET** /health | Get a general health report
[**get_health_info**](HealthApi.md#get_health_info) | **GET** /health/info | Get information about the server


# **get_database_health**
> Health get_database_health()

Get a health report for the database

### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import health_api
from ibutsu_client.model.health import Health
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a health report for the database
        api_response = api_instance.get_database_health()
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling HealthApi->get_database_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A health report |  -  |
**500** | A health report with an error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health**
> Health get_health()

Get a general health report

### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import health_api
from ibutsu_client.model.health import Health
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a general health report
        api_response = api_instance.get_health()
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling HealthApi->get_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A health report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_info**
> HealthInfo get_health_info()

Get information about the server

### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import health_api
from ibutsu_client.model.health_info import HealthInfo
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get information about the server
        api_response = api_instance.get_health_info()
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling HealthApi->get_health_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthInfo**](HealthInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Some information about the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

