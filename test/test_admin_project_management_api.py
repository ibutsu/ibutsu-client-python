"""Tests for AdminProjectManagementApi."""

from urllib.parse import parse_qs, urlparse
from uuid import uuid4

import pytest

from ibutsu_client.api.admin_project_management_api import AdminProjectManagementApi
from ibutsu_client.models.project import Project
from ibutsu_client.models.project_list import ProjectList


class TestAdminProjectManagementApi:
    """AdminProjectManagementApi Tests"""

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "PROJECT_ID_PLACEHOLDER",
                    "name": "New Project",
                    "title": "New Project Title",
                },
                "status": 201,
            }
        ],
        indirect=True,
    )
    def test_admin_add_project(self, mock_api_client, create_mock_response):
        """Test case for admin_add_project"""
        api = AdminProjectManagementApi(api_client=mock_api_client)
        project_id = uuid4()

        # Update the mock response with the actual project_id
        create_mock_response.data = create_mock_response.data.replace(
            b"PROJECT_ID_PLACEHOLDER", str(project_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

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

    @pytest.mark.parametrize(
        "create_mock_response",
        [{"data": {}, "status": 200}],
        indirect=True,
    )
    def test_admin_delete_project(self, mock_api_client, create_mock_response):
        """Test case for admin_delete_project"""
        api = AdminProjectManagementApi(api_client=mock_api_client)
        project_id = uuid4()

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        api.admin_delete_project(id=project_id)

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "DELETE"
        assert args[1].endswith(f"/admin/project/{project_id}")

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "PROJECT_ID_PLACEHOLDER",
                    "name": "My Project",
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_admin_get_project(self, mock_api_client, create_mock_response):
        """Test case for admin_get_project"""
        api = AdminProjectManagementApi(api_client=mock_api_client)
        project_id = uuid4()

        # Update the mock response with the actual project_id
        create_mock_response.data = create_mock_response.data.replace(
            b"PROJECT_ID_PLACEHOLDER", str(project_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

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

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "projects": [
                        {"id": "00000000-0000-0000-0000-000000000001", "name": "Project 1"},
                        {"id": "00000000-0000-0000-0000-000000000002", "name": "Project 2"},
                    ],
                    "pagination": {"page": 1, "pageSize": 25, "totalItems": 2, "totalPages": 1},
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_admin_get_project_list(self, mock_api_client, create_mock_response):
        """Test case for admin_get_project_list"""
        api = AdminProjectManagementApi(api_client=mock_api_client)

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

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

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "PROJECT_ID_PLACEHOLDER",
                    "name": "Updated Project",
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_admin_update_project(self, mock_api_client, create_mock_response):
        """Test case for admin_update_project"""
        api = AdminProjectManagementApi(api_client=mock_api_client)
        project_id = uuid4()

        # Update the mock response with the actual project_id
        create_mock_response.data = create_mock_response.data.replace(
            b"PROJECT_ID_PLACEHOLDER", str(project_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

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
