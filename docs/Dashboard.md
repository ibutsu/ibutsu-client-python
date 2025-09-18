# Dashboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the dashboard | [optional] 
**title** | **str** | The title of the dashboard | [optional] 
**description** | **str** | A basic description of the dashboard | [optional] 
**filters** | **str** | An optional set of filters | [optional] 
**project_id** | **str** | The ID of the project this dashboard is associated with | [optional] 
**user_id** | **str** | The ID of a user this dashboard might be associated with | [optional] 

## Example

```python
from ibutsu_client.models.dashboard import Dashboard

# TODO update the JSON string below
json = "{}"
# create an instance of Dashboard from a JSON string
dashboard_instance = Dashboard.from_json(json)
# print the JSON string representation of the object
print(Dashboard.to_json())

# convert the object into a dict
dashboard_dict = dashboard_instance.to_dict()
# create an instance of Dashboard from a dict
dashboard_from_dict = Dashboard.from_dict(dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


