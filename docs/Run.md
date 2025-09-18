# Run


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test run | [optional] 
**created** | **str** | The time this record was created | [optional] 
**duration** | **float** | Duration of tests in seconds | [optional] 
**source** | **str** | A source for this test run | [optional] 
**start_time** | **str** | The time the test run started | [optional] 
**component** | **str** | A component | [optional] 
**env** | **str** | The environment which is being tested | [optional] 
**project_id** | **str** | The project this run is associated with | [optional] 
**summary** | **object** | A summary of the test results | [optional] 
**metadata** | **object** | Extra metadata for this run | [optional] 

## Example

```python
from ibutsu_client.models.run import Run

# TODO update the JSON string below
json = "{}"
# create an instance of Run from a JSON string
run_instance = Run.from_json(json)
# print the JSON string representation of the object
print(Run.to_json())

# convert the object into a dict
run_dict = run_instance.to_dict()
# create an instance of Run from a dict
run_from_dict = Run.from_dict(run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


