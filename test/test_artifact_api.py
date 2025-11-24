"""Tests for ArtifactApi."""

from uuid import uuid4

import pytest

from ibutsu_client.api.artifact_api import ArtifactApi
from ibutsu_client.models.artifact import Artifact
from ibutsu_client.models.artifact_list import ArtifactList


class TestArtifactApi:
    """ArtifactApi Tests"""

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "artifacts": [
                        {
                            "id": "00000000-0000-0000-0000-000000000001",
                            "filename": "test1.txt",
                            "mime_type": "text/plain",
                        },
                        {
                            "id": "00000000-0000-0000-0000-000000000002",
                            "filename": "test2.png",
                            "mime_type": "image/png",
                        },
                    ],
                    "pagination": {"page": 1, "pageSize": 25, "totalItems": 2, "totalPages": 1},
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_get_artifact_list(self, mock_api_client, create_mock_response):
        """Test case for get_artifact_list"""
        api = ArtifactApi(api_client=mock_api_client)

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        response = api.get_artifact_list(page=1, page_size=25)

        # Verify result
        assert isinstance(response, ArtifactList)
        assert len(response.artifacts) == 2
        assert response.artifacts[0].filename == "test1.txt"
        assert response.pagination.total_items == 2

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert "/artifact" in args[1]
        assert "page=1" in args[1]
        assert "pageSize=25" in args[1]

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "ARTIFACT_ID_PLACEHOLDER",
                    "filename": "test.txt",
                    "mime_type": "text/plain",
                },
                "status": 200,
            }
        ],
        indirect=True,
    )
    def test_get_artifact(self, mock_api_client, create_mock_response):
        """Test case for get_artifact"""
        api = ArtifactApi(api_client=mock_api_client)
        artifact_id = uuid4()

        # Update the mock response with the actual artifact_id
        create_mock_response.data = create_mock_response.data.replace(
            b"ARTIFACT_ID_PLACEHOLDER", str(artifact_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        response = api.get_artifact(id=artifact_id)

        # Verify result
        assert isinstance(response, Artifact)
        assert str(response.id) == str(artifact_id)
        assert response.filename == "test.txt"

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert args[1].endswith(f"/artifact/{artifact_id}")

    @pytest.mark.parametrize(
        "create_mock_response",
        [{"data": b"file content", "status": 200}],
        indirect=True,
    )
    def test_download_artifact(self, mock_api_client, create_mock_response):
        """Test case for download_artifact"""
        api = ArtifactApi(api_client=mock_api_client)
        artifact_id = uuid4()
        file_content = b"file content"

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        response = api.download_artifact(id=artifact_id)

        # Verify result
        assert response == file_content

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert args[1].endswith(f"/artifact/{artifact_id}/download")

    @pytest.mark.parametrize(
        "create_mock_response",
        [{"data": b"file content", "status": 200}],
        indirect=True,
    )
    def test_view_artifact(self, mock_api_client, create_mock_response):
        """Test case for view_artifact"""
        api = ArtifactApi(api_client=mock_api_client)
        artifact_id = uuid4()
        file_content = b"file content"

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        response = api.view_artifact(id=artifact_id)

        # Verify result
        assert response == file_content

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "GET"
        assert args[1].endswith(f"/artifact/{artifact_id}/view")

    @pytest.mark.parametrize(
        "create_mock_response",
        [
            {
                "data": {
                    "id": "ARTIFACT_ID_PLACEHOLDER",
                    "filename": "test.txt",
                    "result_id": None,
                    "run_id": "RUN_ID_PLACEHOLDER",
                },
                "status": 201,
            }
        ],
        indirect=True,
    )
    def test_upload_artifact(self, mock_api_client, create_mock_response):
        """Test case for upload_artifact"""
        api = ArtifactApi(api_client=mock_api_client)
        run_id = uuid4()
        artifact_id = uuid4()
        filename = "test.txt"
        file_content = b"content"

        # Update the mock response with the actual IDs
        create_mock_response.data = create_mock_response.data.replace(
            b"ARTIFACT_ID_PLACEHOLDER", str(artifact_id).encode()
        )
        create_mock_response.data = create_mock_response.data.replace(
            b"RUN_ID_PLACEHOLDER", str(run_id).encode()
        )
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        response = api.upload_artifact(filename=filename, file=file_content, run_id=run_id)

        # Verify result
        assert isinstance(response, Artifact)
        assert response.filename == filename
        assert str(response.run_id) == str(run_id)

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _kwargs = mock_api_client.call_api.call_args
        assert args[0] == "POST"
        assert args[1].endswith("/artifact")

        # Verify form params include file and metadata
        # args[4] is post_params
        post_params = args[4]
        # Check if file is in post_params
        # post_params is a list of tuples
        # param[1] should be (filename, filedata, mimetype)
        file_found = any(
            param[0] == "file" and param[1][1] == file_content for param in post_params
        )
        assert file_found

    @pytest.mark.parametrize(
        "create_mock_response",
        [{"data": {}, "status": 200}],
        indirect=True,
    )
    def test_delete_artifact(self, mock_api_client, create_mock_response):
        """Test case for delete_artifact"""
        api = ArtifactApi(api_client=mock_api_client)
        artifact_id = uuid4()

        # Mock the API response
        mock_api_client.call_api.return_value = create_mock_response

        # Call the API
        api.delete_artifact(id=artifact_id)

        # Verify call
        mock_api_client.call_api.assert_called_once()
        args, _ = mock_api_client.call_api.call_args
        assert args[0] == "DELETE"
        assert args[1].endswith(f"/artifact/{artifact_id}")
