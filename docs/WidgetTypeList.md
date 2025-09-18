# WidgetTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[WidgetType]**](WidgetType.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from ibutsu_client.models.widget_type_list import WidgetTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetTypeList from a JSON string
widget_type_list_instance = WidgetTypeList.from_json(json)
# print the JSON string representation of the object
print(WidgetTypeList.to_json())

# convert the object into a dict
widget_type_list_dict = widget_type_list_instance.to_dict()
# create an instance of WidgetTypeList from a dict
widget_type_list_from_dict = WidgetTypeList.from_dict(widget_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


