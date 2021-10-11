# ibutsu_client.LoginApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](LoginApi.md#activate) | **POST** /login/activate/{activation_code} | 
[**auth**](LoginApi.md#auth) | **GET** /login/auth/{provider} | 
[**config**](LoginApi.md#config) | **GET** /login/config/{provider} | 
[**login**](LoginApi.md#login) | **POST** /login | 
[**recover**](LoginApi.md#recover) | **POST** /login/recover | 
[**register**](LoginApi.md#register) | **POST** /login/register | 
[**reset_password**](LoginApi.md#reset_password) | **POST** /login/reset-password | 
[**support**](LoginApi.md#support) | **GET** /login/support | 


# **activate**
> activate(activation_code)



### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import login_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    activation_code = "activation_code_example" # str | The activation code

    # example passing only required values which don't have defaults set
    try:
        api_instance.activate(activation_code)
    except ibutsu_client.ApiException as e:
        print("Exception when calling LoginApi->activate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_code** | **str**| The activation code |

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
**302** | Redirect the user to the login page |  -  |
**404** | The activation code was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth**
> auth(provider)



### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import login_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    provider = "provider_example" # str | The login provider's configuration

    # example passing only required values which don't have defaults set
    try:
        api_instance.auth(provider)
    except ibutsu_client.ApiException as e:
        print("Exception when calling LoginApi->auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The login provider&#39;s configuration |

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
**200** | Successful auth |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config**
> LoginConfig config(provider)



### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import login_api
from ibutsu_client.model.login_config import LoginConfig
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    provider = "provider_example" # str | The login provider's configuration

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.config(provider)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling LoginApi->config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The login provider&#39;s configuration |

### Return type

[**LoginConfig**](LoginConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of the login types supported by the backend |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> LoginToken login()



### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import login_api
from ibutsu_client.model.login_token import LoginToken
from ibutsu_client.model.login_error import LoginError
from ibutsu_client.model.unknownbasetype import UNKNOWNBASETYPE
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    unknown_base_type = {
        email="me@example.com",
        password="mysupersecretpassword",
    } # UNKNOWN_BASE_TYPE | A login object (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.login(unknown_base_type=unknown_base_type)
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling LoginApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| A login object | [optional]

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user was authenticated |  -  |
**401** | There was an error when the user tried to log in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover**
> recover()



### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import login_api
from ibutsu_client.model.account_recovery import AccountRecovery
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    account_recovery = AccountRecovery(
        email="user@domain.com",
    ) # AccountRecovery | A user recovering their password (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.recover(account_recovery=account_recovery)
    except ibutsu_client.ApiException as e:
        print("Exception when calling LoginApi->recover: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_recovery** | [**AccountRecovery**](AccountRecovery.md)| A user recovering their password | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An e-mail was sent to the user |  -  |
**400** | There was an error when the user tried to recover their account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> register()



### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import login_api
from ibutsu_client.model.login_error import LoginError
from ibutsu_client.model.account_registration import AccountRegistration
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    account_registration = AccountRegistration(
        email="user@domain.com",
        password="supersecretpassword",
    ) # AccountRegistration | A user registering their account (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.register(account_registration=account_registration)
    except ibutsu_client.ApiException as e:
        print("Exception when calling LoginApi->register: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_registration** | [**AccountRegistration**](AccountRegistration.md)| A user registering their account | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The user was registered |  -  |
**401** | There was an error when the user tried to log in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password()



### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import login_api
from ibutsu_client.model.account_reset import AccountReset
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    account_reset = AccountReset(
        activation_code="YjdmYWFkMTItNzkxZC00MjE4LTgwZGItOWFlOWM2Y2RhOTM5",
        password="supersecretpassword",
    ) # AccountReset | A user resetting their password (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.reset_password(account_reset=account_reset)
    except ibutsu_client.ApiException as e:
        print("Exception when calling LoginApi->reset_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_reset** | [**AccountReset**](AccountReset.md)| A user resetting their password | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The user&#39;s password was reset |  -  |
**400** | There was an error when the user tried to reset their password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} support()



### Example

```python
import time
import ibutsu_client
from ibutsu_client.api import login_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "http://localhost/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.support()
        pprint(api_response)
    except ibutsu_client.ApiException as e:
        print("Exception when calling LoginApi->support: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of the login types supported by the backend |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

