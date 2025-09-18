# WidgetConfigList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widgets** | [**List[WidgetConfig]**](WidgetConfig.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from ibutsu_client.models.widget_config_list import WidgetConfigList

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetConfigList from a JSON string
widget_config_list_instance = WidgetConfigList.from_json(json)
# print the JSON string representation of the object
print(WidgetConfigList.to_json())

# convert the object into a dict
widget_config_list_dict = widget_config_list_instance.to_dict()
# create an instance of WidgetConfigList from a dict
widget_config_list_from_dict = WidgetConfigList.from_dict(widget_config_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


