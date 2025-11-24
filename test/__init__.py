"""Test utilities for ibutsu_client tests."""

import json
from typing import Any
from unittest.mock import Mock

from ibutsu_client.rest import RESTResponse


def create_mock_response(
    data: dict[str, Any] | list[Any] | None = None,
    status: int = 200,
    headers: dict[str, str] | None = None,
) -> RESTResponse:
    """Create a mock REST response for testing.

    Args:
        data: The response data (will be JSON-encoded)
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
