"""Tests for ProjectApi."""

from urllib.parse import parse_qs, urlparse
from uuid import uuid4

import pytest

from ibutsu_client.api.project_api import ProjectApi
from ibutsu_client.models.project import Project
from ibutsu_client.models.project_list import ProjectList


class TestProjectApi:
    """ProjectApi Tests"""

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "PROJECT_ID_PLACEHOLDER",
                    "name": "test-project",
                    "title": "Test Project",
                },
                "status": 201,
            }
        ],
        indirect=True,
    )
    def test_add_project(self, mock_api_client, create_mock_response):
        """Test case for add_project"""
        api = ProjectApi(api_client=mock_api_client)
        project_id = uuid4()

        # Update the mock response with the actual project_id
        create_mock_response.data = create_mock_response.data.replace(
            b"PROJECT_ID_PLACEHOLDER", str(project_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

        # Create project object to send
        project_item = Project(name="test-project", title="Test Project")

        # Call the API
        response = api.add_project(project=project_item)

        # Verify the response is deserialized correctly
        assert isinstance(response, Project)
        assert str(response.id) == str(project_id)
        assert response.name == "test-project"

        # Verify call_api was called with correct arguments
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "POST"  # method
        assert args[1].endswith("/project")  # url

        # Body is serialized to dict
        assert isinstance(args[3], dict)
        assert args[3]["name"] == "test-project"
        assert args[3]["title"] == "Test Project"

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "PROJECT_ID_PLACEHOLDER",
                    "name": "test-project",
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_get_project(self, mock_api_client, create_mock_response):
        """Test case for get_project"""
        api = ProjectApi(api_client=mock_api_client)
        project_id = uuid4()

        # Update the mock response with the actual project_id
        create_mock_response.data = create_mock_response.data.replace(
            b"PROJECT_ID_PLACEHOLDER", str(project_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        response = api.get_project(id=str(project_id))

        # Verify result
        assert isinstance(response, Project)
        assert str(response.id) == str(project_id)
        assert response.name == "test-project"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert args[1].endswith(f"/project/{project_id}")

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "projects": [
                        {"id": "00000000-0000-0000-0000-000000000001", "name": "project1"},
                        {"id": "00000000-0000-0000-0000-000000000002", "name": "project2"},
                    ],
                    "pagination": {"page": 1, "pageSize": 25, "totalItems": 2, "totalPages": 1},
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_get_project_list(self, mock_api_client, create_mock_response):
        """Test case for get_project_list"""
        api = ProjectApi(api_client=mock_api_client)

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        response = api.get_project_list(page=1, page_size=25, owner_id="user1")

        # Verify result
        assert isinstance(response, ProjectList)
        assert len(response.projects) == 2
        assert response.projects[0].name == "project1"
        assert response.pagination.total_items == 2

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "GET"

        parsed_url = urlparse(args[1])
        assert parsed_url.path.endswith("/project")
        query_params = parse_qs(parsed_url.query)

        assert query_params["page"] == ["1"]
        assert query_params["pageSize"] == ["25"]
        assert query_params["ownerId"] == ["user1"]

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "PROJECT_ID_PLACEHOLDER",
                    "name": "updated-project",
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_update_project(self, mock_api_client, create_mock_response):
        """Test case for update_project"""
        api = ProjectApi(api_client=mock_api_client)
        project_id = uuid4()

        # Update the mock response with the actual project_id
        create_mock_response.data = create_mock_response.data.replace(
            b"PROJECT_ID_PLACEHOLDER", str(project_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

        # Update object
        project_update = Project(name="updated-project")

        # Call the API
        response = api.update_project(id=project_id, project=project_update)

        # Verify result
        assert isinstance(response, Project)
        assert str(response.id) == str(project_id)
        assert response.name == "updated-project"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "PUT"
        assert args[1].endswith(f"/project/{project_id}")

        # Body is serialized
        assert isinstance(args[3], dict)
        assert args[3]["name"] == "updated-project"

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": ["env", "component", "tag"],
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_get_filter_params(self, mock_api_client, create_mock_response):
        """Test case for get_filter_params"""
        api = ProjectApi(api_client=mock_api_client)
        project_id = uuid4()

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

        # Call API
        response = api.get_filter_params(id=str(project_id))

        # Verify result
        assert isinstance(response, list)
        assert response == ["env", "component", "tag"]

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert args[1].endswith(f"/project/filter-params/{project_id}")
