"""Tests for AdminProjectManagementApi."""

from urllib.parse import parse_qs, urlparse
from uuid import uuid4

from ibutsu_client.api.admin_project_management_api import AdminProjectManagementApi
from ibutsu_client.models.project import Project
from ibutsu_client.models.project_list import ProjectList


class TestAdminProjectManagementApi:
    """AdminProjectManagementApi Tests"""

    def test_admin_add_project(self, mock_api_client, mock_rest_response):
        """Test case for admin_add_project"""
        api = AdminProjectManagementApi(api_client=mock_api_client)
        project_id = uuid4()
        project_data = {
            "id": str(project_id),
            "name": "New Project",
            "title": "New Project Title",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=project_data, status=201)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        new_project = Project(name="New Project", title="New Project Title")
        response = api.admin_add_project(project=new_project)

        # Verify result
        assert isinstance(response, Project)
        assert str(response.id) == str(project_id)
        assert response.name == "New Project"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "POST"
        assert args[1].endswith("/admin/project")

    def test_admin_delete_project(self, mock_api_client, mock_rest_response):
        """Test case for admin_delete_project"""
        api = AdminProjectManagementApi(api_client=mock_api_client)
        project_id = uuid4()

        # Mock the API response
        mock_response = mock_rest_response(status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        api.admin_delete_project(id=project_id)

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "DELETE"
        assert args[1].endswith(f"/admin/project/{project_id}")

    def test_admin_get_project(self, mock_api_client, mock_rest_response):
        """Test case for admin_get_project"""
        api = AdminProjectManagementApi(api_client=mock_api_client)
        project_id = uuid4()
        project_data = {
            "id": str(project_id),
            "name": "My Project",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=project_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        response = api.admin_get_project(id=project_id)

        # Verify result
        assert isinstance(response, Project)
        assert str(response.id) == str(project_id)
        assert response.name == "My Project"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert args[1].endswith(f"/admin/project/{project_id}")

    def test_admin_get_project_list(self, mock_api_client, mock_rest_response):
        """Test case for admin_get_project_list"""
        api = AdminProjectManagementApi(api_client=mock_api_client)

        project_list_data = {
            "projects": [
                {"id": str(uuid4()), "name": "Project 1"},
                {"id": str(uuid4()), "name": "Project 2"},
            ],
            "pagination": {"page": 1, "pageSize": 25, "totalItems": 2, "totalPages": 1},
        }

        # Mock the API response
        mock_response = mock_rest_response(data=project_list_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        response = api.admin_get_project_list(page=1, page_size=25)

        # Verify result
        assert isinstance(response, ProjectList)
        assert len(response.projects) == 2
        assert response.projects[0].name == "Project 1"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"

        parsed_url = urlparse(args[1])
        assert parsed_url.path.endswith("/admin/project")
        query_params = parse_qs(parsed_url.query)

        assert query_params["page"] == ["1"]
        assert query_params["pageSize"] == ["25"]

    def test_admin_update_project(self, mock_api_client, mock_rest_response):
        """Test case for admin_update_project"""
        api = AdminProjectManagementApi(api_client=mock_api_client)
        project_id = uuid4()
        project_data = {
            "id": str(project_id),
            "name": "Updated Project",
        }

        # Mock the API response
        mock_response = mock_rest_response(data=project_data, status=200)
        mock_api_client.call_api.return_value = mock_response

        # Call the API
        update_project = Project(name="Updated Project")
        response = api.admin_update_project(id=project_id, project=update_project)

        # Verify result
        assert isinstance(response, Project)
        assert str(response.id) == str(project_id)
        assert response.name == "Updated Project"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "PUT"
        assert args[1].endswith(f"/admin/project/{project_id}")
