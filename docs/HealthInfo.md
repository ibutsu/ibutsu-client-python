# HealthInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frontend** | **str** | The URL of the frontend | [optional] 
**backend** | **str** | The URL of the backend | [optional] 
**api_ui** | **str** | The URL to the UI for the API | [optional] 

## Example

```python
from ibutsu_client.models.health_info import HealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HealthInfo from a JSON string
health_info_instance = HealthInfo.from_json(json)
# print the JSON string representation of the object
print(HealthInfo.to_json())

# convert the object into a dict
health_info_dict = health_info_instance.to_dict()
# create an instance of HealthInfo from a dict
health_info_from_dict = HealthInfo.from_dict(health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


