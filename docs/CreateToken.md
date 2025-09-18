# CreateToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name given to this token | 
**expires** | **str** | The date and time when this token expires | 

## Example

```python
from ibutsu_client.models.create_token import CreateToken

# TODO update the JSON string below
json = "{}"
# create an instance of CreateToken from a JSON string
create_token_instance = CreateToken.from_json(json)
# print the JSON string representation of the object
print(CreateToken.to_json())

# convert the object into a dict
create_token_dict = create_token_instance.to_dict()
# create an instance of CreateToken from a dict
create_token_from_dict = CreateToken.from_dict(create_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


