# ReportParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of report to generate | 
**filter** | **str** | A regular expression to filter test results by | [optional] 
**source** | **str** | The source of the test results | [optional] 

## Example

```python
from ibutsu_client.models.report_parameters import ReportParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ReportParameters from a JSON string
report_parameters_instance = ReportParameters.from_json(json)
# print the JSON string representation of the object
print(ReportParameters.to_json())

# convert the object into a dict
report_parameters_dict = report_parameters_instance.to_dict()
# create an instance of ReportParameters from a dict
report_parameters_from_dict = ReportParameters.from_dict(report_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


