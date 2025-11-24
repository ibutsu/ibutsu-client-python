"""Tests for DashboardApi."""

from urllib.parse import parse_qs, urlparse
from uuid import uuid4

from ibutsu_client.api.dashboard_api import DashboardApi
from ibutsu_client.models.dashboard import Dashboard
from ibutsu_client.models.dashboard_list import DashboardList


class TestDashboardApi:
    """DashboardApi Tests"""

    def test_add_dashboard(self, mock_api_client, mock_rest_response):
        """Test case for add_dashboard"""
        api = DashboardApi(api_client=mock_api_client)
        dashboard_id = uuid4()
        dashboard_data = {
            "id": str(dashboard_id),
            "title": "New Dashboard",
            "description": "Description",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=dashboard_data, status=201)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        new_dashboard = Dashboard(title="New Dashboard", description="Description")
        response = api.add_dashboard(dashboard=new_dashboard)

        # Verify result
        assert isinstance(response, Dashboard)
        assert str(response.id) == str(dashboard_id)
        assert response.title == "New Dashboard"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "POST"
        assert args[1].endswith("/dashboard")

    def test_delete_dashboard(self, mock_api_client, mock_rest_response):
        """Test case for delete_dashboard"""
        api = DashboardApi(api_client=mock_api_client)
        dashboard_id = uuid4()

        # Mock the API response
        mock_response = mock_rest_response(status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        api.delete_dashboard(id=dashboard_id)

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "DELETE"
        assert args[1].endswith(f"/dashboard/{dashboard_id}")

    def test_get_dashboard(self, mock_api_client, mock_rest_response):
        """Test case for get_dashboard"""
        api = DashboardApi(api_client=mock_api_client)
        dashboard_id = uuid4()
        dashboard_data = {
            "id": str(dashboard_id),
            "title": "My Dashboard",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=dashboard_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        response = api.get_dashboard(id=dashboard_id)

        # Verify result
        assert isinstance(response, Dashboard)
        assert str(response.id) == str(dashboard_id)
        assert response.title == "My Dashboard"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert args[1].endswith(f"/dashboard/{dashboard_id}")

    def test_get_dashboard_list(self, mock_api_client, mock_rest_response):
        """Test case for get_dashboard_list"""
        api = DashboardApi(api_client=mock_api_client)

        dashboard_list_data = {
            "dashboards": [
                {"id": str(uuid4()), "title": "Dashboard 1"},
                {"id": str(uuid4()), "title": "Dashboard 2"},
            ],
            "pagination": {"page": 1, "pageSize": 25, "totalItems": 2, "totalPages": 1},
        }

        # Mock the API response
        mock_response = mock_rest_response(data=dashboard_list_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        response = api.get_dashboard_list(page=1, page_size=25)

        # Verify result
        assert isinstance(response, DashboardList)
        assert len(response.dashboards) == 2
        assert response.dashboards[0].title == "Dashboard 1"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"

        parsed_url = urlparse(args[1])
        assert parsed_url.path.endswith("/dashboard")
        query_params = parse_qs(parsed_url.query)

        assert query_params["page"] == ["1"]
        assert query_params["pageSize"] == ["25"]

    def test_update_dashboard(self, mock_api_client, mock_rest_response):
        """Test case for update_dashboard"""
        api = DashboardApi(api_client=mock_api_client)
        dashboard_id = uuid4()
        dashboard_data = {
            "id": str(dashboard_id),
            "title": "Updated Dashboard",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=dashboard_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        update_dashboard = Dashboard(title="Updated Dashboard")
        response = api.update_dashboard(id=dashboard_id, dashboard=update_dashboard)

        # Verify result
        assert isinstance(response, Dashboard)
        assert str(response.id) == str(dashboard_id)
        assert response.title == "Updated Dashboard"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "PUT"
        assert args[1].endswith(f"/dashboard/{dashboard_id}")
