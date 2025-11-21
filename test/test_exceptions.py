"""Comprehensive tests for exceptions module."""

from unittest.mock import Mock

import pytest

from ibutsu_client.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    BadRequestException,
    ConflictException,
    ForbiddenException,
    NotFoundException,
    OpenApiException,
    ServiceException,
    UnauthorizedException,
    UnprocessableEntityException,
    render_path,
)


class TestOpenApiException:
    """Tests for OpenApiException base class."""

    def test_openapi_exception_is_exception(self):
        """Test OpenApiException is a standard Exception."""
        exc = OpenApiException("test error")
        assert isinstance(exc, Exception)

    def test_openapi_exception_message(self):
        """Test OpenApiException message."""
        exc = OpenApiException("test error")
        assert str(exc) == "test error"


class TestApiTypeError:
    """Tests for ApiTypeError."""

    def test_api_type_error_basic(self):
        """Test ApiTypeError with basic message."""
        exc = ApiTypeError("Invalid type")
        assert "Invalid type" in str(exc)
        assert isinstance(exc, TypeError)
        assert isinstance(exc, OpenApiException)

    def test_api_type_error_with_path(self):
        """Test ApiTypeError with path_to_item."""
        exc = ApiTypeError("Invalid type", path_to_item=["data", "user", "id"])
        error_str = str(exc)
        assert "Invalid type" in error_str
        assert "['data']['user']['id']" in error_str

    def test_api_type_error_with_valid_classes(self):
        """Test ApiTypeError stores valid_classes."""
        exc = ApiTypeError(
            "Invalid type",
            valid_classes=(str, int),
        )
        assert exc.valid_classes == (str, int)

    def test_api_type_error_with_key_type(self):
        """Test ApiTypeError stores key_type."""
        exc = ApiTypeError("Invalid type", key_type=True)
        assert exc.key_type is True

    def test_api_type_error_all_params(self):
        """Test ApiTypeError with all parameters."""
        exc = ApiTypeError(
            "Invalid type",
            path_to_item=["data", 0, "field"],
            valid_classes=(str, int),
            key_type=False,
        )
        assert exc.path_to_item == ["data", 0, "field"]
        assert exc.valid_classes == (str, int)
        assert exc.key_type is False
        error_str = str(exc)
        assert "Invalid type" in error_str
        assert "['data'][0]['field']" in error_str


class TestApiValueError:
    """Tests for ApiValueError."""

    def test_api_value_error_basic(self):
        """Test ApiValueError with basic message."""
        exc = ApiValueError("Invalid value")
        assert "Invalid value" in str(exc)
        assert isinstance(exc, ValueError)
        assert isinstance(exc, OpenApiException)

    def test_api_value_error_with_path(self):
        """Test ApiValueError with path_to_item."""
        exc = ApiValueError("Invalid value", path_to_item=["config", "timeout"])
        error_str = str(exc)
        assert "Invalid value" in error_str
        assert "['config']['timeout']" in error_str

    def test_api_value_error_stores_path(self):
        """Test ApiValueError stores path_to_item."""
        path = ["nested", "data", 5]
        exc = ApiValueError("Invalid value", path_to_item=path)
        assert exc.path_to_item == path


class TestApiAttributeError:
    """Tests for ApiAttributeError."""

    def test_api_attribute_error_basic(self):
        """Test ApiAttributeError with basic message."""
        exc = ApiAttributeError("Missing attribute")
        assert "Missing attribute" in str(exc)
        assert isinstance(exc, AttributeError)
        assert isinstance(exc, OpenApiException)

    def test_api_attribute_error_with_path(self):
        """Test ApiAttributeError with path_to_item."""
        exc = ApiAttributeError("Missing attribute", path_to_item=["object", "field"])
        error_str = str(exc)
        assert "Missing attribute" in error_str
        assert "['object']['field']" in error_str

    def test_api_attribute_error_stores_path(self):
        """Test ApiAttributeError stores path_to_item."""
        path = ["a", "b", "c"]
        exc = ApiAttributeError("Missing attribute", path_to_item=path)
        assert exc.path_to_item == path


class TestApiKeyError:
    """Tests for ApiKeyError."""

    def test_api_key_error_basic(self):
        """Test ApiKeyError with basic message."""
        exc = ApiKeyError("Missing key")
        assert "Missing key" in str(exc)
        assert isinstance(exc, KeyError)
        assert isinstance(exc, OpenApiException)

    def test_api_key_error_with_path(self):
        """Test ApiKeyError with path_to_item."""
        exc = ApiKeyError("Missing key", path_to_item=["dict", "required_key"])
        error_str = str(exc)
        assert "Missing key" in error_str
        assert "['dict']['required_key']" in error_str

    def test_api_key_error_stores_path(self):
        """Test ApiKeyError stores path_to_item."""
        path = ["x", "y"]
        exc = ApiKeyError("Missing key", path_to_item=path)
        assert exc.path_to_item == path


class TestApiException:
    """Tests for ApiException."""

    def test_api_exception_basic(self):
        """Test ApiException with status and reason."""
        exc = ApiException(status=404, reason="Not Found")
        assert exc.status == 404
        assert exc.reason == "Not Found"
        assert exc.body is None
        assert exc.data is None
        assert exc.headers is None

    def test_api_exception_with_body(self):
        """Test ApiException with body."""
        exc = ApiException(status=400, reason="Bad Request", body="Invalid input")
        assert exc.body == "Invalid input"

    def test_api_exception_with_data(self):
        """Test ApiException with data."""
        data = {"error": "validation failed"}
        exc = ApiException(status=422, reason="Unprocessable Entity", data=data)
        assert exc.data == data

    def test_api_exception_with_http_resp(self):
        """Test ApiException with http_resp."""
        mock_resp = Mock()
        mock_resp.status = 500
        mock_resp.reason = "Internal Server Error"
        mock_resp.data = b"Server error occurred"
        mock_resp.getheaders = lambda: {"Content-Type": "text/plain"}

        exc = ApiException(http_resp=mock_resp)
        assert exc.status == 500
        assert exc.reason == "Internal Server Error"
        assert exc.body == "Server error occurred"
        assert exc.headers == {"Content-Type": "text/plain"}

    def test_api_exception_http_resp_overrides(self):
        """Test ApiException http_resp doesn't override explicitly set values."""
        mock_resp = Mock()
        mock_resp.status = 500
        mock_resp.reason = "Internal Server Error"
        mock_resp.data = b"Server error"
        mock_resp.getheaders = dict

        exc = ApiException(status=400, reason="Custom", body="Custom body", http_resp=mock_resp)
        # Explicitly set values should not be overridden
        assert exc.status == 400
        assert exc.reason == "Custom"
        assert exc.body == "Custom body"

    def test_api_exception_http_resp_decode_error(self):
        """Test ApiException handles decode errors gracefully."""
        mock_resp = Mock()
        mock_resp.status = 500
        mock_resp.reason = "Internal Server Error"
        mock_resp.data = Mock()
        mock_resp.data.decode = Mock(side_effect=Exception("Decode error"))
        mock_resp.getheaders = dict

        exc = ApiException(http_resp=mock_resp)
        assert exc.body is None  # Should handle decode error gracefully

    def test_api_exception_str(self):
        """Test ApiException string representation."""
        exc = ApiException(status=404, reason="Not Found", body="Resource not found")
        error_str = str(exc)
        assert "(404)" in error_str
        assert "Reason: Not Found" in error_str
        assert "Resource not found" in error_str

    def test_api_exception_str_with_headers(self):
        """Test ApiException string representation with headers."""
        exc = ApiException(
            status=401,
            reason="Unauthorized",
            body="Invalid credentials",
        )
        exc.headers = {"WWW-Authenticate": "Bearer"}
        error_str = str(exc)
        assert "HTTP response headers" in error_str
        assert "WWW-Authenticate" in error_str

    def test_api_exception_str_with_data(self):
        """Test ApiException string representation with data."""
        data = {"error": {"code": "INVALID", "message": "Invalid request"}}
        exc = ApiException(status=400, reason="Bad Request", data=data)
        error_str = str(exc)
        assert "HTTP response body:" in error_str
        assert str(data) in error_str


class TestApiExceptionFromResponse:
    """Tests for ApiException.from_response class method."""

    def test_from_response_400_bad_request(self):
        """Test from_response creates BadRequestException for 400."""
        mock_resp = Mock()
        mock_resp.status = 400
        mock_resp.reason = "Bad Request"
        mock_resp.data = b"Invalid request"
        mock_resp.getheaders = dict

        with pytest.raises(BadRequestException) as exc_info:
            ApiException.from_response(http_resp=mock_resp, body="Invalid request", data=None)
        assert exc_info.value.status == 400

    def test_from_response_401_unauthorized(self):
        """Test from_response creates UnauthorizedException for 401."""
        mock_resp = Mock()
        mock_resp.status = 401
        mock_resp.reason = "Unauthorized"
        mock_resp.data = b"Invalid credentials"
        mock_resp.getheaders = dict

        with pytest.raises(UnauthorizedException) as exc_info:
            ApiException.from_response(http_resp=mock_resp, body="Invalid credentials", data=None)
        assert exc_info.value.status == 401

    def test_from_response_403_forbidden(self):
        """Test from_response creates ForbiddenException for 403."""
        mock_resp = Mock()
        mock_resp.status = 403
        mock_resp.reason = "Forbidden"
        mock_resp.data = b"Access denied"
        mock_resp.getheaders = dict

        with pytest.raises(ForbiddenException) as exc_info:
            ApiException.from_response(http_resp=mock_resp, body="Access denied", data=None)
        assert exc_info.value.status == 403

    def test_from_response_404_not_found(self):
        """Test from_response creates NotFoundException for 404."""
        mock_resp = Mock()
        mock_resp.status = 404
        mock_resp.reason = "Not Found"
        mock_resp.data = b"Resource not found"
        mock_resp.getheaders = dict

        with pytest.raises(NotFoundException) as exc_info:
            ApiException.from_response(http_resp=mock_resp, body="Resource not found", data=None)
        assert exc_info.value.status == 404

    def test_from_response_409_conflict(self):
        """Test from_response creates ConflictException for 409."""
        mock_resp = Mock()
        mock_resp.status = 409
        mock_resp.reason = "Conflict"
        mock_resp.data = b"Resource conflict"
        mock_resp.getheaders = dict

        with pytest.raises(ConflictException) as exc_info:
            ApiException.from_response(http_resp=mock_resp, body="Resource conflict", data=None)
        assert exc_info.value.status == 409

    def test_from_response_422_unprocessable_entity(self):
        """Test from_response creates UnprocessableEntityException for 422."""
        mock_resp = Mock()
        mock_resp.status = 422
        mock_resp.reason = "Unprocessable Entity"
        mock_resp.data = b"Validation failed"
        mock_resp.getheaders = dict

        with pytest.raises(UnprocessableEntityException) as exc_info:
            ApiException.from_response(http_resp=mock_resp, body="Validation failed", data=None)
        assert exc_info.value.status == 422

    def test_from_response_500_service_exception(self):
        """Test from_response creates ServiceException for 500."""
        mock_resp = Mock()
        mock_resp.status = 500
        mock_resp.reason = "Internal Server Error"
        mock_resp.data = b"Server error"
        mock_resp.getheaders = dict

        with pytest.raises(ServiceException) as exc_info:
            ApiException.from_response(http_resp=mock_resp, body="Server error", data=None)
        assert exc_info.value.status == 500

    def test_from_response_503_service_exception(self):
        """Test from_response creates ServiceException for 503."""
        mock_resp = Mock()
        mock_resp.status = 503
        mock_resp.reason = "Service Unavailable"
        mock_resp.data = b"Service down"
        mock_resp.getheaders = dict

        with pytest.raises(ServiceException) as exc_info:
            ApiException.from_response(http_resp=mock_resp, body="Service down", data=None)
        assert exc_info.value.status == 503

    def test_from_response_other_status(self):
        """Test from_response creates generic ApiException for other statuses."""
        mock_resp = Mock()
        mock_resp.status = 418
        mock_resp.reason = "I'm a teapot"
        mock_resp.data = b"Teapot response"
        mock_resp.getheaders = dict

        with pytest.raises(ApiException) as exc_info:
            ApiException.from_response(http_resp=mock_resp, body="Teapot response", data=None)
        assert exc_info.value.status == 418
        # Should be generic ApiException, not a subclass
        assert type(exc_info.value) is ApiException


class TestSpecificExceptions:
    """Tests for specific exception subclasses."""

    def test_bad_request_exception(self):
        """Test BadRequestException."""
        exc = BadRequestException(status=400, reason="Bad Request")
        assert isinstance(exc, ApiException)
        assert exc.status == 400

    def test_not_found_exception(self):
        """Test NotFoundException."""
        exc = NotFoundException(status=404, reason="Not Found")
        assert isinstance(exc, ApiException)
        assert exc.status == 404

    def test_unauthorized_exception(self):
        """Test UnauthorizedException."""
        exc = UnauthorizedException(status=401, reason="Unauthorized")
        assert isinstance(exc, ApiException)
        assert exc.status == 401

    def test_forbidden_exception(self):
        """Test ForbiddenException."""
        exc = ForbiddenException(status=403, reason="Forbidden")
        assert isinstance(exc, ApiException)
        assert exc.status == 403

    def test_service_exception(self):
        """Test ServiceException."""
        exc = ServiceException(status=500, reason="Internal Server Error")
        assert isinstance(exc, ApiException)
        assert exc.status == 500

    def test_conflict_exception(self):
        """Test ConflictException."""
        exc = ConflictException(status=409, reason="Conflict")
        assert isinstance(exc, ApiException)
        assert exc.status == 409

    def test_unprocessable_entity_exception(self):
        """Test UnprocessableEntityException."""
        exc = UnprocessableEntityException(status=422, reason="Unprocessable Entity")
        assert isinstance(exc, ApiException)
        assert exc.status == 422


class TestRenderPath:
    """Tests for render_path helper function."""

    def test_render_path_empty(self):
        """Test render_path with empty list."""
        result = render_path([])
        assert result == ""

    def test_render_path_string_keys(self):
        """Test render_path with string keys."""
        result = render_path(["data", "user", "name"])
        assert result == "['data']['user']['name']"

    def test_render_path_integer_indices(self):
        """Test render_path with integer indices."""
        result = render_path(["items", 0, "id"])
        assert result == "['items'][0]['id']"

    def test_render_path_mixed(self):
        """Test render_path with mixed keys and indices."""
        result = render_path(["results", 5, "data", 2, "value"])
        assert result == "['results'][5]['data'][2]['value']"

    def test_render_path_single_string(self):
        """Test render_path with single string."""
        result = render_path(["field"])
        assert result == "['field']"

    def test_render_path_single_int(self):
        """Test render_path with single integer."""
        result = render_path([0])
        assert result == "[0]"
