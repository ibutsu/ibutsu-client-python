"""Tests for DashboardApi."""

from urllib.parse import parse_qs, urlparse
from uuid import uuid4

import pytest

from ibutsu_client.api.dashboard_api import DashboardApi
from ibutsu_client.models.dashboard import Dashboard
from ibutsu_client.models.dashboard_list import DashboardList


class TestDashboardApi:
    """DashboardApi Tests"""

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "DASHBOARD_ID_PLACEHOLDER",
                    "title": "New Dashboard",
                    "description": "Description",
                },
                "status": 201,
            }
        ],
        indirect=True,
    )
    def test_add_dashboard(self, mock_api_client, create_mock_response):
        """Test case for add_dashboard"""
        api = DashboardApi(api_client=mock_api_client)
        dashboard_id = uuid4()

        # Update the mock response with the actual dashboard_id
        create_mock_response.data = create_mock_response.data.replace(
            b"DASHBOARD_ID_PLACEHOLDER", str(dashboard_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

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

    @pytest.mark.parametrize(
        "create_mock_response",
        [{"data": {}, "status": 200}],
        indirect=True,
    )
    def test_delete_dashboard(self, mock_api_client, create_mock_response):
        """Test case for delete_dashboard"""
        api = DashboardApi(api_client=mock_api_client)
        dashboard_id = uuid4()

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        api.delete_dashboard(id=dashboard_id)

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "DELETE"
        assert args[1].endswith(f"/dashboard/{dashboard_id}")

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "DASHBOARD_ID_PLACEHOLDER",
                    "title": "My Dashboard",
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_get_dashboard(self, mock_api_client, create_mock_response):
        """Test case for get_dashboard"""
        api = DashboardApi(api_client=mock_api_client)
        dashboard_id = uuid4()

        # Update the mock response with the actual dashboard_id
        create_mock_response.data = create_mock_response.data.replace(
            b"DASHBOARD_ID_PLACEHOLDER", str(dashboard_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

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

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "dashboards": [
                        {"id": "00000000-0000-0000-0000-000000000001", "title": "Dashboard 1"},
                        {"id": "00000000-0000-0000-0000-000000000002", "title": "Dashboard 2"},
                    ],
                    "pagination": {"page": 1, "pageSize": 25, "totalItems": 2, "totalPages": 1},
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_get_dashboard_list(self, mock_api_client, create_mock_response):
        """Test case for get_dashboard_list"""
        api = DashboardApi(api_client=mock_api_client)

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

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

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "DASHBOARD_ID_PLACEHOLDER",
                    "title": "Updated Dashboard",
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_update_dashboard(self, mock_api_client, create_mock_response):
        """Test case for update_dashboard"""
        api = DashboardApi(api_client=mock_api_client)
        dashboard_id = uuid4()

        # Update the mock response with the actual dashboard_id
        create_mock_response.data = create_mock_response.data.replace(
            b"DASHBOARD_ID_PLACEHOLDER", str(dashboard_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

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
