# Result


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test result | [optional] 
**test_id** | **str** | Unique id | [optional] 
**start_time** | **str** | Timestamp of starttime. | [optional] 
**duration** | **float** | Duration of test in seconds. | [optional] 
**result** | **str** | Status of result. | [optional] 
**component** | **str** | A component | [optional] 
**env** | **str** | The environment which is being tested | [optional] 
**run_id** | **str** | The run this result is associated with | [optional] 
**project_id** | **str** | The project this run is associated with | [optional] 
**metadata** | **object** |  | [optional] 
**params** | **object** |  | [optional] 
**source** | **str** | Where the data came from (useful for filtering) | [optional] 

## Example

```python
from ibutsu_client.models.result import Result

# TODO update the JSON string below
json = "{}"
# create an instance of Result from a JSON string
result_instance = Result.from_json(json)
# print the JSON string representation of the object
print(Result.to_json())

# convert the object into a dict
result_dict = result_instance.to_dict()
# create an instance of Result from a dict
result_from_dict = Result.from_dict(result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


