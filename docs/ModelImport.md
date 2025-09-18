# ModelImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The database ID of the import | [optional] 
**status** | **str** | The current status of the import, can be one of \&quot;pending\&quot;, \&quot;running\&quot;, \&quot;done\&quot; | [optional] 
**filename** | **str** | The name of the file that was uploaded | [optional] 
**format** | **str** | The format of the file uploaded | [optional] 
**run_id** | **str** | The ID of the run from the import | [optional] 

## Example

```python
from ibutsu_client.models.model_import import ModelImport

# TODO update the JSON string below
json = "{}"
# create an instance of ModelImport from a JSON string
model_import_instance = ModelImport.from_json(json)
# print the JSON string representation of the object
print(ModelImport.to_json())

# convert the object into a dict
model_import_dict = model_import_instance.to_dict()
# create an instance of ModelImport from a dict
model_import_from_dict = ModelImport.from_dict(model_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


