#!/usr/bin/env python3

"""
:mod: `authenticator.py` -- Common authentication helpers
================================================================================

    module:: authenticator
    :platform: Unix, Windows
    :synopsis: This module contains classes and helper functions that are common for 
    authenticating with artifact registries.
    moduleauthor: Toddy Mladenov <toddysm@gmail.com>
"""
import json
import requests
from string import Template

class AzureAuthenticator:
    """
    Helper class allowing authentication with Azure Container Registry.
    """

    __auth_url = Template('https://login.microsoftonline.com/$tenant_id/oauth2/token')
    __auth_resource = 'https://management.azure.com/'
    __header_content_type = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    __auth_body = {
        'grant_type': 'client_credentials',
        'client_id': None,
        'client_secret': None,
        'resource': __auth_resource
    }

    def __init__(self, tenant_id, subscription_id):
        """
        Initializes the Azure authenticator with the tenant identifier.

        :param tenant_id: The tenant identifier (GUID)
        :type tenant_id: string
        :param subscription_id: The subscription identifier (GUID)
        :type subscription_id: string
        """
        self.tenant_id = tenant_id
        self.subscription_id = subscription_id
        self.__auth_url = self.__auth_url.substitute(tenant_id=tenant_id)

    def get_access_token_with_sp(self, app_id, app_secret):
        """
        Retrieves access token using Service Principal authentication.

        :param app_id: Azure application identifier (GUID)
        :type app_id: string
        :param app_secret: Azure application secret
        :type app_secret: string
        """
        self.__auth_body['client_id'] = app_id
        self.__auth_body['client_secret'] = app_secret
        token_response = requests.post(self.__auth_url, headers=self.__header_content_type, data=self.__auth_body)
        return token_response.json()['access_token']
