
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.admin_project_management_api import AdminProjectManagementApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from ibutsu_client.api.admin_project_management_api import AdminProjectManagementApi
from ibutsu_client.api.admin_user_management_api import AdminUserManagementApi
from ibutsu_client.api.artifact_api import ArtifactApi
from ibutsu_client.api.dashboard_api import DashboardApi
from ibutsu_client.api.group_api import GroupApi
from ibutsu_client.api.health_api import HealthApi
from ibutsu_client.api.import_api import ImportApi
from ibutsu_client.api.login_api import LoginApi
from ibutsu_client.api.project_api import ProjectApi
from ibutsu_client.api.report_api import ReportApi
from ibutsu_client.api.result_api import ResultApi
from ibutsu_client.api.run_api import RunApi
from ibutsu_client.api.task_api import TaskApi
from ibutsu_client.api.user_api import UserApi
from ibutsu_client.api.widget_api import WidgetApi
from ibutsu_client.api.widget_config_api import WidgetConfigApi
