# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class ScheduledPlan(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScheduledPlan - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'title': 'str',
            'user': 'UserPublic',
            'enabled': 'bool',
            'last_run_at': 'datetime',
            'next_run_at': 'datetime',
            'look_id': 'int',
            'dashboard_id': 'int',
            'lookml_dashboard_id': 'str',
            'require_results': 'bool',
            'require_no_results': 'bool',
            'require_change': 'bool',
            'crontab': 'str',
            'timezone': 'str',
            'scheduled_plan_destination': 'list[ScheduledPlanDestination]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'title': 'title',
            'user': 'user',
            'enabled': 'enabled',
            'last_run_at': 'last_run_at',
            'next_run_at': 'next_run_at',
            'look_id': 'look_id',
            'dashboard_id': 'dashboard_id',
            'lookml_dashboard_id': 'lookml_dashboard_id',
            'require_results': 'require_results',
            'require_no_results': 'require_no_results',
            'require_change': 'require_change',
            'crontab': 'crontab',
            'timezone': 'timezone',
            'scheduled_plan_destination': 'scheduled_plan_destination'
        }

        self._id = None
        self._name = None
        self._title = None
        self._user = None
        self._enabled = None
        self._last_run_at = None
        self._next_run_at = None
        self._look_id = None
        self._dashboard_id = None
        self._lookml_dashboard_id = None
        self._require_results = None
        self._require_no_results = None
        self._require_change = None
        self._crontab = None
        self._timezone = None
        self._scheduled_plan_destination = None

    @property
    def id(self):
        """
        Gets the id of this ScheduledPlan.
        Unique Id

        :return: The id of this ScheduledPlan.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledPlan.
        Unique Id

        :param id: The id of this ScheduledPlan.
        :type: int
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ScheduledPlan.
        Name

        :return: The name of this ScheduledPlan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ScheduledPlan.
        Name

        :param name: The name of this ScheduledPlan.
        :type: str
        """
        
        self._name = name

    @property
    def title(self):
        """
        Gets the title of this ScheduledPlan.
        Title

        :return: The title of this ScheduledPlan.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ScheduledPlan.
        Title

        :param title: The title of this ScheduledPlan.
        :type: str
        """
        
        self._title = title

    @property
    def user(self):
        """
        Gets the user of this ScheduledPlan.
        User who owns this ScheduledPlan

        :return: The user of this ScheduledPlan.
        :rtype: UserPublic
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this ScheduledPlan.
        User who owns this ScheduledPlan

        :param user: The user of this ScheduledPlan.
        :type: UserPublic
        """
        
        self._user = user

    @property
    def enabled(self):
        """
        Gets the enabled of this ScheduledPlan.
        Whether the ScheduledPlan is enabled

        :return: The enabled of this ScheduledPlan.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ScheduledPlan.
        Whether the ScheduledPlan is enabled

        :param enabled: The enabled of this ScheduledPlan.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def last_run_at(self):
        """
        Gets the last_run_at of this ScheduledPlan.
        When the ScheduledPlan was last run

        :return: The last_run_at of this ScheduledPlan.
        :rtype: datetime
        """
        return self._last_run_at

    @last_run_at.setter
    def last_run_at(self, last_run_at):
        """
        Sets the last_run_at of this ScheduledPlan.
        When the ScheduledPlan was last run

        :param last_run_at: The last_run_at of this ScheduledPlan.
        :type: datetime
        """
        
        self._last_run_at = last_run_at

    @property
    def next_run_at(self):
        """
        Gets the next_run_at of this ScheduledPlan.
        When the ScheduledPlan will next run

        :return: The next_run_at of this ScheduledPlan.
        :rtype: datetime
        """
        return self._next_run_at

    @next_run_at.setter
    def next_run_at(self, next_run_at):
        """
        Sets the next_run_at of this ScheduledPlan.
        When the ScheduledPlan will next run

        :param next_run_at: The next_run_at of this ScheduledPlan.
        :type: datetime
        """
        
        self._next_run_at = next_run_at

    @property
    def look_id(self):
        """
        Gets the look_id of this ScheduledPlan.
        Id of a look

        :return: The look_id of this ScheduledPlan.
        :rtype: int
        """
        return self._look_id

    @look_id.setter
    def look_id(self, look_id):
        """
        Sets the look_id of this ScheduledPlan.
        Id of a look

        :param look_id: The look_id of this ScheduledPlan.
        :type: int
        """
        
        self._look_id = look_id

    @property
    def dashboard_id(self):
        """
        Gets the dashboard_id of this ScheduledPlan.
        Id of a dashboard

        :return: The dashboard_id of this ScheduledPlan.
        :rtype: int
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """
        Sets the dashboard_id of this ScheduledPlan.
        Id of a dashboard

        :param dashboard_id: The dashboard_id of this ScheduledPlan.
        :type: int
        """
        
        self._dashboard_id = dashboard_id

    @property
    def lookml_dashboard_id(self):
        """
        Gets the lookml_dashboard_id of this ScheduledPlan.
        Id of a LookML dashboard

        :return: The lookml_dashboard_id of this ScheduledPlan.
        :rtype: str
        """
        return self._lookml_dashboard_id

    @lookml_dashboard_id.setter
    def lookml_dashboard_id(self, lookml_dashboard_id):
        """
        Sets the lookml_dashboard_id of this ScheduledPlan.
        Id of a LookML dashboard

        :param lookml_dashboard_id: The lookml_dashboard_id of this ScheduledPlan.
        :type: str
        """
        
        self._lookml_dashboard_id = lookml_dashboard_id

    @property
    def require_results(self):
        """
        Gets the require_results of this ScheduledPlan.
        Delivery should occur if running the dashboard or look returns results

        :return: The require_results of this ScheduledPlan.
        :rtype: bool
        """
        return self._require_results

    @require_results.setter
    def require_results(self, require_results):
        """
        Sets the require_results of this ScheduledPlan.
        Delivery should occur if running the dashboard or look returns results

        :param require_results: The require_results of this ScheduledPlan.
        :type: bool
        """
        
        self._require_results = require_results

    @property
    def require_no_results(self):
        """
        Gets the require_no_results of this ScheduledPlan.
        Delivery should occur if the dashboard look does not return results

        :return: The require_no_results of this ScheduledPlan.
        :rtype: bool
        """
        return self._require_no_results

    @require_no_results.setter
    def require_no_results(self, require_no_results):
        """
        Sets the require_no_results of this ScheduledPlan.
        Delivery should occur if the dashboard look does not return results

        :param require_no_results: The require_no_results of this ScheduledPlan.
        :type: bool
        """
        
        self._require_no_results = require_no_results

    @property
    def require_change(self):
        """
        Gets the require_change of this ScheduledPlan.
        Delivery should occur if data have changed since the last run

        :return: The require_change of this ScheduledPlan.
        :rtype: bool
        """
        return self._require_change

    @require_change.setter
    def require_change(self, require_change):
        """
        Sets the require_change of this ScheduledPlan.
        Delivery should occur if data have changed since the last run

        :param require_change: The require_change of this ScheduledPlan.
        :type: bool
        """
        
        self._require_change = require_change

    @property
    def crontab(self):
        """
        Gets the crontab of this ScheduledPlan.
        Vixie-Style crontab specification when to run

        :return: The crontab of this ScheduledPlan.
        :rtype: str
        """
        return self._crontab

    @crontab.setter
    def crontab(self, crontab):
        """
        Sets the crontab of this ScheduledPlan.
        Vixie-Style crontab specification when to run

        :param crontab: The crontab of this ScheduledPlan.
        :type: str
        """
        
        self._crontab = crontab

    @property
    def timezone(self):
        """
        Gets the timezone of this ScheduledPlan.
        Timezone for interpreting the specified crontab (default is Looker instance timezone)

        :return: The timezone of this ScheduledPlan.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ScheduledPlan.
        Timezone for interpreting the specified crontab (default is Looker instance timezone)

        :param timezone: The timezone of this ScheduledPlan.
        :type: str
        """
        
        self._timezone = timezone

    @property
    def scheduled_plan_destination(self):
        """
        Gets the scheduled_plan_destination of this ScheduledPlan.
        Scheduled plan destinations

        :return: The scheduled_plan_destination of this ScheduledPlan.
        :rtype: list[ScheduledPlanDestination]
        """
        return self._scheduled_plan_destination

    @scheduled_plan_destination.setter
    def scheduled_plan_destination(self, scheduled_plan_destination):
        """
        Sets the scheduled_plan_destination of this ScheduledPlan.
        Scheduled plan destinations

        :param scheduled_plan_destination: The scheduled_plan_destination of this ScheduledPlan.
        :type: list[ScheduledPlanDestination]
        """
        
        self._scheduled_plan_destination = scheduled_plan_destination

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

