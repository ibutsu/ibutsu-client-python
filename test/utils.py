"""Test data factory functions for ibutsu_client tests."""

import uuid
from typing import Any


def sample_project_data(
    project_id: str | None = None,
    name: str = "test-project",
    title: str = "Test Project",
    owner_id: str | None = None,
    group_id: str | None = None,
) -> dict[str, Any]:
    """Factory function to create sample project data.

    Args:
        project_id: Project UUID (generated if not provided)
        name: Machine name of the project
        title: Human-readable title
        owner_id: Owner UUID
        group_id: Group UUID

    Returns:
        Dictionary with project data
    """
    if project_id is None:
        project_id = str(uuid.uuid4())
    if owner_id is None:
        owner_id = str(uuid.uuid4())
    if group_id is None:
        group_id = str(uuid.uuid4())

    return {
        "id": project_id,
        "name": name,
        "title": title,
        "owner_id": owner_id,
        "group_id": group_id,
    }


def sample_run_data(
    run_id: str | None = None,
    project_id: str | None = None,
    created: str = "2024-01-15T10:00:00",
    start_time: str = "2024-01-15T10:00:00",
    duration: float = 120.5,
    source: str = "pytest",
    component: str = "api",
    env: str = "test",
    summary: dict[str, Any] | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Factory function to create sample test run data.

    Args:
        run_id: Run UUID (generated if not provided)
        project_id: Project UUID (generated if not provided)
        created: ISO timestamp of creation
        start_time: ISO timestamp of run start
        duration: Duration in seconds
        source: Source system identifier
        component: Component under test
        env: Test environment
        summary: Summary statistics
        metadata: Additional metadata

    Returns:
        Dictionary with run data
    """
    if run_id is None:
        run_id = str(uuid.uuid4())
    if project_id is None:
        project_id = str(uuid.uuid4())
    if summary is None:
        summary = {"passed": 10, "failed": 2, "skipped": 1, "errors": 0, "xfailed": 0}
    if metadata is None:
        metadata = {"jenkins_build": "123", "branch": "main"}

    return {
        "id": run_id,
        "project_id": project_id,
        "created": created,
        "start_time": start_time,
        "duration": duration,
        "source": source,
        "component": component,
        "env": env,
        "summary": summary,
        "metadata": metadata,
    }


def sample_result_data(
    result_id: str | None = None,
    run_id: str | None = None,
    project_id: str | None = None,
    test_id: str = "test_example.py::TestClass::test_method",
    start_time: str = "2024-01-15T10:00:00",
    duration: float = 1.5,
    result: str = "passed",
    component: str = "api",
    env: str = "test",
    source: str = "pytest",
    metadata: dict[str, Any] | None = None,
    params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Factory function to create sample test result data.

    Args:
        result_id: Result UUID (generated if not provided)
        run_id: Associated run UUID (generated if not provided)
        project_id: Project UUID (generated if not provided)
        test_id: Test identifier
        start_time: ISO timestamp
        duration: Duration in seconds
        result: Test result status (passed, failed, error, skipped, etc.)
        component: Component under test
        env: Test environment
        source: Source system identifier
        metadata: Additional metadata
        params: Test parameters

    Returns:
        Dictionary with result data
    """
    if result_id is None:
        result_id = str(uuid.uuid4())
    if run_id is None:
        run_id = str(uuid.uuid4())
    if project_id is None:
        project_id = str(uuid.uuid4())
    if metadata is None:
        metadata = {"test_file": "test_example.py", "line_number": 42}
    if params is None:
        params = {}

    return {
        "id": result_id,
        "run_id": run_id,
        "project_id": project_id,
        "test_id": test_id,
        "start_time": start_time,
        "duration": duration,
        "result": result,
        "component": component,
        "env": env,
        "source": source,
        "metadata": metadata,
        "params": params,
    }


def sample_artifact_data(
    artifact_id: str | None = None,
    filename: str = "test_log.txt",
    result_id: str | None = None,
    run_id: str | None = None,
    project_id: str | None = None,
) -> dict[str, Any]:
    """Factory function to create sample artifact data.

    Args:
        artifact_id: Artifact UUID (generated if not provided)
        filename: Artifact filename
        result_id: Associated result UUID
        run_id: Associated run UUID
        project_id: Project UUID

    Returns:
        Dictionary with artifact data
    """
    if artifact_id is None:
        artifact_id = str(uuid.uuid4())
    if result_id is None:
        result_id = str(uuid.uuid4())
    if run_id is None:
        run_id = str(uuid.uuid4())
    if project_id is None:
        project_id = str(uuid.uuid4())

    return {
        "id": artifact_id,
        "filename": filename,
        "result_id": result_id,
        "run_id": run_id,
        "project_id": project_id,
    }


def sample_pagination_data(
    page: int = 1,
    page_size: int = 25,
    total_items: int = 100,
    total_pages: int = 4,
) -> dict[str, Any]:
    """Factory function to create sample pagination data.

    Args:
        page: Current page number
        page_size: Number of items per page
        total_items: Total number of items
        total_pages: Total number of pages

    Returns:
        Dictionary with pagination data
    """
    return {
        "page": page,
        "pageSize": page_size,
        "totalItems": total_items,
        "totalPages": total_pages,
    }


def sample_user_data(
    user_id: str | None = None,
    email: str = "test@example.com",
    name: str = "Test User",
    is_superadmin: bool = False,
    is_active: bool = True,
) -> dict[str, Any]:
    """Factory function to create sample user data.

    Args:
        user_id: User UUID (generated if not provided)
        email: User email address
        name: User full name
        is_superadmin: Whether user is a superadmin
        is_active: Whether user account is active

    Returns:
        Dictionary with user data
    """
    if user_id is None:
        user_id = str(uuid.uuid4())

    return {
        "id": user_id,
        "email": email,
        "name": name,
        "is_superadmin": is_superadmin,
        "is_active": is_active,
    }


def sample_dashboard_data(
    dashboard_id: str | None = None,
    title: str = "Test Dashboard",
    project_id: str | None = None,
    description: str | None = None,
    filters: str | None = None,
) -> dict[str, Any]:
    """Factory function to create sample dashboard data.

    Args:
        dashboard_id: Dashboard UUID (generated if not provided)
        title: Dashboard title
        project_id: Project UUID (generated if not provided)
        description: Dashboard description
        filters: Dashboard filters

    Returns:
        Dictionary with dashboard data
    """
    if dashboard_id is None:
        dashboard_id = str(uuid.uuid4())
    if project_id is None:
        project_id = str(uuid.uuid4())

    data = {
        "id": dashboard_id,
        "title": title,
        "project_id": project_id,
    }
    if description is not None:
        data["description"] = description
    if filters is not None:
        data["filters"] = filters

    return data


def sample_widget_config_data(
    widget_id: str | None = None,
    widget: str = "result-summary",
    config_type: str = "widget",
    weight: int = 0,
    params: dict[str, Any] | None = None,
    title: str | None = None,
) -> dict[str, Any]:
    """Factory function to create sample widget configuration data.

    Args:
        widget_id: Widget UUID (generated if not provided)
        widget: Widget name to render
        config_type: Type of config ("widget" or "view")
        weight: Widget display weight/order
        params: Widget parameters
        title: Widget title

    Returns:
        Dictionary with widget config data
    """
    if widget_id is None:
        widget_id = str(uuid.uuid4())
    if params is None:
        params = {}

    return {
        "id": widget_id,
        "type": config_type,
        "widget": widget,
        "weight": weight,
        "params": params,
        "title": title,
    }


def sample_group_data(
    group_id: str | None = None,
    name: str = "test-group",
) -> dict[str, Any]:
    """Factory function to create sample group data.

    Args:
        group_id: Group UUID (generated if not provided)
        name: Group name

    Returns:
        Dictionary with group data
    """
    if group_id is None:
        group_id = str(uuid.uuid4())

    return {
        "id": group_id,
        "name": name,
    }


def sample_token_data(
    token_id: str | None = None,
    user_id: str | None = None,
    name: str = "test-token",
    token: str = "test-token-value",
    expires: str | None = "2025-12-31",
) -> dict[str, Any]:
    """Factory function to create sample token data.

    Args:
        token_id: Token UUID (generated if not provided)
        user_id: User UUID (generated if not provided)
        name: Token name/identifier
        token: The actual token string
        expires: Expiration date

    Returns:
        Dictionary with token data
    """
    if token_id is None:
        token_id = str(uuid.uuid4())
    if user_id is None:
        user_id = str(uuid.uuid4())

    return {
        "id": token_id,
        "user_id": user_id,
        "name": name,
        "token": token,
        "expires": expires,
    }
