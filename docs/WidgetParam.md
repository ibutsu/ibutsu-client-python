# WidgetParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the parameter to supply to the widget | [optional] 
**description** | **str** | A friendly description of the parameter | [optional] 
**type** | **str** | The type of parameter (string, integer, etc) | [optional] 

## Example

```python
from ibutsu_client.models.widget_param import WidgetParam

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetParam from a JSON string
widget_param_instance = WidgetParam.from_json(json)
# print the JSON string representation of the object
print(WidgetParam.to_json())

# convert the object into a dict
widget_param_dict = widget_param_instance.to_dict()
# create an instance of WidgetParam from a dict
widget_param_from_dict = WidgetParam.from_dict(widget_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


