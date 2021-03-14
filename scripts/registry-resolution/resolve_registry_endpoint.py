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

# RegEx for matching the docker distribution reference
_domain_regex_str = r"(?:[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]){1,63}(?:[.](?:[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]){1,63})+"
_repo_regex_str = r"(?:[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])(?:/[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])*"
_tag_regex_str = r"(?:[:])([\w][\w.-]{0,127})"
_sha_regex_str = r"(?:[@])([A-Za-z][A-Za-z0-9]*(?:[-_+.][A-Za-z][A-Za-z0-9]*)*[:][0-9A-Fa-f]{32,})"
_reference_regex_str = f"({_domain_regex_str})?/?({_repo_regex_str})(?:(?:{_tag_regex_str})|(?:{_sha_regex_str}))*"

_reference_regex = re.compile(_reference_regex_str)

print(_reference_regex.match("mcr.microsoft.com/acr/test/hello-world:v1.0").groups())
print(_reference_regex.match("mcr.microsoft.com/acr/test/hello-world@sha256:238f32f98492b75484d1f00f8cfb91deafd0d5b692ead87e2dadce9b718c1984").groups())
print(_reference_regex.match("acr/test/hello-world:v1.0").groups())
print(_reference_regex.match("acr/test/hello-world@sha256:238f32f98492b75484d1f00f8cfb91deafd0d5b692ead87e2dadce9b718c1984").groups())
print(_reference_regex.match("acr/test/hello-world").groups())
print(_reference_regex.match("hello-world").groups())

if __name__ == '__main__':
    """Resolves the container registry's endpoint DNS name and provides additional
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
