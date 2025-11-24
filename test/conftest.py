"""Test configuration and fixtures for ibutsu_client tests."""

import json
from typing import Any
from unittest.mock import Mock

import pytest

from ibutsu_client.rest import RESTResponse


def _make_mock_response(
    data: dict[str, Any] | list[Any] | bytes | None = None,
    status: int = 200,
    headers: dict[str, str] | None = None,
) -> RESTResponse:
    """Internal helper to create a mock REST response.

    Args:
        data: The response data (will be JSON-encoded unless bytes)
        status: HTTP status code
        headers: Response headers

    Returns:
        A mock RESTResponse object
    """
    if headers is None:
        headers = {"Content-Type": "application/json; charset=utf-8"}

    if data is None:
        data = {}

    response = Mock(spec=RESTResponse)
    response.status = status
    response.headers = headers
    # Handle bytes data directly without JSON encoding
    if isinstance(data, bytes):
        response.data = data
    else:
        response.data = json.dumps(data).encode("utf-8")
    response.reason = "OK" if status < 400 else "Error"

    def mock_read():
        """Mock the read method to decode the response data."""
        return response.data

    def mock_getheader(name: str, default: str | None = None) -> str | None:
        """Mock the getheader method."""
        return headers.get(name, default)

    def mock_getheaders() -> dict[str, str]:
        """Mock the getheaders method."""
        return headers

    response.read = mock_read
    response.getheader = mock_getheader
    response.getheaders = mock_getheaders
    return response


@pytest.fixture
def mock_api_client():
    """Create a mock ApiClient for testing API methods."""
    from ibutsu_client.api_client import ApiClient

    client = ApiClient()
    client.call_api = Mock()
    return client


@pytest.fixture
def create_mock_response(request):
    """Parametrized fixture for creating mock API responses.

    Use with indirect parametrization. Call factory functions directly in the parametrize decorator:

    Example:
        from test.utils import sample_project_data

        @pytest.mark.parametrize('create_mock_response', [
            {'data': sample_project_data(name='test', title='Test'), 'status': 201},
            {'data': {'error': 'not found'}, 'status': 404},
        ], indirect=True)
        def test_api_method(self, mocker, create_mock_response):
            api = SomeApi()
            mocker.patch.object(api.api_client, "call_api", return_value=create_mock_response)
            result = api.method()
            ...

    Args:
        request.param: Dict with keys:
            - data: Response data dict/list/bytes
            - status: HTTP status code (default: 200)
            - headers: Response headers dict (optional)

    Returns:
        Mock RESTResponse object ready to use
    """
    params = request.param
    data = params.get("data", {})
    status = params.get("status", 200)
    headers = params.get("headers", None)

    return _make_mock_response(data=data, status=status, headers=headers)
