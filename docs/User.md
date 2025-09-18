# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the user | [optional] 
**email** | **str** | The user&#39;s e-mail address | 
**name** | **str** | The user&#39;s name | [optional] 
**is_superadmin** | **bool** | Flag to show if a user is a super-admin | [optional] 
**is_active** | **bool** | Flag to show if the user is active | [optional] 
**group_id** | **str** | The ID of the group of this project | [optional] 

## Example

```python
from ibutsu_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


