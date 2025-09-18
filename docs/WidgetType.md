# WidgetType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for this widget type | [optional] 
**title** | **str** | The title of the widget, for users to see | [optional] 
**description** | **str** | A helpful description of this widget type | [optional] 
**params** | [**List[WidgetParam]**](WidgetParam.md) | A dictionary or map of parameters to values | [optional] 
**type** | **str** | The type of widget (widget, view) | [optional] 

## Example

```python
from ibutsu_client.models.widget_type import WidgetType

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetType from a JSON string
widget_type_instance = WidgetType.from_json(json)
# print the JSON string representation of the object
print(WidgetType.to_json())

# convert the object into a dict
widget_type_dict = widget_type_instance.to_dict()
# create an instance of WidgetType from a dict
widget_type_from_dict = WidgetType.from_dict(widget_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


