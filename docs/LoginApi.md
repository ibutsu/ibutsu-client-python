# ibutsu_client.LoginApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](LoginApi.md#activate) | **GET** /login/activate/{activation_code} | 
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
import ibutsu_client
from ibutsu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.LoginApi(api_client)
    activation_code = 'activation_code_example' # str | The activation code

    try:
        api_instance.activate(activation_code)
    except Exception as e:
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
import ibutsu_client
from ibutsu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.LoginApi(api_client)
    provider = 'provider_example' # str | The login provider's configuration

    try:
        api_instance.auth(provider)
    except Exception as e:
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
import ibutsu_client
from ibutsu_client.models.login_config import LoginConfig
from ibutsu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.LoginApi(api_client)
    provider = 'provider_example' # str | The login provider's configuration

    try:
        api_response = api_instance.config(provider)
        print("The response of LoginApi->config:\n")
        pprint(api_response)
    except Exception as e:
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
> LoginToken login(credentials=credentials)

### Example


```python
import ibutsu_client
from ibutsu_client.models.credentials import Credentials
from ibutsu_client.models.login_token import LoginToken
from ibutsu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.LoginApi(api_client)
    credentials = ibutsu_client.Credentials() # Credentials | A login object (optional)

    try:
        api_response = api_instance.login(credentials=credentials)
        print("The response of LoginApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**Credentials**](Credentials.md)| A login object | [optional] 

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
> recover(account_recovery=account_recovery)

### Example


```python
import ibutsu_client
from ibutsu_client.models.account_recovery import AccountRecovery
from ibutsu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.LoginApi(api_client)
    account_recovery = ibutsu_client.AccountRecovery() # AccountRecovery | A user recovering their password (optional)

    try:
        api_instance.recover(account_recovery=account_recovery)
    except Exception as e:
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
> register(account_registration=account_registration)

### Example


```python
import ibutsu_client
from ibutsu_client.models.account_registration import AccountRegistration
from ibutsu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.LoginApi(api_client)
    account_registration = ibutsu_client.AccountRegistration() # AccountRegistration | A user registering their account (optional)

    try:
        api_instance.register(account_registration=account_registration)
    except Exception as e:
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
> reset_password(account_reset=account_reset)

### Example


```python
import ibutsu_client
from ibutsu_client.models.account_reset import AccountReset
from ibutsu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.LoginApi(api_client)
    account_reset = ibutsu_client.AccountReset() # AccountReset | A user resetting their password (optional)

    try:
        api_instance.reset_password(account_reset=account_reset)
    except Exception as e:
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
> LoginSupport support()

### Example


```python
import ibutsu_client
from ibutsu_client.models.login_support import LoginSupport
from ibutsu_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = ibutsu_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with ibutsu_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibutsu_client.LoginApi(api_client)

    try:
        api_response = api_instance.support()
        print("The response of LoginApi->support:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->support: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginSupport**](LoginSupport.md)

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

