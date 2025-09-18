# LoginConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The client ID for the provider | [optional] 
**redirect_uri** | **str** | The redirect URI for the provider to call back | [optional] 
**scope** | **str** | The OAuth2 permission scope | [optional] 

## Example

```python
from ibutsu_client.models.login_config import LoginConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LoginConfig from a JSON string
login_config_instance = LoginConfig.from_json(json)
# print the JSON string representation of the object
print(LoginConfig.to_json())

# convert the object into a dict
login_config_dict = login_config_instance.to_dict()
# create an instance of LoginConfig from a dict
login_config_from_dict = LoginConfig.from_dict(login_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


