# coding: utf-8

"""
    Trend Micro Deep Security API

    Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 11.3.184
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class PolicyLogInspectionRuleDetailsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def describe_log_inspection_rule_on_policy(self, policy_id, log_inspection_rule_id, api_version, **kwargs):  # noqa: E501
        """Describe an log inspection rule  # noqa: E501

        Describe an log inspection rule including policy-level overrides.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_log_inspection_rule_on_policy(policy_id, log_inspection_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int log_inspection_rule_id: The ID number of the log inspection rule. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: LogInspectionRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_log_inspection_rule_on_policy_with_http_info(policy_id, log_inspection_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_log_inspection_rule_on_policy_with_http_info(policy_id, log_inspection_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_log_inspection_rule_on_policy_with_http_info(self, policy_id, log_inspection_rule_id, api_version, **kwargs):  # noqa: E501
        """Describe an log inspection rule  # noqa: E501

        Describe an log inspection rule including policy-level overrides.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_log_inspection_rule_on_policy_with_http_info(policy_id, log_inspection_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int log_inspection_rule_id: The ID number of the log inspection rule. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: LogInspectionRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'log_inspection_rule_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_log_inspection_rule_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `describe_log_inspection_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'log_inspection_rule_id' is set
        if ('log_inspection_rule_id' not in params or
                params['log_inspection_rule_id'] is None):
            raise ValueError("Missing the required parameter `log_inspection_rule_id` when calling `describe_log_inspection_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_log_inspection_rule_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `describe_log_inspection_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'log_inspection_rule_id' in params and not re.search('\\d+', str(params['log_inspection_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `log_inspection_rule_id` when calling `describe_log_inspection_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'log_inspection_rule_id' in params:
            path_params['logInspectionRuleID'] = params['log_inspection_rule_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/loginspection/rules/{logInspectionRuleID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogInspectionRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_log_inspection_rules_on_policy(self, policy_id, api_version, **kwargs):  # noqa: E501
        """List log inspection rules  # noqa: E501

        Lists all log inspection rules assigned to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_log_inspection_rules_on_policy(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only rules assigned to the current policy.
        :return: LogInspectionRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_log_inspection_rules_on_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_log_inspection_rules_on_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
            return data

    def list_log_inspection_rules_on_policy_with_http_info(self, policy_id, api_version, **kwargs):  # noqa: E501
        """List log inspection rules  # noqa: E501

        Lists all log inspection rules assigned to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_log_inspection_rules_on_policy_with_http_info(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only rules assigned to the current policy.
        :return: LogInspectionRules
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_log_inspection_rules_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `list_log_inspection_rules_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_log_inspection_rules_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `list_log_inspection_rules_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/loginspection/rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogInspectionRules',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_log_inspection_rule_on_policy(self, policy_id, log_inspection_rule_id, log_inspection_rule, api_version, **kwargs):  # noqa: E501
        """Modify an log inspection rule  # noqa: E501

        Modify an log inspection rule assigned to a policy. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_log_inspection_rule_on_policy(policy_id, log_inspection_rule_id, log_inspection_rule, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int log_inspection_rule_id: The ID number of the log inspection rule to modify. (required)
        :param LogInspectionRule log_inspection_rule: The settings of the log inspection rule to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: LogInspectionRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_log_inspection_rule_on_policy_with_http_info(policy_id, log_inspection_rule_id, log_inspection_rule, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_log_inspection_rule_on_policy_with_http_info(policy_id, log_inspection_rule_id, log_inspection_rule, api_version, **kwargs)  # noqa: E501
            return data

    def modify_log_inspection_rule_on_policy_with_http_info(self, policy_id, log_inspection_rule_id, log_inspection_rule, api_version, **kwargs):  # noqa: E501
        """Modify an log inspection rule  # noqa: E501

        Modify an log inspection rule assigned to a policy. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_log_inspection_rule_on_policy_with_http_info(policy_id, log_inspection_rule_id, log_inspection_rule, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int log_inspection_rule_id: The ID number of the log inspection rule to modify. (required)
        :param LogInspectionRule log_inspection_rule: The settings of the log inspection rule to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: LogInspectionRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'log_inspection_rule_id', 'log_inspection_rule', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_log_inspection_rule_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `modify_log_inspection_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'log_inspection_rule_id' is set
        if ('log_inspection_rule_id' not in params or
                params['log_inspection_rule_id'] is None):
            raise ValueError("Missing the required parameter `log_inspection_rule_id` when calling `modify_log_inspection_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'log_inspection_rule' is set
        if ('log_inspection_rule' not in params or
                params['log_inspection_rule'] is None):
            raise ValueError("Missing the required parameter `log_inspection_rule` when calling `modify_log_inspection_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_log_inspection_rule_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `modify_log_inspection_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'log_inspection_rule_id' in params and not re.search('\\d+', str(params['log_inspection_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `log_inspection_rule_id` when calling `modify_log_inspection_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'log_inspection_rule_id' in params:
            path_params['logInspectionRuleID'] = params['log_inspection_rule_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'log_inspection_rule' in params:
            body_params = params['log_inspection_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/loginspection/rules/{logInspectionRuleID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogInspectionRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_log_inspection_rule_on_policy(self, policy_id, log_inspection_rule_id, api_version, **kwargs):  # noqa: E501
        """Reset log inspection rule overrides  # noqa: E501

        Remove all overrides for an log inspection rule from a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_log_inspection_rule_on_policy(policy_id, log_inspection_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int log_inspection_rule_id: The ID number of the log inspection rule to reset. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: LogInspectionRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reset_log_inspection_rule_on_policy_with_http_info(policy_id, log_inspection_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.reset_log_inspection_rule_on_policy_with_http_info(policy_id, log_inspection_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def reset_log_inspection_rule_on_policy_with_http_info(self, policy_id, log_inspection_rule_id, api_version, **kwargs):  # noqa: E501
        """Reset log inspection rule overrides  # noqa: E501

        Remove all overrides for an log inspection rule from a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_log_inspection_rule_on_policy_with_http_info(policy_id, log_inspection_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int log_inspection_rule_id: The ID number of the log inspection rule to reset. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: LogInspectionRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'log_inspection_rule_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_log_inspection_rule_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `reset_log_inspection_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'log_inspection_rule_id' is set
        if ('log_inspection_rule_id' not in params or
                params['log_inspection_rule_id'] is None):
            raise ValueError("Missing the required parameter `log_inspection_rule_id` when calling `reset_log_inspection_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `reset_log_inspection_rule_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `reset_log_inspection_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'log_inspection_rule_id' in params and not re.search('\\d+', str(params['log_inspection_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `log_inspection_rule_id` when calling `reset_log_inspection_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'log_inspection_rule_id' in params:
            path_params['logInspectionRuleID'] = params['log_inspection_rule_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/loginspection/rules/{logInspectionRuleID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogInspectionRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
