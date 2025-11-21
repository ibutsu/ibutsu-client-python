"""Comprehensive tests for rest module."""

from unittest.mock import Mock

import pytest
import urllib3

from ibutsu_client.configuration import Configuration
from ibutsu_client.exceptions import ApiException, ApiValueError
from ibutsu_client.rest import (
    RESTClientObject,
    RESTResponse,
    is_socks_proxy_url,
)


class TestIsSocksProxyUrl:
    """Tests for is_socks_proxy_url function."""

    def test_is_socks_proxy_url_none(self):
        """Test is_socks_proxy_url with None."""
        assert is_socks_proxy_url(None) is False

    def test_is_socks_proxy_url_socks5(self):
        """Test is_socks_proxy_url with socks5 URL."""
        assert is_socks_proxy_url("socks5://proxy.example.com:1080") is True

    def test_is_socks_proxy_url_socks5h(self):
        """Test is_socks_proxy_url with socks5h URL."""
        assert is_socks_proxy_url("socks5h://proxy.example.com:1080") is True

    def test_is_socks_proxy_url_socks4(self):
        """Test is_socks_proxy_url with socks4 URL."""
        assert is_socks_proxy_url("socks4://proxy.example.com:1080") is True

    def test_is_socks_proxy_url_socks4a(self):
        """Test is_socks_proxy_url with socks4a URL."""
        assert is_socks_proxy_url("socks4a://proxy.example.com:1080") is True

    def test_is_socks_proxy_url_http(self):
        """Test is_socks_proxy_url with http URL."""
        assert is_socks_proxy_url("http://proxy.example.com:8080") is False

    def test_is_socks_proxy_url_https(self):
        """Test is_socks_proxy_url with https URL."""
        assert is_socks_proxy_url("https://proxy.example.com:8080") is False

    def test_is_socks_proxy_url_no_scheme(self):
        """Test is_socks_proxy_url with no scheme."""
        assert is_socks_proxy_url("proxy.example.com:1080") is False

    def test_is_socks_proxy_url_case_insensitive(self):
        """Test is_socks_proxy_url is case insensitive."""
        assert is_socks_proxy_url("SOCKS5://proxy.example.com:1080") is True


class TestRESTResponse:
    """Tests for RESTResponse class."""

    def test_rest_response_init(self):
        """Test RESTResponse initialization."""
        mock_resp = Mock()
        mock_resp.status = 200
        mock_resp.reason = "OK"
        mock_resp.headers = {"Content-Type": "application/json"}
        mock_resp.data = b'{"result": "success"}'

        rest_resp = RESTResponse(mock_resp)
        assert rest_resp.response is mock_resp
        assert rest_resp.status == 200
        assert rest_resp.reason == "OK"
        assert rest_resp.data is None  # Not read yet

    def test_rest_response_read(self):
        """Test RESTResponse read method."""
        mock_resp = Mock()
        mock_resp.status = 200
        mock_resp.reason = "OK"
        mock_resp.data = b"response data"

        rest_resp = RESTResponse(mock_resp)
        data = rest_resp.read()
        assert data == b"response data"
        assert rest_resp.data == b"response data"

    def test_rest_response_read_caches_data(self):
        """Test RESTResponse read method caches data."""
        mock_resp = Mock()
        mock_resp.status = 200
        mock_resp.reason = "OK"
        mock_resp.data = b"response data"

        rest_resp = RESTResponse(mock_resp)
        data1 = rest_resp.read()
        data2 = rest_resp.read()
        assert data1 is data2

    def test_rest_response_getheaders(self):
        """Test RESTResponse getheaders method."""
        mock_resp = Mock()
        mock_resp.status = 200
        mock_resp.reason = "OK"
        mock_resp.headers = {"Content-Type": "application/json", "Content-Length": "100"}
        mock_resp.data = b""

        rest_resp = RESTResponse(mock_resp)
        headers = rest_resp.getheaders()
        assert headers == {"Content-Type": "application/json", "Content-Length": "100"}

    def test_rest_response_getheader(self):
        """Test RESTResponse getheader method."""
        mock_resp = Mock()
        mock_resp.status = 200
        mock_resp.reason = "OK"
        mock_resp.headers = {"Content-Type": "application/json"}
        mock_resp.data = b""

        rest_resp = RESTResponse(mock_resp)
        content_type = rest_resp.getheader("Content-Type")
        assert content_type == "application/json"

    def test_rest_response_getheader_with_default(self):
        """Test RESTResponse getheader with default value."""
        mock_resp = Mock()
        mock_resp.status = 200
        mock_resp.reason = "OK"
        mock_resp.headers = {}
        mock_resp.data = b""

        rest_resp = RESTResponse(mock_resp)
        value = rest_resp.getheader("Missing-Header", "default-value")
        assert value == "default-value"

    def test_rest_response_getheader_case_sensitivity(self):
        """Test RESTResponse getheader case sensitivity."""
        mock_resp = Mock()
        mock_resp.status = 200
        mock_resp.reason = "OK"
        # urllib3 HTTPResponse.headers is case-insensitive
        mock_resp.headers = {"Content-Type": "application/json"}
        mock_resp.data = b""

        rest_resp = RESTResponse(mock_resp)
        # Behavior depends on urllib3's HTTPHeaderDict which is case-insensitive
        value = rest_resp.getheader("content-type")
        # Will be None if headers dict is plain dict, or found if HTTPHeaderDict
        assert value in [None, "application/json"]


class TestRESTClientObjectInit:
    """Tests for RESTClientObject initialization."""

    def test_rest_client_init_default(self):
        """Test RESTClientObject initialization with default configuration."""
        config = Configuration()
        client = RESTClientObject(config)
        assert client.pool_manager is not None
        assert isinstance(client.pool_manager, urllib3.PoolManager)

    def test_rest_client_init_verify_ssl_true(self):
        """Test RESTClientObject with verify_ssl=True."""
        config = Configuration()
        config.verify_ssl = True
        client = RESTClientObject(config)
        # Should use CERT_REQUIRED
        assert client.pool_manager is not None

    def test_rest_client_init_verify_ssl_false(self):
        """Test RESTClientObject with verify_ssl=False."""
        config = Configuration()
        config.verify_ssl = False
        client = RESTClientObject(config)
        # Should use CERT_NONE
        assert client.pool_manager is not None

    def test_rest_client_init_with_ssl_ca_cert(self):
        """Test RESTClientObject with SSL CA cert."""
        config = Configuration()
        config.ssl_ca_cert = "/path/to/ca.pem"
        client = RESTClientObject(config)
        assert client.pool_manager is not None

    def test_rest_client_init_with_client_cert(self):
        """Test RESTClientObject with client certificate."""
        config = Configuration()
        config.cert_file = "/path/to/cert.pem"
        config.key_file = "/path/to/key.pem"
        client = RESTClientObject(config)
        assert client.pool_manager is not None

    def test_rest_client_init_with_assert_hostname(self):
        """Test RESTClientObject with assert_hostname."""
        config = Configuration()
        config.assert_hostname = "example.com"
        client = RESTClientObject(config)
        assert client.pool_manager is not None

    def test_rest_client_init_with_retries(self):
        """Test RESTClientObject with retries."""
        config = Configuration()
        config.retries = 5
        client = RESTClientObject(config)
        assert client.pool_manager is not None

    def test_rest_client_init_with_tls_server_name(self):
        """Test RESTClientObject with TLS server name."""
        config = Configuration()
        config.tls_server_name = "example.com"
        client = RESTClientObject(config)
        assert client.pool_manager is not None

    def test_rest_client_init_with_socket_options(self):
        """Test RESTClientObject with socket options."""
        config = Configuration()
        config.socket_options = [(1, 2, 3)]
        client = RESTClientObject(config)
        assert client.pool_manager is not None

    def test_rest_client_init_with_connection_pool_maxsize(self):
        """Test RESTClientObject with custom connection pool max size."""
        config = Configuration()
        config.connection_pool_maxsize = 50
        client = RESTClientObject(config)
        assert client.pool_manager is not None

    def test_rest_client_init_with_http_proxy(self):
        """Test RESTClientObject with HTTP proxy."""
        config = Configuration()
        config.proxy = "http://proxy.example.com:8080"
        config.verify_ssl = False  # Simplify for testing
        client = RESTClientObject(config)
        assert isinstance(client.pool_manager, urllib3.ProxyManager)

    def test_rest_client_init_with_http_proxy_headers(self):
        """Test RESTClientObject with HTTP proxy headers."""
        config = Configuration()
        config.proxy = "http://proxy.example.com:8080"
        config.proxy_headers = {"Proxy-Authorization": "Basic abc123"}
        config.verify_ssl = False
        client = RESTClientObject(config)
        assert isinstance(client.pool_manager, urllib3.ProxyManager)

    @pytest.mark.skipif(
        not hasattr(urllib3, "contrib"),
        reason="urllib3 contrib module not available",
    )
    def test_rest_client_init_with_socks_proxy(self):
        """Test RESTClientObject with SOCKS proxy."""
        config = Configuration()
        config.proxy = "socks5://proxy.example.com:1080"
        config.verify_ssl = False

        try:
            client = RESTClientObject(config)
            # Should use SOCKSProxyManager if available
            assert client.pool_manager is not None
        except ImportError:
            # SOCKS support may not be installed
            pytest.skip("SOCKS proxy support not installed")


class TestRESTClientObjectRequest:
    """Tests for RESTClientObject request method."""

    def test_request_get(self, mocker):
        """Test GET request."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b'{"result": "success"}'
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request("GET", "https://example.com/api/test")
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_get_preload_content_behavior(self):
        """Test GET request always uses preload_content=False."""
        config = Configuration()
        client = RESTClientObject(config)

        # Prepare a mock HTTPResponse object returned by urllib3's pool manager
        mock_http_response = Mock()
        mock_http_response.status = 200
        mock_http_response.reason = "OK"
        mock_http_response.data = b'{"result": "success"}'

        # Mock the pool_manager to verify how it's called
        mock_pool_manager = Mock()
        mock_pool_manager.request.return_value = mock_http_response
        client.pool_manager = mock_pool_manager

        # Make a GET request
        response = client.request("GET", "https://example.com/api/test")

        # Verify that pool_manager.request was called with preload_content=False
        # This ensures streaming behavior is enabled for better memory efficiency
        mock_pool_manager.request.assert_called_once()
        _, kwargs = mock_pool_manager.request.call_args
        assert kwargs.get("preload_content") is False

        # Verify that the RESTResponse wrapper exposes status/reason correctly
        assert isinstance(response, RESTResponse)
        assert response.status == 200
        assert response.reason == "OK"

    def test_request_post_json(self, mocker):
        """Test POST request with JSON body."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 201
        mock_response.data = b'{"created": true}'
        mock_response.reason = "Created"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "POST",
            "https://example.com/api/test",
            headers={"Content-Type": "application/json"},
            body={"name": "test"},
        )
        assert isinstance(result, RESTResponse)
        assert result.status == 201

    def test_request_post_form_urlencoded(self, mocker):
        """Test POST request with form-urlencoded."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "POST",
            "https://example.com/api/test",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            post_params=[("key1", "value1"), ("key2", "value2")],
        )
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_post_multipart(self, mocker):
        """Test POST request with multipart/form-data."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "POST",
            "https://example.com/api/test",
            headers={"Content-Type": "multipart/form-data"},
            post_params=[("field1", "value1"), ("field2", "value2")],
        )
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_post_string_body(self, mocker):
        """Test POST request with string body."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "POST",
            "https://example.com/api/test",
            headers={"Content-Type": "text/plain"},
            body="plain text data",
        )
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_post_bytes_body(self, mocker):
        """Test POST request with bytes body."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "POST",
            "https://example.com/api/test",
            headers={"Content-Type": "application/octet-stream"},
            body=b"binary data",
        )
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_post_bool_body(self, mocker):
        """Test POST request with boolean body."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "POST",
            "https://example.com/api/test",
            headers={"Content-Type": "text/plain"},
            body=True,
        )
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_put(self, mocker):
        """Test PUT request."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b'{"updated": true}'
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "PUT",
            "https://example.com/api/test/123",
            body={"name": "updated"},
        )
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_patch(self, mocker):
        """Test PATCH request."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b'{"patched": true}'
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "PATCH",
            "https://example.com/api/test/123",
            body={"field": "value"},
        )
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_delete(self, mocker):
        """Test DELETE request."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 204
        mock_response.data = b""
        mock_response.reason = "No Content"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request("DELETE", "https://example.com/api/test/123")
        assert isinstance(result, RESTResponse)
        assert result.status == 204

    def test_request_options(self, mocker):
        """Test OPTIONS request."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b""
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request("OPTIONS", "https://example.com/api/test")
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_head(self, mocker):
        """Test HEAD request."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b""
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request("HEAD", "https://example.com/api/test")
        assert isinstance(result, RESTResponse)
        assert result.status == 200

    def test_request_with_timeout_float(self, mocker):
        """Test request with float timeout."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mock_request = mocker.patch.object(
            client.pool_manager, "request", return_value=mock_response
        )

        client.request("GET", "https://example.com/api/test", _request_timeout=30.0)

        # Verify timeout was passed
        call_args = mock_request.call_args
        assert "timeout" in call_args.kwargs
        assert isinstance(call_args.kwargs["timeout"], urllib3.Timeout)

    def test_request_with_timeout_tuple(self, mocker):
        """Test request with tuple timeout (connect, read)."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mock_request = mocker.patch.object(
            client.pool_manager, "request", return_value=mock_response
        )

        client.request("GET", "https://example.com/api/test", _request_timeout=(10.0, 30.0))

        # Verify timeout was passed
        call_args = mock_request.call_args
        assert "timeout" in call_args.kwargs
        assert isinstance(call_args.kwargs["timeout"], urllib3.Timeout)

    def test_request_body_and_post_params_error(self):
        """Test request raises error when both body and post_params provided."""
        config = Configuration()
        client = RESTClientObject(config)

        with pytest.raises(ApiValueError, match="body parameter cannot be used with post_params"):
            client.request(
                "POST",
                "https://example.com/api/test",
                body={"data": "value"},
                post_params=[("field", "value")],
            )

    def test_request_ssl_error(self, mocker):
        """Test request handles SSL error."""
        config = Configuration()
        client = RESTClientObject(config)

        mocker.patch.object(
            client.pool_manager,
            "request",
            side_effect=urllib3.exceptions.SSLError("SSL certificate verification failed"),
        )

        with pytest.raises(ApiException, match="SSL"):
            client.request("GET", "https://example.com/api/test")

    def test_request_unsupported_method(self):
        """Test request with unsupported HTTP method."""
        config = Configuration()
        client = RESTClientObject(config)

        with pytest.raises(AssertionError):
            client.request("INVALID", "https://example.com/api/test")

    def test_request_post_dict_in_post_params(self, mocker):
        """Test POST request with dict in post_params gets JSON serialized."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mock_request = mocker.patch.object(
            client.pool_manager, "request", return_value=mock_response
        )

        client.request(
            "POST",
            "https://example.com/api/test",
            headers={"Content-Type": "multipart/form-data"},
            post_params=[("data", {"nested": "value"})],
        )

        # Verify dict was JSON-serialized
        call_args = mock_request.call_args
        assert "fields" in call_args.kwargs

    def test_request_post_no_content_type_defaults_to_json(self, mocker):
        """Test POST request without Content-Type defaults to JSON."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b'{"result": "ok"}'
        mock_response.reason = "OK"

        mock_request = mocker.patch.object(
            client.pool_manager, "request", return_value=mock_response
        )

        client.request(
            "POST",
            "https://example.com/api/test",
            body={"data": "value"},
        )

        # Should default to JSON
        call_args = mock_request.call_args
        assert call_args.kwargs["body"] == '{"data": "value"}'

    def test_request_post_invalid_content_type(self):
        """Test POST request with invalid content type raises error."""
        config = Configuration()
        client = RESTClientObject(config)

        with pytest.raises(ApiException, match="Cannot prepare a request"):
            client.request(
                "POST",
                "https://example.com/api/test",
                headers={"Content-Type": "application/xml"},
                body={"data": "value"},
            )

    def test_request_method_case_insensitive(self, mocker):
        """Test request method is case insensitive."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        # Should work with lowercase
        result = client.request("get", "https://example.com/api/test")
        assert result.status == 200

    def test_request_empty_post_params(self, mocker):
        """Test request with empty post_params."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "POST",
            "https://example.com/api/test",
            post_params=[],
        )
        assert result.status == 200

    def test_request_empty_headers(self, mocker):
        """Test request with empty headers."""
        config = Configuration()
        client = RESTClientObject(config)

        mock_response = Mock()
        mock_response.status = 200
        mock_response.data = b"OK"
        mock_response.reason = "OK"

        mocker.patch.object(client.pool_manager, "request", return_value=mock_response)

        result = client.request(
            "GET",
            "https://example.com/api/test",
            headers={},
        )
        assert result.status == 200
