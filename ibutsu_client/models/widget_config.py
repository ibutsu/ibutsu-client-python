# coding: utf-8

"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.10.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ibutsu_client.configuration import Configuration


class WidgetConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'type': 'str',
        'widget': 'str',
        'project': 'str',
        'weight': 'int',
        'params': 'object',
        'title': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'widget': 'widget',
        'project': 'project',
        'weight': 'weight',
        'params': 'params',
        'title': 'title'
    }

    def __init__(self, id=None, type=None, widget=None, project=None, weight=None, params=None, title=None, local_vars_configuration=None):  # noqa: E501
        """WidgetConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._widget = None
        self._project = None
        self._weight = None
        self._params = None
        self._title = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if widget is not None:
            self.widget = widget
        if project is not None:
            self.project = project
        if weight is not None:
            self.weight = weight
        if params is not None:
            self.params = params
        if title is not None:
            self.title = title

    @property
    def id(self):
        """Gets the id of this WidgetConfig.  # noqa: E501

        The internal ID of the WidgetConfig  # noqa: E501

        :return: The id of this WidgetConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WidgetConfig.

        The internal ID of the WidgetConfig  # noqa: E501

        :param id: The id of this WidgetConfig.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this WidgetConfig.  # noqa: E501

        The type of widget, one of either \"widget\" or \"view\"  # noqa: E501

        :return: The type of this WidgetConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WidgetConfig.

        The type of widget, one of either \"widget\" or \"view\"  # noqa: E501

        :param type: The type of this WidgetConfig.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def widget(self):
        """Gets the widget of this WidgetConfig.  # noqa: E501

        The widget to render, from the list at /widget/types  # noqa: E501

        :return: The widget of this WidgetConfig.  # noqa: E501
        :rtype: str
        """
        return self._widget

    @widget.setter
    def widget(self, widget):
        """Sets the widget of this WidgetConfig.

        The widget to render, from the list at /widget/types  # noqa: E501

        :param widget: The widget of this WidgetConfig.  # noqa: E501
        :type: str
        """

        self._widget = widget

    @property
    def project(self):
        """Gets the project of this WidgetConfig.  # noqa: E501

        The project for which the widget is designed  # noqa: E501

        :return: The project of this WidgetConfig.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this WidgetConfig.

        The project for which the widget is designed  # noqa: E501

        :param project: The project of this WidgetConfig.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def weight(self):
        """Gets the weight of this WidgetConfig.  # noqa: E501

        The weighting for the widget, lower weight means it will display first  # noqa: E501

        :return: The weight of this WidgetConfig.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this WidgetConfig.

        The weighting for the widget, lower weight means it will display first  # noqa: E501

        :param weight: The weight of this WidgetConfig.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def params(self):
        """Gets the params of this WidgetConfig.  # noqa: E501

        A dictionary of parameters to send to the widget  # noqa: E501

        :return: The params of this WidgetConfig.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this WidgetConfig.

        A dictionary of parameters to send to the widget  # noqa: E501

        :param params: The params of this WidgetConfig.  # noqa: E501
        :type: object
        """

        self._params = params

    @property
    def title(self):
        """Gets the title of this WidgetConfig.  # noqa: E501

        The title shown on the widget or page  # noqa: E501

        :return: The title of this WidgetConfig.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WidgetConfig.

        The title shown on the widget or page  # noqa: E501

        :param title: The title of this WidgetConfig.  # noqa: E501
        :type: str
        """

        self._title = title

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WidgetConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WidgetConfig):
            return True

        return self.to_dict() != other.to_dict()
