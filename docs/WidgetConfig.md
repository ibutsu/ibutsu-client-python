# WidgetConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The internal ID of the WidgetConfig | [optional] 
**type** | **str** | The type of widget, one of either \&quot;widget\&quot; or \&quot;view\&quot; | [optional] 
**widget** | **str** | The widget to render, from the list at /widget/types | [optional] 
**project_id** | **str** | The project ID for which the widget is designed | [optional] 
**weight** | **int** | The weighting for the widget, lower weight means it will display first | [optional] 
**params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A dictionary of parameters to send to the widget | [optional] 
**title** | **str** | The title shown on the widget or page | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


