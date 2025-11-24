"""Tests for ResultApi."""

from urllib.parse import parse_qs, urlparse
from uuid import uuid4

from ibutsu_client.api.result_api import ResultApi
from ibutsu_client.models.result import Result
from ibutsu_client.models.result_list import ResultList


class TestResultApi:
    """ResultApi Tests"""

    def test_add_result(self, mock_api_client, mock_rest_response):
        """Test case for add_result"""
        api = ResultApi(api_client=mock_api_client)
        result_id = uuid4()
        result_data = {
            "id": str(result_id),
            "test_id": "test_case_1",
            "result": "passed",
            "duration": 1.5,
        }

        # Mock the API response
        mock_response = mock_rest_response(data=result_data, status=201)
        mock_api_client.call_api.return_value = mock_response

        # Create result object to send
        result_item = Result(test_id="test_case_1", result="passed", duration=1.5)

        # Call the API
        response = api.add_result(result=result_item)

        # Verify the response is deserialized correctly
        assert isinstance(response, Result)
        assert str(response.id) == str(result_id)
        assert response.test_id == "test_case_1"
        assert response.result == "passed"

        # Verify call_api was called with correct arguments
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "POST"  # method
        assert args[1].endswith("/result")  # url

        # Body is serialized to dict
        assert isinstance(args[3], dict)
        assert args[3]["test_id"] == "test_case_1"
        assert args[3]["result"] == "passed"
        assert args[3]["duration"] == 1.5

    def test_get_result(self, mock_api_client, mock_rest_response):
        """Test case for get_result"""
        api = ResultApi(api_client=mock_api_client)
        result_id = uuid4()
        result_data = {
            "id": str(result_id),
            "test_id": "test_case_1",
            "result": "passed",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=result_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        response = api.get_result(id=result_id)

        # Verify result
        assert isinstance(response, Result)
        assert str(response.id) == str(result_id)
        assert response.test_id == "test_case_1"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert args[1].endswith(f"/result/{result_id}")

    def test_get_result_list(self, mock_api_client, mock_rest_response):
        """Test case for get_result_list"""
        api = ResultApi(api_client=mock_api_client)

        result_list_data = {
            "results": [
                {"id": str(uuid4()), "test_id": "test_1", "result": "passed"},
                {"id": str(uuid4()), "test_id": "test_2", "result": "failed"},
            ],
            "pagination": {"page": 1, "pageSize": 25, "totalItems": 2, "totalPages": 1},
        }

        # Mock the API response
        mock_response = mock_rest_response(data=result_list_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        response = api.get_result_list(page=1, page_size=25, filter=["result=passed"])

        # Verify result
        assert isinstance(response, ResultList)
        assert len(response.results) == 2
        assert response.results[0].test_id == "test_1"
        assert response.pagination.total_items == 2

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "GET"

        parsed_url = urlparse(args[1])
        assert parsed_url.path.endswith("/result")
        query_params = parse_qs(parsed_url.query)

        assert query_params["page"] == ["1"]
        assert query_params["pageSize"] == ["25"]
        assert query_params["filter"] == ["result=passed"]

    def test_update_result(self, mock_api_client, mock_rest_response):
        """Test case for update_result"""
        api = ResultApi(api_client=mock_api_client)
        result_id = uuid4()
        result_data = {
            "id": str(result_id),
            "test_id": "test_case_1",
            "result": "failed",  # Updated result
        }

        # Mock the API response
        mock_response = mock_rest_response(data=result_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Update object
        result_update = Result(result="failed")

        # Call the API
        response = api.update_result(id=result_id, result=result_update)

        # Verify result
        assert isinstance(response, Result)
        assert str(response.id) == str(result_id)
        assert response.result == "failed"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "PUT"
        assert args[1].endswith(f"/result/{result_id}")

        # Body is serialized
        assert isinstance(args[3], dict)
        assert args[3]["result"] == "failed"
