# LoginSupport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **bool** | Flag to see if email/password login is available | [optional] 
**keycloak** | **bool** | Flag to see if Keycloak login is available | [optional] 
**google** | **bool** | Flag to see if Google login is available | [optional] 
**github** | **bool** | Flag to see if GitHub login is available | [optional] 
**facebook** | **bool** | Flag to see if Facebook login is available | [optional] 
**gitlab** | **bool** | Flag to see if GitLab login is available | [optional] 

## Example

```python
from ibutsu_client.models.login_support import LoginSupport

# TODO update the JSON string below
json = "{}"
# create an instance of LoginSupport from a JSON string
login_support_instance = LoginSupport.from_json(json)
# print the JSON string representation of the object
print(LoginSupport.to_json())

# convert the object into a dict
login_support_dict = login_support_instance.to_dict()
# create an instance of LoginSupport from a dict
login_support_from_dict = LoginSupport.from_dict(login_support_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


