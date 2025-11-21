"""Comprehensive tests for Configuration."""

import copy
import logging
import sys

import pytest

from ibutsu_client.configuration import Configuration


class TestConfigurationInit:
    """Tests for Configuration initialization."""

    def test_init_default(self):
        """Test initialization with default values."""
        config = Configuration()
        assert config.host == "/api"
        assert config.server_index == 0
        assert config.temp_folder_path is None
        assert config.verify_ssl is True
        assert config.client_side_validation is True
        assert config.api_key == {}
        assert config.api_key_prefix == {}

    def test_init_with_host(self):
        """Test initialization with custom host."""
        config = Configuration(host="https://example.com")
        assert config.host == "https://example.com"
        assert config.server_index is None

    def test_init_with_api_key(self):
        """Test initialization with API key."""
        api_key = {"jwt": "test-token"}
        config = Configuration(api_key=api_key)
        assert config.api_key == api_key

    def test_init_with_api_key_prefix(self):
        """Test initialization with API key prefix."""
        api_key_prefix = {"jwt": "Bearer"}
        config = Configuration(api_key_prefix=api_key_prefix)
        assert config.api_key_prefix == api_key_prefix

    def test_init_with_basic_auth(self):
        """Test initialization with basic auth credentials."""
        config = Configuration(username="user", password="pass")
        assert config.username == "user"
        assert config.password == "pass"

    def test_init_with_access_token(self):
        """Test initialization with access token."""
        config = Configuration(access_token="test-token")
        assert config.access_token == "test-token"

    def test_init_with_server_index(self):
        """Test initialization with server index."""
        config = Configuration(server_index=1)
        assert config.server_index == 1

    def test_init_with_server_variables(self):
        """Test initialization with server variables."""
        variables = {"env": "production"}
        config = Configuration(server_variables=variables)
        assert config.server_variables == variables

    def test_init_with_server_operation_index(self):
        """Test initialization with server operation index."""
        operation_index = {1: 0, 2: 1}
        config = Configuration(server_operation_index=operation_index)
        assert config.server_operation_index == operation_index

    def test_init_with_server_operation_variables(self):
        """Test initialization with server operation variables."""
        operation_variables = {1: {"env": "prod"}}
        config = Configuration(server_operation_variables=operation_variables)
        assert config.server_operation_variables == operation_variables

    def test_init_with_ignore_operation_servers(self):
        """Test initialization with ignore_operation_servers."""
        config = Configuration(ignore_operation_servers=True)
        assert config.ignore_operation_servers is True

    def test_init_with_ssl_ca_cert(self):
        """Test initialization with SSL CA certificate."""
        config = Configuration(ssl_ca_cert="/path/to/cert.pem")
        assert config.ssl_ca_cert == "/path/to/cert.pem"

    def test_init_with_retries(self):
        """Test initialization with retries."""
        config = Configuration(retries=5)
        assert config.retries == 5

    def test_init_with_ca_cert_data(self):
        """Test initialization with CA cert data."""
        cert_data = "-----BEGIN CERTIFICATE-----\ntest\n-----END CERTIFICATE-----"
        config = Configuration(ca_cert_data=cert_data)
        assert config.ca_cert_data == cert_data

    def test_init_with_debug(self):
        """Test initialization with debug mode."""
        config = Configuration(debug=True)
        assert config.debug is True

    def test_init_without_debug(self):
        """Test initialization without debug mode specified."""
        config = Configuration()
        assert config.debug is False


class TestConfigurationDefaultInstance:
    """Tests for Configuration default instance management."""

    def test_get_default_creates_new_instance(self):
        """Test get_default creates a new instance if none exists."""
        Configuration._default = None
        default = Configuration.get_default()
        assert default is not None
        assert isinstance(default, Configuration)

    def test_get_default_returns_same_instance(self):
        """Test get_default returns the same instance."""
        Configuration._default = None
        default1 = Configuration.get_default()
        default2 = Configuration.get_default()
        assert default1 is default2

    def test_set_default(self):
        """Test setting custom default instance."""
        custom_config = Configuration(host="https://custom.com")
        Configuration.set_default(custom_config)
        default = Configuration.get_default()
        assert default is custom_config
        assert default.host == "https://custom.com"

    def test_get_default_copy_deprecated(self):
        """Test get_default_copy returns same as get_default."""
        Configuration._default = None
        default = Configuration.get_default_copy()
        assert default is Configuration.get_default()


class TestConfigurationLoggerProperties:
    """Tests for Configuration logger properties."""

    @staticmethod
    def _assert_all_loggers_have_level(config, expected_level):
        """Helper to assert all loggers have the expected level."""
        logger_levels = [logger.level for logger in config.logger.values()]
        assert all(level == expected_level for level in logger_levels), (
            f"Not all loggers have expected level {expected_level}. Found levels: {logger_levels}"
        )

    def test_logger_file_getter(self):
        """Test logger_file getter."""
        config = Configuration()
        assert config.logger_file is None

    def test_logger_file_setter(self, tmp_path):
        """Test logger_file setter."""
        config = Configuration()
        log_file = tmp_path / "test.log"
        config.logger_file = str(log_file)
        assert config.logger_file == str(log_file)
        assert config.logger_file_handler is not None

    def test_debug_getter(self):
        """Test debug getter."""
        config = Configuration()
        assert config.debug is False

    def test_debug_setter_true(self):
        """Test debug setter to True."""
        config = Configuration()
        config.debug = True
        assert config.debug
        # Check logger levels
        self._assert_all_loggers_have_level(config, logging.DEBUG)

    def test_debug_setter_false(self):
        """Test debug setter to False."""
        config = Configuration()
        config.debug = False
        assert not config.debug
        # Check logger levels
        self._assert_all_loggers_have_level(config, logging.WARNING)

    def test_logger_format_getter(self):
        """Test logger_format getter."""
        config = Configuration()
        assert config.logger_format == "%(asctime)s %(levelname)s %(message)s"

    def test_logger_format_setter(self):
        """Test logger_format setter."""
        config = Configuration()
        new_format = "%(levelname)s - %(message)s"
        config.logger_format = new_format
        assert config.logger_format == new_format
        assert config.logger_formatter._fmt == new_format


class TestConfigurationHostSettings:
    """Tests for Configuration host settings."""

    def test_get_host_settings(self):
        """Test get_host_settings returns default settings."""
        config = Configuration()
        settings = config.get_host_settings()
        assert len(settings) == 1
        assert settings[0]["url"] == "/api"
        assert "description" in settings[0]

    def test_get_host_from_settings_with_none_index(self):
        """Test get_host_from_settings with None index."""
        config = Configuration(host="https://example.com")
        result = config.get_host_from_settings(None)
        assert result == "https://example.com"

    def test_get_host_from_settings_with_index(self):
        """Test get_host_from_settings with valid index."""
        config = Configuration()
        result = config.get_host_from_settings(0)
        assert result == "/api"

    def test_get_host_from_settings_invalid_index(self):
        """Test get_host_from_settings with invalid index."""
        config = Configuration()
        with pytest.raises(ValueError, match="Invalid index"):
            config.get_host_from_settings(10)

    def test_get_host_from_settings_with_variables(self):
        """Test get_host_from_settings with variable substitution."""
        config = Configuration()
        servers = [
            {
                "url": "https://{env}.example.com",
                "description": "Test server",
                "variables": {
                    "env": {
                        "description": "Environment",
                        "default_value": "dev",
                        "enum_values": ["dev", "staging", "prod"],
                    }
                },
            }
        ]
        result = config.get_host_from_settings(0, variables={"env": "prod"}, servers=servers)
        assert result == "https://prod.example.com"

    def test_get_host_from_settings_with_default_variable(self):
        """Test get_host_from_settings uses default variable value."""
        config = Configuration()
        servers = [
            {
                "url": "https://{env}.example.com",
                "description": "Test server",
                "variables": {
                    "env": {
                        "description": "Environment",
                        "default_value": "dev",
                        "enum_values": ["dev", "staging", "prod"],
                    }
                },
            }
        ]
        result = config.get_host_from_settings(0, servers=servers)
        assert result == "https://dev.example.com"

    def test_get_host_from_settings_invalid_enum_value(self):
        """Test get_host_from_settings with invalid enum value."""
        config = Configuration()
        servers = [
            {
                "url": "https://{env}.example.com",
                "description": "Test server",
                "variables": {
                    "env": {
                        "description": "Environment",
                        "default_value": "dev",
                        "enum_values": ["dev", "staging", "prod"],
                    }
                },
            }
        ]
        with pytest.raises(ValueError, match="invalid value"):
            config.get_host_from_settings(0, variables={"env": "invalid"}, servers=servers)

    def test_host_property_getter(self):
        """Test host property getter."""
        config = Configuration()
        assert config.host == "/api"

    def test_host_property_setter(self):
        """Test host property setter."""
        config = Configuration()
        config.host = "https://new-host.com"
        assert config.host == "https://new-host.com"
        assert config.server_index is None


class TestConfigurationAuth:
    """Tests for Configuration authentication methods."""

    def test_get_api_key_with_prefix_no_key(self):
        """Test get_api_key_with_prefix with no key set."""
        config = Configuration()
        result = config.get_api_key_with_prefix("jwt")
        assert result is None

    def test_get_api_key_with_prefix_key_only(self):
        """Test get_api_key_with_prefix with key but no prefix."""
        config = Configuration(api_key={"jwt": "test-token"})
        result = config.get_api_key_with_prefix("jwt")
        assert result == "test-token"

    def test_get_api_key_with_prefix_key_and_prefix(self):
        """Test get_api_key_with_prefix with key and prefix."""
        config = Configuration(
            api_key={"jwt": "test-token"},
            api_key_prefix={"jwt": "Bearer"},
        )
        result = config.get_api_key_with_prefix("jwt")
        assert result == "Bearer test-token"

    def test_get_api_key_with_prefix_with_alias(self):
        """Test get_api_key_with_prefix with alias."""
        config = Configuration(api_key={"alt_key": "test-token"})
        result = config.get_api_key_with_prefix("jwt", alias="alt_key")
        assert result == "test-token"

    def test_get_api_key_with_prefix_refresh_hook(self):
        """Test get_api_key_with_prefix calls refresh hook."""
        config = Configuration()
        hook_called = []

        def refresh_hook(cfg):
            hook_called.append(True)
            cfg.api_key["jwt"] = "refreshed-token"

        config.refresh_api_key_hook = refresh_hook
        result = config.get_api_key_with_prefix("jwt")
        assert len(hook_called) == 1
        assert result == "refreshed-token"

    def test_get_basic_auth_token_none(self):
        """Test get_basic_auth_token with no credentials."""
        config = Configuration()
        token = config.get_basic_auth_token()
        # Should return authorization header even with empty credentials
        assert token is not None
        assert "Basic" in token

    def test_get_basic_auth_token_with_credentials(self):
        """Test get_basic_auth_token with credentials."""
        config = Configuration(username="user", password="pass")
        token = config.get_basic_auth_token()
        assert token is not None
        assert "Basic" in token

    def test_get_basic_auth_token_username_only(self):
        """Test get_basic_auth_token with username only."""
        config = Configuration(username="user")
        token = config.get_basic_auth_token()
        assert token is not None
        assert "Basic" in token

    def test_auth_settings_no_token(self):
        """Test auth_settings with no access token."""
        config = Configuration()
        settings = config.auth_settings()
        assert settings == {}

    def test_auth_settings_with_access_token(self):
        """Test auth_settings with access token."""
        config = Configuration(access_token="test-token")
        settings = config.auth_settings()
        assert "jwt" in settings
        assert settings["jwt"]["type"] == "bearer"
        assert settings["jwt"]["in"] == "header"
        assert settings["jwt"]["format"] == "JWT"
        assert settings["jwt"]["key"] == "Authorization"
        assert settings["jwt"]["value"] == "Bearer test-token"


class TestConfigurationDeepCopy:
    """Tests for Configuration deep copy."""

    def test_deepcopy(self):
        """Test deepcopy creates independent copy."""
        config = Configuration(
            host="https://example.com",
            api_key={"jwt": "test-token"},
            username="user",
            password="pass",
        )
        config_copy = copy.deepcopy(config)

        # Verify it's a copy
        assert config_copy is not config
        assert config_copy.host == config.host
        assert config_copy.api_key == config.api_key
        assert config_copy.username == config.username

        # Modify copy and verify original is unchanged
        config_copy.host = "https://other.com"
        assert config.host == "https://example.com"
        assert config_copy.host == "https://other.com"

    def test_deepcopy_excludes_logger(self):
        """Test deepcopy handles logger correctly."""
        config = Configuration()
        config_copy = copy.deepcopy(config)

        # Loggers should be shallow copied
        assert config_copy.logger is not None
        assert "package_logger" in config_copy.logger


class TestConfigurationDebugReport:
    """Tests for Configuration debug report."""

    def test_to_debug_report(self):
        """Test to_debug_report generates report."""
        config = Configuration()
        report = config.to_debug_report()
        assert "Python SDK Debug Report" in report
        assert "OS:" in report
        assert "Python Version:" in report
        assert "Version of the API:" in report
        assert "SDK Package Version:" in report
        assert sys.platform in report


class TestConfigurationSSLSettings:
    """Tests for Configuration SSL settings."""

    def test_verify_ssl_default(self):
        """Test verify_ssl default value."""
        config = Configuration()
        assert config.verify_ssl is True

    def test_ssl_ca_cert(self):
        """Test ssl_ca_cert setting."""
        config = Configuration(ssl_ca_cert="/path/to/cert.pem")
        assert config.ssl_ca_cert == "/path/to/cert.pem"

    def test_ca_cert_data_str(self):
        """Test ca_cert_data with string."""
        cert_data = "-----BEGIN CERTIFICATE-----\ntest\n-----END CERTIFICATE-----"
        config = Configuration(ca_cert_data=cert_data)
        assert config.ca_cert_data == cert_data

    def test_ca_cert_data_bytes(self):
        """Test ca_cert_data with bytes."""
        cert_data = b"-----BEGIN CERTIFICATE-----\ntest\n-----END CERTIFICATE-----"
        config = Configuration(ca_cert_data=cert_data)
        assert config.ca_cert_data == cert_data

    def test_cert_file(self):
        """Test cert_file setting."""
        config = Configuration()
        config.cert_file = "/path/to/cert.pem"
        assert config.cert_file == "/path/to/cert.pem"

    def test_key_file(self):
        """Test key_file setting."""
        config = Configuration()
        config.key_file = "/path/to/key.pem"
        assert config.key_file == "/path/to/key.pem"

    def test_assert_hostname(self):
        """Test assert_hostname setting."""
        config = Configuration()
        config.assert_hostname = True
        assert config.assert_hostname

    def test_tls_server_name(self):
        """Test tls_server_name setting."""
        config = Configuration()
        config.tls_server_name = "example.com"
        assert config.tls_server_name == "example.com"


class TestConfigurationConnectionSettings:
    """Tests for Configuration connection settings."""

    def test_connection_pool_maxsize_default(self):
        """Test connection_pool_maxsize default value."""
        config = Configuration()
        # Should be cpu_count * 5
        assert config.connection_pool_maxsize > 0

    def test_proxy(self):
        """Test proxy setting."""
        config = Configuration()
        config.proxy = "http://proxy.example.com:8080"
        assert config.proxy == "http://proxy.example.com:8080"

    def test_proxy_headers(self):
        """Test proxy_headers setting."""
        config = Configuration()
        headers = {"Proxy-Authorization": "Basic abc123"}
        config.proxy_headers = headers
        assert config.proxy_headers == headers

    def test_safe_chars_for_path_param(self):
        """Test safe_chars_for_path_param setting."""
        config = Configuration()
        assert config.safe_chars_for_path_param == ""
        config.safe_chars_for_path_param = "/-_.~"
        assert config.safe_chars_for_path_param == "/-_.~"

    def test_retries(self):
        """Test retries setting."""
        config = Configuration(retries=3)
        assert config.retries == 3

    def test_socket_options(self):
        """Test socket_options setting."""
        config = Configuration()
        assert config.socket_options is None
        options = [(1, 2, 3)]
        config.socket_options = options
        assert config.socket_options == options


class TestConfigurationDateTimeFormats:
    """Tests for Configuration date/time format settings."""

    def test_datetime_format_default(self):
        """Test datetime_format default value."""
        config = Configuration()
        assert config.datetime_format == "%Y-%m-%dT%H:%M:%S.%f%z"

    def test_datetime_format_custom(self):
        """Test setting custom datetime_format."""
        config = Configuration()
        config.datetime_format = "%Y-%m-%d %H:%M:%S"
        assert config.datetime_format == "%Y-%m-%d %H:%M:%S"

    def test_date_format_default(self):
        """Test date_format default value."""
        config = Configuration()
        assert config.date_format == "%Y-%m-%d"

    def test_date_format_custom(self):
        """Test setting custom date_format."""
        config = Configuration()
        config.date_format = "%d/%m/%Y"
        assert config.date_format == "%d/%m/%Y"


class TestConfigurationValidation:
    """Tests for Configuration client-side validation."""

    def test_client_side_validation_default(self):
        """Test client_side_validation default value."""
        config = Configuration()
        assert config.client_side_validation is True

    def test_client_side_validation_disabled(self):
        """Test disabling client_side_validation."""
        config = Configuration()
        config.client_side_validation = False
        assert not config.client_side_validation


class TestConfigurationTempFolder:
    """Tests for Configuration temp folder."""

    def test_temp_folder_path_default(self):
        """Test temp_folder_path default value."""
        config = Configuration()
        assert config.temp_folder_path is None

    def test_temp_folder_path_custom(self):
        """Test setting custom temp_folder_path."""
        config = Configuration()
        config.temp_folder_path = "/tmp/custom"
        assert config.temp_folder_path == "/tmp/custom"
