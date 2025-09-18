# ResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Result]**](Result.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from ibutsu_client.models.result_list import ResultList

# TODO update the JSON string below
json = "{}"
# create an instance of ResultList from a JSON string
result_list_instance = ResultList.from_json(json)
# print the JSON string representation of the object
print(ResultList.to_json())

# convert the object into a dict
result_list_dict = result_list_instance.to_dict()
# create an instance of ResultList from a dict
result_list_from_dict = ResultList.from_dict(result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


