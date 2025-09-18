# DashboardList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboards** | [**List[Dashboard]**](Dashboard.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from ibutsu_client.models.dashboard_list import DashboardList

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardList from a JSON string
dashboard_list_instance = DashboardList.from_json(json)
# print the JSON string representation of the object
print(DashboardList.to_json())

# convert the object into a dict
dashboard_list_dict = dashboard_list_instance.to_dict()
# create an instance of DashboardList from a dict
dashboard_list_from_dict = DashboardList.from_dict(dashboard_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


