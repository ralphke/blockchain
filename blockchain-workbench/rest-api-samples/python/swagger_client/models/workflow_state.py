# coding: utf-8

"""
    Azure Blockchain Workbench REST API

    The Azure Blockchain Workbench REST API is a Workbench extensibility point, which allows developers to create and manage blockchain applications, manage users and organizations within a consortium, integrate blockchain applications into services and platforms, perform transactions on a blockchain, and retrieve transactional and contract data from a blockchain.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.workflow_state_transition import WorkflowStateTransition  # noqa: F401,E501


class WorkflowState(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'display_name': 'str',
        'percent_complete': 'int',
        'value': 'int',
        'style': 'str',
        'workflow_state_transitions': 'list[WorkflowStateTransition]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'display_name': 'displayName',
        'percent_complete': 'percentComplete',
        'value': 'value',
        'style': 'style',
        'workflow_state_transitions': 'workflowStateTransitions'
    }

    def __init__(self, id=None, name=None, description=None, display_name=None, percent_complete=None, value=None, style=None, workflow_state_transitions=None):  # noqa: E501
        """WorkflowState - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._display_name = None
        self._percent_complete = None
        self._value = None
        self._style = None
        self._workflow_state_transitions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if value is not None:
            self.value = value
        if style is not None:
            self.style = style
        if workflow_state_transitions is not None:
            self.workflow_state_transitions = workflow_state_transitions

    @property
    def id(self):
        """Gets the id of this WorkflowState.  # noqa: E501


        :return: The id of this WorkflowState.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkflowState.


        :param id: The id of this WorkflowState.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WorkflowState.  # noqa: E501


        :return: The name of this WorkflowState.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowState.


        :param name: The name of this WorkflowState.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this WorkflowState.  # noqa: E501


        :return: The description of this WorkflowState.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowState.


        :param description: The description of this WorkflowState.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this WorkflowState.  # noqa: E501


        :return: The display_name of this WorkflowState.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this WorkflowState.


        :param display_name: The display_name of this WorkflowState.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def percent_complete(self):
        """Gets the percent_complete of this WorkflowState.  # noqa: E501


        :return: The percent_complete of this WorkflowState.  # noqa: E501
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this WorkflowState.


        :param percent_complete: The percent_complete of this WorkflowState.  # noqa: E501
        :type: int
        """

        self._percent_complete = percent_complete

    @property
    def value(self):
        """Gets the value of this WorkflowState.  # noqa: E501


        :return: The value of this WorkflowState.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this WorkflowState.


        :param value: The value of this WorkflowState.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def style(self):
        """Gets the style of this WorkflowState.  # noqa: E501


        :return: The style of this WorkflowState.  # noqa: E501
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this WorkflowState.


        :param style: The style of this WorkflowState.  # noqa: E501
        :type: str
        """

        self._style = style

    @property
    def workflow_state_transitions(self):
        """Gets the workflow_state_transitions of this WorkflowState.  # noqa: E501


        :return: The workflow_state_transitions of this WorkflowState.  # noqa: E501
        :rtype: list[WorkflowStateTransition]
        """
        return self._workflow_state_transitions

    @workflow_state_transitions.setter
    def workflow_state_transitions(self, workflow_state_transitions):
        """Sets the workflow_state_transitions of this WorkflowState.


        :param workflow_state_transitions: The workflow_state_transitions of this WorkflowState.  # noqa: E501
        :type: list[WorkflowStateTransition]
        """

        self._workflow_state_transitions = workflow_state_transitions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, WorkflowState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
