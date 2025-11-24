"""Tests for RunApi."""

from urllib.parse import parse_qs, urlparse
from uuid import uuid4

from ibutsu_client.api.run_api import RunApi
from ibutsu_client.models.run import Run
from ibutsu_client.models.run_list import RunList
from ibutsu_client.models.update_run import UpdateRun


class TestRunApi:
    """RunApi Tests"""

    def test_add_run(self, mock_api_client, mock_rest_response):
        """Test case for add_run"""
        api = RunApi(api_client=mock_api_client)
        run_id = uuid4()
        run_data = {
            "id": str(run_id),
            "component": "test-component",
            "env": "ci",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=run_data, status=201)
        mock_api_client.call_api.return_value = mock_response

        # Create run object to send
        run_item = Run(component="test-component", env="ci")

        # Call the API
        response = api.add_run(run=run_item)

        # Verify the response is deserialized correctly
        assert isinstance(response, Run)
        assert str(response.id) == str(run_id)
        assert response.component == "test-component"

        # Verify call_api was called with correct arguments
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "POST"  # method
        assert args[1].endswith("/run")  # url

        # Body is serialized to dict
        assert isinstance(args[3], dict)
        assert args[3]["component"] == "test-component"
        assert args[3]["env"] == "ci"

    def test_get_run(self, mock_api_client, mock_rest_response):
        """Test case for get_run"""
        api = RunApi(api_client=mock_api_client)
        run_id = uuid4()
        run_data = {
            "id": str(run_id),
            "component": "test-component",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=run_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        response = api.get_run(id=run_id)

        # Verify result
        assert isinstance(response, Run)
        assert str(response.id) == str(run_id)
        assert response.component == "test-component"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert args[1].endswith(f"/run/{run_id}")

    def test_get_run_list(self, mock_api_client, mock_rest_response):
        """Test case for get_run_list"""
        api = RunApi(api_client=mock_api_client)

        run_list_data = {
            "runs": [
                {"id": str(uuid4()), "component": "comp1"},
                {"id": str(uuid4()), "component": "comp2"},
            ],
            "pagination": {"page": 1, "pageSize": 25, "totalItems": 2, "totalPages": 1},
        }

        # Mock the API response
        mock_response = mock_rest_response(data=run_list_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        response = api.get_run_list(page=1, page_size=25, filter=["env=ci"])

        # Verify result
        assert isinstance(response, RunList)
        assert len(response.runs) == 2
        assert response.runs[0].component == "comp1"
        assert response.pagination.total_items == 2

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "GET"

        parsed_url = urlparse(args[1])
        assert parsed_url.path.endswith("/run")
        query_params = parse_qs(parsed_url.query)

        assert query_params["page"] == ["1"]
        assert query_params["pageSize"] == ["25"]
        assert query_params["filter"] == ["env=ci"]

    def test_update_run(self, mock_api_client, mock_rest_response):
        """Test case for update_run"""
        api = RunApi(api_client=mock_api_client)
        run_id = uuid4()
        run_data = {
            "id": str(run_id),
            "component": "updated-component",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=run_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Update object
        run_update = Run(component="updated-component")

        # Call the API
        response = api.update_run(id=run_id, run=run_update)

        # Verify result
        assert isinstance(response, Run)
        assert str(response.id) == str(run_id)
        assert response.component == "updated-component"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "PUT"
        assert args[1].endswith(f"/run/{run_id}")

        # Body is serialized
        assert isinstance(args[3], dict)
        assert args[3]["component"] == "updated-component"

    def test_bulk_update(self, mock_api_client, mock_rest_response):
        """Test case for bulk_update"""
        api = RunApi(api_client=mock_api_client)

        run_list_data = {
            "runs": [
                {"id": str(uuid4()), "component": "comp1", "metadata": {"new": "val"}},
                {"id": str(uuid4()), "component": "comp2", "metadata": {"new": "val"}},
            ],
            "pagination": {"page": 1, "pageSize": 25, "totalItems": 2, "totalPages": 1},
        }

        # Mock the API response
        mock_response = mock_rest_response(data=run_list_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Update object
        update_data = UpdateRun(metadata={"new": "val"})

        # Call API
        response = api.bulk_update(filter=["env=ci"], update_run=update_data)

        # Verify result
        assert isinstance(response, RunList)
        assert len(response.runs) == 2

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "POST"

        parsed_url = urlparse(args[1])
        assert parsed_url.path.endswith("/runs/bulk-update")
        query_params = parse_qs(parsed_url.query)
        assert query_params["filter"] == ["env=ci"]

        assert isinstance(args[3], dict)
        assert args[3]["metadata"] == {"new": "val"}
