# AccountRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#39;s e-mail address | 
**password** | **str** | The user&#39;s password | 

## Example

```python
from ibutsu_client.models.account_registration import AccountRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRegistration from a JSON string
account_registration_instance = AccountRegistration.from_json(json)
# print the JSON string representation of the object
print(AccountRegistration.to_json())

# convert the object into a dict
account_registration_dict = account_registration_instance.to_dict()
# create an instance of AccountRegistration from a dict
account_registration_from_dict = AccountRegistration.from_dict(account_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


