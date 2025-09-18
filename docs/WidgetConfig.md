# WidgetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The internal ID of the WidgetConfig | [optional] 
**type** | **str** | The type of widget, one of either \&quot;widget\&quot; or \&quot;view\&quot; | [optional] 
**widget** | **str** | The widget to render, from the list at /widget/types | [optional] 
**project_id** | **str** | The project ID for which the widget is designed | [optional] 
**weight** | **int** | The weighting for the widget, lower weight means it will display first | [optional] 
**params** | **object** | A dictionary of parameters to send to the widget | [optional] 
**title** | **str** | The title shown on the widget or page | [optional] 

## Example

```python
from ibutsu_client.models.widget_config import WidgetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetConfig from a JSON string
widget_config_instance = WidgetConfig.from_json(json)
# print the JSON string representation of the object
print(WidgetConfig.to_json())

# convert the object into a dict
widget_config_dict = widget_config_instance.to_dict()
# create an instance of WidgetConfig from a dict
widget_config_from_dict = WidgetConfig.from_dict(widget_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


