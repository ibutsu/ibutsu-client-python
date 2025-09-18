# RunList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runs** | [**List[Run]**](Run.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from ibutsu_client.models.run_list import RunList

# TODO update the JSON string below
json = "{}"
# create an instance of RunList from a JSON string
run_list_instance = RunList.from_json(json)
# print the JSON string representation of the object
print(RunList.to_json())

# convert the object into a dict
run_list_dict = run_list_instance.to_dict()
# create an instance of RunList from a dict
run_list_from_dict = RunList.from_dict(run_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


