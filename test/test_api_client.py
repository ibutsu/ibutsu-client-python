"""Comprehensive tests for ApiClient."""

import datetime
import decimal
from enum import Enum
from pathlib import Path
from unittest.mock import Mock

import pytest
from pydantic import SecretStr

from ibutsu_client.api_client import ApiClient
from ibutsu_client.configuration import Configuration
from ibutsu_client.exceptions import (
    ApiException,
    ApiValueError,
    NotFoundException,
)


class TestApiClientInit:
    """Tests for ApiClient initialization."""

    def test_init_default_configuration(self):
        """Test initialization with default configuration."""
        client = ApiClient()
        assert client.configuration is not None
        assert isinstance(client.configuration, Configuration)
        assert client.default_headers is not None
        assert client.user_agent == "OpenAPI-Generator/3.1.1/python"
        assert client.client_side_validation is True

    def test_init_with_custom_configuration(self):
        """Test initialization with custom configuration."""
        config = Configuration(host="https://example.com")
        client = ApiClient(configuration=config)
        assert client.configuration == config
        assert client.configuration.host == "https://example.com"

    def test_init_with_header_name_and_value(self):
        """Test initialization with custom header."""
        client = ApiClient(header_name="X-Custom-Header", header_value="custom-value")
        assert "X-Custom-Header" in client.default_headers
        assert client.default_headers["X-Custom-Header"] == "custom-value"

    def test_init_with_cookie(self):
        """Test initialization with cookie."""
        client = ApiClient(cookie="session=abc123")
        assert client.cookie == "session=abc123"


class TestApiClientProperties:
    """Tests for ApiClient properties."""

    def test_user_agent_getter(self):
        """Test user_agent getter."""
        client = ApiClient()
        assert client.user_agent == "OpenAPI-Generator/3.1.1/python"

    def test_user_agent_setter(self):
        """Test user_agent setter."""
        client = ApiClient()
        client.user_agent = "CustomAgent/1.0"
        assert client.user_agent == "CustomAgent/1.0"
        assert client.default_headers["User-Agent"] == "CustomAgent/1.0"

    def test_set_default_header(self):
        """Test setting default headers."""
        client = ApiClient()
        client.set_default_header("X-API-Key", "secret-key")
        assert client.default_headers["X-API-Key"] == "secret-key"


class TestApiClientDefaultInstance:
    """Tests for ApiClient default instance management."""

    def test_get_default_creates_new_instance(self):
        """Test get_default creates a new instance if none exists."""
        # Reset the default
        ApiClient._default = None
        default = ApiClient.get_default()
        assert default is not None
        assert isinstance(default, ApiClient)

    def test_get_default_returns_same_instance(self):
        """Test get_default returns the same instance."""
        ApiClient._default = None
        default1 = ApiClient.get_default()
        default2 = ApiClient.get_default()
        assert default1 is default2

    def test_set_default(self):
        """Test setting custom default instance."""
        custom_config = Configuration(host="https://custom.com")
        custom_client = ApiClient(configuration=custom_config)
        ApiClient.set_default(custom_client)
        default = ApiClient.get_default()
        assert default is custom_client
        assert default.configuration.host == "https://custom.com"


class TestApiClientContextManager:
    """Tests for ApiClient context manager."""

    def test_context_manager_enter(self):
        """Test context manager __enter__."""
        client = ApiClient()
        with client as ctx:
            assert ctx is client

    def test_context_manager_exit(self):
        """Test context manager __exit__."""
        client = ApiClient()
        with client:
            pass
        # Should exit cleanly without errors


class TestSanitizeForSerialization:
    """Tests for sanitize_for_serialization method."""

    def test_sanitize_none(self):
        """Test sanitizing None returns None."""
        client = ApiClient()
        assert client.sanitize_for_serialization(None) is None

    def test_sanitize_primitive_types(self):
        """Test sanitizing primitive types."""
        client = ApiClient()
        assert client.sanitize_for_serialization(42) == 42
        assert client.sanitize_for_serialization(3.14) == 3.14
        assert client.sanitize_for_serialization("hello") == "hello"
        assert client.sanitize_for_serialization(True) is True
        assert client.sanitize_for_serialization(b"bytes") == b"bytes"

    def test_sanitize_enum(self):
        """Test sanitizing Enum."""

        class Color(Enum):
            RED = "red"
            BLUE = "blue"

        client = ApiClient()
        assert client.sanitize_for_serialization(Color.RED) == "red"

    def test_sanitize_secret_str(self):
        """Test sanitizing SecretStr."""
        client = ApiClient()
        secret = SecretStr("my-secret")
        result = client.sanitize_for_serialization(secret)
        assert result == "my-secret"

    def test_sanitize_uuid(self):
        """Test sanitizing UUID."""
        import uuid

        client = ApiClient()
        test_uuid = uuid.uuid4()
        result = client.sanitize_for_serialization(test_uuid)
        assert result == str(test_uuid)

    def test_sanitize_datetime(self):
        """Test sanitizing datetime."""
        client = ApiClient()
        dt = datetime.datetime(2023, 1, 15, 10, 30, 45)
        result = client.sanitize_for_serialization(dt)
        assert result == dt.isoformat()

    def test_sanitize_date(self):
        """Test sanitizing date."""
        client = ApiClient()
        d = datetime.date(2023, 1, 15)
        result = client.sanitize_for_serialization(d)
        assert result == d.isoformat()

    def test_sanitize_decimal(self):
        """Test sanitizing Decimal."""
        client = ApiClient()
        dec = decimal.Decimal("123.45")
        result = client.sanitize_for_serialization(dec)
        assert result == "123.45"

    def test_sanitize_list(self):
        """Test sanitizing list."""
        client = ApiClient()
        lst = [1, "two", datetime.date(2023, 1, 15)]
        result = client.sanitize_for_serialization(lst)
        assert result == [1, "two", "2023-01-15"]

    def test_sanitize_tuple(self):
        """Test sanitizing tuple."""
        client = ApiClient()
        tpl = (1, "two", datetime.date(2023, 1, 15))
        result = client.sanitize_for_serialization(tpl)
        assert result == (1, "two", "2023-01-15")

    def test_sanitize_dict(self):
        """Test sanitizing dict."""
        client = ApiClient()
        d = {"key1": 1, "key2": datetime.date(2023, 1, 15)}
        result = client.sanitize_for_serialization(d)
        assert result == {"key1": 1, "key2": "2023-01-15"}

    def test_sanitize_object_with_to_dict(self):
        """Test sanitizing object with to_dict method."""
        client = ApiClient()

        class MockModel:
            def to_dict(self):
                return {"field": "value"}

        obj = MockModel()
        result = client.sanitize_for_serialization(obj)
        assert result == {"field": "value"}

    def test_sanitize_object_with_dict_attribute(self):
        """Test sanitizing object with __dict__."""
        client = ApiClient()

        class MockModel:
            def __init__(self):
                self.field = "value"

        obj = MockModel()
        result = client.sanitize_for_serialization(obj)
        assert result == {"field": "value"}

    def test_sanitize_nested_structures(self):
        """Test sanitizing nested data structures."""
        client = ApiClient()
        data = {
            "list": [1, 2, {"nested": datetime.date(2023, 1, 15)}],
            "dict": {"key": datetime.datetime(2023, 1, 15, 10, 30)},
        }
        result = client.sanitize_for_serialization(data)
        assert result["list"][2]["nested"] == "2023-01-15"
        assert "2023-01-15T10:30:00" in result["dict"]["key"]


class TestParametersToTuples:
    """Tests for parameters_to_tuples method."""

    def test_parameters_dict_no_collection_formats(self):
        """Test converting dict parameters without collection formats."""
        client = ApiClient()
        params = {"key1": "value1", "key2": "value2"}
        result = client.parameters_to_tuples(params, None)
        assert ("key1", "value1") in result
        assert ("key2", "value2") in result

    def test_parameters_list_of_tuples(self):
        """Test converting list of tuples."""
        client = ApiClient()
        params = [("key1", "value1"), ("key2", "value2")]
        result = client.parameters_to_tuples(params, None)
        assert result == params

    def test_parameters_multi_collection_format(self):
        """Test multi collection format."""
        client = ApiClient()
        params = {"tags": ["tag1", "tag2", "tag3"]}
        collection_formats = {"tags": "multi"}
        result = client.parameters_to_tuples(params, collection_formats)
        assert result == [("tags", "tag1"), ("tags", "tag2"), ("tags", "tag3")]

    def test_parameters_csv_collection_format(self):
        """Test CSV collection format."""
        client = ApiClient()
        params = {"tags": ["tag1", "tag2", "tag3"]}
        collection_formats = {"tags": "csv"}
        result = client.parameters_to_tuples(params, collection_formats)
        assert result == [("tags", "tag1,tag2,tag3")]

    def test_parameters_ssv_collection_format(self):
        """Test SSV (space-separated values) collection format."""
        client = ApiClient()
        params = {"tags": ["tag1", "tag2", "tag3"]}
        collection_formats = {"tags": "ssv"}
        result = client.parameters_to_tuples(params, collection_formats)
        assert result == [("tags", "tag1 tag2 tag3")]

    def test_parameters_tsv_collection_format(self):
        """Test TSV (tab-separated values) collection format."""
        client = ApiClient()
        params = {"tags": ["tag1", "tag2", "tag3"]}
        collection_formats = {"tags": "tsv"}
        result = client.parameters_to_tuples(params, collection_formats)
        assert result == [("tags", "tag1\ttag2\ttag3")]

    def test_parameters_pipes_collection_format(self):
        """Test pipes collection format."""
        client = ApiClient()
        params = {"tags": ["tag1", "tag2", "tag3"]}
        collection_formats = {"tags": "pipes"}
        result = client.parameters_to_tuples(params, collection_formats)
        assert result == [("tags", "tag1|tag2|tag3")]


class TestParametersToUrlQuery:
    """Tests for parameters_to_url_query method."""

    def test_parameters_to_url_query_simple(self):
        """Test converting simple parameters to URL query."""
        client = ApiClient()
        params = {"key1": "value1", "key2": "value2"}
        result = client.parameters_to_url_query(params, None)
        assert "key1=value1" in result
        assert "key2=value2" in result

    def test_parameters_to_url_query_with_bool(self):
        """Test converting boolean parameters."""
        client = ApiClient()
        params = {"active": True, "disabled": False}
        result = client.parameters_to_url_query(params, None)
        assert "active=true" in result
        assert "disabled=false" in result

    def test_parameters_to_url_query_with_numbers(self):
        """Test converting numeric parameters."""
        client = ApiClient()
        params = {"count": 42, "price": 19.99}
        result = client.parameters_to_url_query(params, None)
        assert "count=42" in result
        assert "price=19.99" in result

    def test_parameters_to_url_query_with_dict(self):
        """Test converting dict parameter to JSON."""
        client = ApiClient()
        params = {"filter": {"name": "test"}}
        result = client.parameters_to_url_query(params, None)
        assert "filter=" in result
        # Dict should be JSON-encoded and URL-encoded

    def test_parameters_to_url_query_multi_format(self):
        """Test URL query with multi collection format."""
        client = ApiClient()
        params = {"tags": ["tag1", "tag2"]}
        collection_formats = {"tags": "multi"}
        result = client.parameters_to_url_query(params, collection_formats)
        assert "tags=tag1" in result
        assert "tags=tag2" in result

    def test_parameters_to_url_query_csv_format(self):
        """Test URL query with CSV collection format."""
        client = ApiClient()
        params = {"tags": ["tag1", "tag2"]}
        collection_formats = {"tags": "csv"}
        result = client.parameters_to_url_query(params, collection_formats)
        # Note: The actual implementation doesn't URL-encode the delimiter itself
        assert "tags=tag1,tag2" in result or "tags=tag1%2Ctag2" in result

    def test_parameters_to_url_query_special_chars(self):
        """Test URL query with special characters."""
        client = ApiClient()
        params = {"query": "hello world", "filter": "a&b"}
        result = client.parameters_to_url_query(params, None)
        # Should be URL-encoded
        assert "hello%20world" in result or "hello+world" in result


class TestFilesParameters:
    """Tests for files_parameters method."""

    def test_files_parameters_from_path(self, tmp_path):
        """Test files parameters from file path."""
        client = ApiClient()
        test_file = tmp_path / "test.txt"
        test_file.write_bytes(b"test content")

        result = client.files_parameters({"file": str(test_file)})
        assert len(result) == 1
        assert result[0][0] == "file"
        assert result[0][1][0] == "test.txt"
        assert result[0][1][1] == b"test content"
        assert "text/plain" in result[0][1][2]

    def test_files_parameters_from_bytes(self):
        """Test files parameters from bytes."""
        client = ApiClient()
        result = client.files_parameters({"file": b"test content"})
        assert len(result) == 1
        assert result[0][0] == "file"
        assert result[0][1][0] == "file"
        assert result[0][1][1] == b"test content"

    def test_files_parameters_from_tuple(self):
        """Test files parameters from tuple."""
        client = ApiClient()
        result = client.files_parameters({"file": ("custom.txt", b"test content")})
        assert len(result) == 1
        assert result[0][0] == "file"
        assert result[0][1][0] == "custom.txt"
        assert result[0][1][1] == b"test content"

    def test_files_parameters_from_list(self, tmp_path):
        """Test files parameters from list of files."""
        client = ApiClient()
        file1 = tmp_path / "file1.txt"
        file1.write_bytes(b"content1")
        file2 = tmp_path / "file2.txt"
        file2.write_bytes(b"content2")

        result = client.files_parameters({"files": [str(file1), str(file2)]})
        assert len(result) == 2
        assert result[0][0] == "files"
        assert result[1][0] == "files"

    def test_files_parameters_unsupported_type(self):
        """Test files parameters with unsupported type."""
        client = ApiClient()
        with pytest.raises(ValueError, match="Unsupported file value"):
            client.files_parameters({"file": 123})


class TestSelectHeader:
    """Tests for select_header_accept and select_header_content_type."""

    def test_select_header_accept_empty(self):
        """Test select_header_accept with empty list."""
        client = ApiClient()
        result = client.select_header_accept([])
        assert result is None

    def test_select_header_accept_with_json(self):
        """Test select_header_accept prefers JSON."""
        client = ApiClient()
        accepts = ["text/plain", "application/json", "text/html"]
        result = client.select_header_accept(accepts)
        assert result == "application/json"

    def test_select_header_accept_no_json(self):
        """Test select_header_accept without JSON."""
        client = ApiClient()
        accepts = ["text/plain", "text/html"]
        result = client.select_header_accept(accepts)
        assert result == "text/plain"

    def test_select_header_content_type_empty(self):
        """Test select_header_content_type with empty list."""
        client = ApiClient()
        result = client.select_header_content_type([])
        assert result is None

    def test_select_header_content_type_with_json(self):
        """Test select_header_content_type prefers JSON."""
        client = ApiClient()
        content_types = ["text/plain", "application/json", "text/html"]
        result = client.select_header_content_type(content_types)
        assert result == "application/json"

    def test_select_header_content_type_no_json(self):
        """Test select_header_content_type without JSON."""
        client = ApiClient()
        content_types = ["text/plain", "text/html"]
        result = client.select_header_content_type(content_types)
        assert result == "text/plain"


class TestParamSerialize:
    """Tests for param_serialize method."""

    def test_param_serialize_basic(self):
        """Test basic param serialization."""
        client = ApiClient()
        method, url, headers, _body, _post_params = client.param_serialize(
            method="GET",
            resource_path="/api/test",
            query_params={"page": 1},
        )
        assert method == "GET"
        assert "/api/test?page=1" in url
        assert headers is not None

    def test_param_serialize_with_path_params(self):
        """Test param serialization with path parameters."""
        client = ApiClient()
        _method, url, _headers, _body, _post_params = client.param_serialize(
            method="GET",
            resource_path="/api/test/{id}",
            path_params={"id": "123"},
        )
        assert "/api/test/123" in url

    def test_param_serialize_with_header_params(self):
        """Test param serialization with header parameters."""
        client = ApiClient()
        _method, _url, headers, _body, _post_params = client.param_serialize(
            method="GET",
            resource_path="/api/test",
            header_params={"X-Custom": "value"},
        )
        assert "X-Custom" in headers
        assert headers["X-Custom"] == "value"

    def test_param_serialize_with_body(self):
        """Test param serialization with body."""
        client = ApiClient()
        _method, _url, _headers, body, _post_params = client.param_serialize(
            method="POST",
            resource_path="/api/test",
            body={"name": "test"},
        )
        assert body == {"name": "test"}

    def test_param_serialize_with_cookie(self):
        """Test param serialization includes cookie."""
        client = ApiClient(cookie="session=abc123")
        _method, _url, headers, _body, _post_params = client.param_serialize(
            method="GET",
            resource_path="/api/test",
        )
        assert "Cookie" in headers
        assert headers["Cookie"] == "session=abc123"


class TestCallApi:
    """Tests for call_api method."""

    def test_call_api_success(self, mocker):
        """Test successful API call."""
        client = ApiClient()
        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b'{"result": "success"}'
        mock_response.reason = "OK"

        mocker.patch.object(client.rest_client, "request", return_value=mock_response)

        result = client.call_api(
            method="GET",
            url="https://example.com/api/test",
            header_params={"Content-Type": "application/json"},
        )
        assert result == mock_response

    def test_call_api_with_exception(self, mocker):
        """Test API call that raises ApiException."""
        client = ApiClient()
        mocker.patch.object(
            client.rest_client,
            "request",
            side_effect=ApiException(status=404, reason="Not Found"),
        )

        with pytest.raises(ApiException) as exc_info:
            client.call_api(
                method="GET",
                url="https://example.com/api/test",
            )
        assert exc_info.value.status == 404


class TestResponseDeserialize:
    """Tests for response_deserialize method."""

    def test_response_deserialize_json(self, mocker):
        """Test deserializing JSON response."""
        from ibutsu_client.models.health import Health

        client = ApiClient()
        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b'{"status": "OK", "message": "test"}'
        mock_response.getheader = lambda x: "application/json" if x == "content-type" else None
        mock_response.getheaders = lambda: {"content-type": "application/json"}

        result = client.response_deserialize(
            response_data=mock_response,
            response_types_map={"200": Health},
        )
        assert result.status_code == 200
        assert isinstance(result.data, Health)
        assert result.data.status == "OK"

    def test_response_deserialize_bytearray(self):
        """Test deserializing bytearray response."""
        client = ApiClient()
        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"binary content"
        mock_response.getheaders = dict

        result = client.response_deserialize(
            response_data=mock_response,
            response_types_map={"200": "bytearray"},
        )
        assert result.status_code == 200
        assert result.data == b"binary content"

    def test_response_deserialize_error_status(self):
        """Test deserializing error response."""
        client = ApiClient()
        mock_response = Mock()
        mock_response.status = 404
        mock_response.data = b'{"error": "not found"}'
        mock_response.reason = "Not Found"
        mock_response.getheader = lambda x: "application/json" if x == "content-type" else None
        mock_response.getheaders = lambda: {"content-type": "application/json"}

        with pytest.raises(NotFoundException):
            client.response_deserialize(
                response_data=mock_response,
                response_types_map={"404": dict},
            )

    def test_response_deserialize_file(self, tmp_path, mocker):
        """Test deserializing file response."""
        client = ApiClient()
        client.configuration.temp_folder_path = str(tmp_path)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"file content"
        mock_response.getheader = lambda x: (
            'attachment; filename="test.txt"' if x == "Content-Disposition" else None
        )
        mock_response.getheaders = lambda: {
            "Content-Disposition": 'attachment; filename="test.txt"'
        }

        result = client.response_deserialize(
            response_data=mock_response,
            response_types_map={"200": "file"},
        )
        assert result.status_code == 200
        assert Path(result.data).exists()
        assert Path(result.data).read_bytes() == b"file content"

    def test_response_deserialize_with_2xx_wildcard(self):
        """Test deserializing with 2XX wildcard response type."""
        from ibutsu_client.models.health import Health

        client = ApiClient()
        mock_response = Mock()
        mock_response.status = 201
        mock_response.data = b'{"status": "OK"}'
        mock_response.getheader = lambda x: "application/json" if x == "content-type" else None
        mock_response.getheaders = lambda: {"content-type": "application/json"}

        result = client.response_deserialize(
            response_data=mock_response,
            response_types_map={"2XX": Health},
        )
        assert result.status_code == 201
        assert isinstance(result.data, Health)


class TestDeserialize:
    """Tests for deserialize method."""

    def test_deserialize_json_string(self):
        """Test deserializing JSON string."""
        from ibutsu_client.models.health import Health

        client = ApiClient()
        result = client.deserialize('{"status": "OK"}', Health, "application/json")
        assert isinstance(result, Health)
        assert result.status == "OK"

    def test_deserialize_empty_json(self):
        """Test deserializing empty JSON string."""
        client = ApiClient()
        result = client.deserialize("", str, "application/json")
        assert result == ""

    def test_deserialize_text_plain(self):
        """Test deserializing plain text."""
        client = ApiClient()
        result = client.deserialize("plain text", str, "text/plain")
        assert result == "plain text"

    def test_deserialize_no_content_type(self):
        """Test deserializing without content type."""
        from ibutsu_client.models.health import Health

        client = ApiClient()
        result = client.deserialize('{"status": "OK"}', Health, None)
        assert isinstance(result, Health)
        assert result.status == "OK"

    def test_deserialize_unsupported_content_type(self):
        """Test deserializing unsupported content type."""
        client = ApiClient()
        with pytest.raises(ApiException, match="Unsupported content type"):
            client.deserialize("data", str, "application/octet-stream")

    def test_deserialize_list_type(self):
        """Test deserializing List type."""
        client = ApiClient()
        result = client.deserialize("[1, 2, 3]", "List[int]", "application/json")
        assert result == [1, 2, 3]

    def test_deserialize_dict_type(self):
        """Test deserializing Dict type."""
        client = ApiClient()
        result = client.deserialize('{"a": 1, "b": 2}', "Dict[str, int]", "application/json")
        assert result == {"a": 1, "b": 2}


class TestUpdateParamsForAuth:
    """Tests for update_params_for_auth method."""

    def test_update_params_for_auth_no_settings(self):
        """Test update params with no auth settings."""
        client = ApiClient()
        headers = {}
        queries = []
        client.update_params_for_auth(headers, queries, None, "/api/test", "GET", None)
        # Should not modify headers or queries

    def test_update_params_for_auth_with_bearer_token(self):
        """Test update params with bearer token."""
        config = Configuration(access_token="test-token")
        client = ApiClient(configuration=config)
        headers = {}
        queries = []
        client.update_params_for_auth(headers, queries, ["jwt"], "/api/test", "GET", None)
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer test-token"

    def test_update_params_for_auth_cookie(self):
        """Test update params with cookie auth."""
        client = ApiClient()
        headers = {}
        queries = []
        auth_setting = {
            "in": "cookie",
            "value": "session=abc123",
        }
        client._apply_auth_params(headers, queries, "/api/test", "GET", None, auth_setting)
        assert "Cookie" in headers
        assert headers["Cookie"] == "session=abc123"

    def test_update_params_for_auth_query(self):
        """Test update params with query auth."""
        client = ApiClient()
        headers = {}
        queries = []
        auth_setting = {
            "in": "query",
            "key": "api_key",
            "value": "secret-key",
        }
        client._apply_auth_params(headers, queries, "/api/test", "GET", None, auth_setting)
        assert ("api_key", "secret-key") in queries

    def test_update_params_for_auth_invalid_location(self):
        """Test update params with invalid auth location."""
        client = ApiClient()
        headers = {}
        queries = []
        auth_setting = {
            "in": "invalid",
            "key": "key",
            "value": "value",
        }
        with pytest.raises(ApiValueError, match="Authentication token must be in"):
            client._apply_auth_params(headers, queries, "/api/test", "GET", None, auth_setting)


class TestPrivateDeserializeMethods:
    """Tests for private deserialization methods."""

    def test_deserialize_primitive_int(self):
        """Test deserializing primitive int."""
        client = ApiClient()
        result = client._ApiClient__deserialize_primitive("42", int)
        assert result == 42

    def test_deserialize_primitive_float(self):
        """Test deserializing primitive float."""
        client = ApiClient()
        result = client._ApiClient__deserialize_primitive("3.14", float)
        assert result == 3.14

    def test_deserialize_primitive_bool(self):
        """Test deserializing primitive bool."""
        client = ApiClient()
        result = client._ApiClient__deserialize_primitive(True, bool)
        assert result is True

    def test_deserialize_object(self):
        """Test deserializing object."""
        client = ApiClient()
        value = {"key": "value"}
        result = client._ApiClient__deserialize_object(value)
        assert result == value

    def test_deserialize_date(self):
        """Test deserializing date."""
        client = ApiClient()
        result = client._ApiClient__deserialize_date("2023-01-15")
        assert result == datetime.date(2023, 1, 15)

    def test_deserialize_date_invalid(self):
        """Test deserializing invalid date."""
        client = ApiClient()
        with pytest.raises(ApiException, match="Failed to parse"):
            client._ApiClient__deserialize_date("invalid-date")

    def test_deserialize_datetime(self):
        """Test deserializing datetime."""
        client = ApiClient()
        result = client._ApiClient__deserialize_datetime("2023-01-15T10:30:00")
        assert result.year == 2023
        assert result.month == 1
        assert result.day == 15

    def test_deserialize_datetime_invalid(self):
        """Test deserializing invalid datetime."""
        client = ApiClient()
        with pytest.raises(ApiException, match="Failed to parse"):
            client._ApiClient__deserialize_datetime("invalid-datetime")

    def test_deserialize_enum(self):
        """Test deserializing enum."""

        class Color(Enum):
            RED = "red"
            BLUE = "blue"

        client = ApiClient()
        result = client._ApiClient__deserialize_enum("red", Color)
        assert result == Color.RED

    def test_deserialize_enum_invalid(self):
        """Test deserializing invalid enum."""

        class Color(Enum):
            RED = "red"
            BLUE = "blue"

        client = ApiClient()
        with pytest.raises(ApiException, match="Failed to parse"):
            client._ApiClient__deserialize_enum("green", Color)

    def test_deserialize_model(self, mocker):
        """Test deserializing model."""
        client = ApiClient()

        class MockModel:
            @classmethod
            def from_dict(cls, data):
                return {"model": "data"}

        result = client._ApiClient__deserialize_model({"key": "value"}, MockModel)
        assert result == {"model": "data"}
