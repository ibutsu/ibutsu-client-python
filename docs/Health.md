# Health


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the database, one of \&quot;OK\&quot;, \&quot;Error\&quot;, \&quot;Pending\&quot; | [optional] 
**message** | **str** | A message to explain the current status | [optional] 

## Example

```python
from ibutsu_client.models.health import Health

# TODO update the JSON string below
json = "{}"
# create an instance of Health from a JSON string
health_instance = Health.from_json(json)
# print the JSON string representation of the object
print(Health.to_json())

# convert the object into a dict
health_dict = health_instance.to_dict()
# create an instance of Health from a dict
health_from_dict = Health.from_dict(health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


