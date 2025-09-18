# AccountRecovery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#39;s e-mail address | 

## Example

```python
from ibutsu_client.models.account_recovery import AccountRecovery

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRecovery from a JSON string
account_recovery_instance = AccountRecovery.from_json(json)
# print the JSON string representation of the object
print(AccountRecovery.to_json())

# convert the object into a dict
account_recovery_dict = account_recovery_instance.to_dict()
# create an instance of AccountRecovery from a dict
account_recovery_from_dict = AccountRecovery.from_dict(account_recovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


