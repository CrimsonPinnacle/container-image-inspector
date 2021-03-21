#!/usr/bin/env python3

"""
:mod: `select_access_token.py` -- Parses the file with Azure access tokens and selects one
==========================================================================================

    module:: select_access_token
    :platform: Unix, Windows
    :synopsis: This script parses the file with Azure access tokens and selects one
    moduleauthor: Toddy Mladenov <toddysm@gmail.com>
"""
import argparse
import json
import logging

from random import choices
from colorama import init, Fore, Back
from pathlib import Path

# Configure logging
_log_msg_format = "%(asctime)s [%(levelname)s]: %(message)s"
_log_level = logging.ERROR
logging.basicConfig(handlers=[logging.FileHandler("select-access-token.log"),
                              logging.StreamHandler()], format=_log_msg_format, level=_log_level)

def pprint_token_info(access_tokens):
    """
    Pretty prints the access token details.

    :param access_tokens: The tenant identifier (GUID)
    :type access_tokens: List of dictionaries
    """
    print("{:<5} {:<36} {:<36} {:<10}".format(' ', 'User', 'Provider/Tenant', 'Expires On'))
    counter = 0
    for token in access_tokens:
        if 'servicePrincipalId' in token:
            print("{:<5} {:<36} {:<36} {:<10}".format(counter, token['servicePrincipalId'],
                    token['servicePrincipalTenant'], 'N/A'))
        if 'userId' in token:
            print("{:<5} {:<36} {:<36} {:<10}".format(counter, token['userId'], 
                    token['identityProvider'], token['expiresOn']))
        
        counter += 1

if __name__ == '__main__':
    """
    Parses the file with Azure access tokens and gives the user the option to select one.

    By default the access tokens are saved in `~/.azure/accessTokens.json but the script allows
    to use different file for the input.

    It prints the information on the console and logs it to a `select-access-token.log`
    file saved locally.
    """
    # Initializes colorama
    init(autoreset=True)

    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="Parses the file with Azure access tokens and gives the user the option to select one.")
    parser.add_argument('-f', '--file', help="The file to load the tokens from.\n \
                         If not specified the default file `~/.azure/accessTokens.json` is used.", required=False)
                        
    args = parser.parse_args()

    # Get the user's home folder
    home = str(Path.home())

    if (args.file is None):
        print(Fore.YELLOW + f"Using default access tokens location '{home}/.azure/accessTokens.json'")
        args.file = f"{home}/.azure/accessTokens.json"

    logging.info(f"Using access token location: {args.file}")

    with open(args.file) as f:
        access_tokens = json.load(f)

    # Ask the user to select a token
    pprint_token_info(access_tokens)
    selection = ""
    while not (isinstance(selection, int) and selection < len(access_tokens)):
        try:
            selection = int(input(Fore.GREEN + "Type the token number to select: " + Fore.YELLOW))
            if selection >= len(access_tokens):
                raise
        except:
            print(Fore.RED + f"Please select a number between 0 and {len(access_tokens) - 1}.")

    if 'servicePrincipalId' in access_tokens[selection]:
        print(f"Returning access token for Service Principal: {access_tokens[selection]['servicePrincipalId']}")
        print(access_tokens[selection]['accessToken'])
    if 'userId' in access_tokens[selection]:
        type_selection = ""
        while type_selection != 'a' and type_selection != 'r':
            type_selection = input(Fore.GREEN + "Select the token type to return ('a' for access token, 'r' for refresh token): " + Fore.YELLOW)
            if type_selection == 'a':
                print(f"Returning access token for user: {access_tokens[selection]['userId']}")
                print(access_tokens[selection]['accessToken'])
            elif type_selection == 'r':
                print(f"Returning refresh token for user: {access_tokens[selection]['userId']}")
                print(access_tokens[selection]['refreshToken'])            
            else:
                print(Fore.RED + "Please select 'a' for access token or 'r' for refresh token.")

