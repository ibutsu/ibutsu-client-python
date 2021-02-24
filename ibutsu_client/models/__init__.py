# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from ibutsu_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from ibutsu_client.model.artifact import Artifact
from ibutsu_client.model.artifact_list import ArtifactList
from ibutsu_client.model.dashboard import Dashboard
from ibutsu_client.model.dashboard_list import DashboardList
from ibutsu_client.model.group import Group
from ibutsu_client.model.group_list import GroupList
from ibutsu_client.model.health import Health
from ibutsu_client.model.health_info import HealthInfo
from ibutsu_client.model.inline_response200 import InlineResponse200
from ibutsu_client.model.model_import import ModelImport
from ibutsu_client.model.pagination import Pagination
from ibutsu_client.model.project import Project
from ibutsu_client.model.project_list import ProjectList
from ibutsu_client.model.report import Report
from ibutsu_client.model.report_list import ReportList
from ibutsu_client.model.report_parameters import ReportParameters
from ibutsu_client.model.result import Result
from ibutsu_client.model.result_list import ResultList
from ibutsu_client.model.run import Run
from ibutsu_client.model.run_list import RunList
from ibutsu_client.model.update_run import UpdateRun
from ibutsu_client.model.widget_config import WidgetConfig
from ibutsu_client.model.widget_config_list import WidgetConfigList
from ibutsu_client.model.widget_param import WidgetParam
from ibutsu_client.model.widget_type import WidgetType
from ibutsu_client.model.widget_type_list import WidgetTypeList
