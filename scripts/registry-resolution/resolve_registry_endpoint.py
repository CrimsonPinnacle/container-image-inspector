#!/usr/bin/env python3

"""
:mod: `resolve_registry_endpoint.py` -- Resolves and analyses container registry's DNS name
========================================================================================

    module:: resolve_registry_endpoint
    :platform: Unix, Windows
    :synopsis: This module 
    moduleauthor: Toddy Mladenov <toddysm@gmail.com>
"""
import argparse
import logging
import os
import re
import sys

from random import choices
from colorama import init, Fore, Back

# Configure logging
_log_msg_format = "%(asctime)s [%(levelname)s]: %(message)s"
_log_level = logging.DEBUG
logging.basicConfig(handlers=[logging.FileHandler("registry-resolution.log"),
                              logging.StreamHandler()], format=_log_msg_format, level=_log_level)

if __name__ == '__main__':
    """
    Resolves the container registry's endpoint DNS name and provides additional
    details about the DNS.

    It prints the information on the console and logs it to a `registry-resolution.log`
    file saved locally.
    """
    # Initializes colorama
    init()

    # parse the command line arguments
    parser = argparse.ArgumentParser(description="Resolves and analyses the container registry's DNS name")
    parser.add_argument('-i', '--image', help="The image for which to analyze the container registry name.\n \
                        Must be in one of the following formats:\n \
                         - `[registry-name].[domain]:[port]/[repository]:[tag-or-sha]\n \
                         - `[registry-name].[domain]/[repository]:[tag-or-sha]`\n \
                         - `[registry-name].[domain]/[repository]` (assumes `latest`)\n \
                         - `[repository]:[tag-or-sha]`\n (assumes DockerHub endpoint `registry-`1.docker.io`) \
                         - `[repository]` (assumes DockerHub endpoint `registry-`1.docker.io` and `latest`)\n", required=True)
                        
    args = parser.parse_args()

    logging.info(f"Analyzing the container registry DNS for image: {args.image}")
