#!/usr/bin/env python3

"""
:mod: `resolve_registry_endpoint.py` -- Resolves and analyses cxontainer registry's DNS name
========================================================================================

    module:: resolve_registry_endpoint
    :platform: Unix, Windows
    :synopsis: This module 
    moduleauthor: Toddy Mladenov <toddysm@gmail.com>
"""
import argparse
import logging
import os
import sys

from random import choices
from colorama import init, Fore, Back

# Configure logging
log_msg_format = "%(asctime)s (%(module)s --> %(funcName)s[%(lineno)d]) [%(levelname)s]: %(message)s"
log_level = logging.DEBUG
logging.basicConfig(filename="registry-resolution.log", filemode='w', format=log_msg_format, level=log_level)

if __name__ == '__main__':
    """Resolves the container registry's endpoint DNS name and provides additional
    details about the DNS resolution.

    It prints the information on the console and logs it to a `registry-resolution.log`
    file saved locally.
    """
    # Initializes colorama
    init()

    # parse the command line arguments
    parser = argparse.ArgumentParser(description="Resolves and analyses the container registry's DNS name")
    parser.add_argument('-i', '--image', help="The image for which to analyze the container registry name. \
                        Must be in the format `[registry-name].[domain]/[repository]:[tag-or-sha]", required=True)
                        
    args = parser.parse_args()

    logging.info("Analyzing the container registry DNS for image: " + Fore.GREEN + f"{args.image}")
