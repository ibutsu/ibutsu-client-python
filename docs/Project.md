# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the project | [optional] 
**name** | **str** | The machine name of the project | [optional] 
**title** | **str** | The human-readable title of the project | [optional] 
**owner_id** | **str** | The ID of the owner of this project | [optional] 
**group_id** | **str** | The ID of the group of this project | [optional] 

## Example

```python
from ibutsu_client.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


