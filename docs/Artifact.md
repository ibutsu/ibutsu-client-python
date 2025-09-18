# Artifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the artifact | [optional] 
**result_id** | **str** | ID of test result to attach artifact to | [optional] 
**run_id** | **str** | ID of test run to attach artifact to | [optional] 
**filename** | **str** | name of the file | [optional] 
**additional_metadata** | **object** | Additional data to pass to server | [optional] 
**upload_date** | **str** | The date this artifact was uploaded | [optional] 

## Example

```python
from ibutsu_client.models.artifact import Artifact

# TODO update the JSON string below
json = "{}"
# create an instance of Artifact from a JSON string
artifact_instance = Artifact.from_json(json)
# print the JSON string representation of the object
print(Artifact.to_json())

# convert the object into a dict
artifact_dict = artifact_instance.to_dict()
# create an instance of Artifact from a dict
artifact_from_dict = Artifact.from_dict(artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


