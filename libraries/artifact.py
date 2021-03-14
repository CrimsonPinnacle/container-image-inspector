#!/usr/bin/env python3

"""
:mod: `artifact.py` -- Common artifact data and operations
================================================================================

    module:: artifact
    :platform: Unix, Windows
    :synopsis: This module contains classes and operations that are common for 
    artifacts. It also includes common exceptions thrown by artifacts operations.
    moduleauthor: Toddy Mladenov <toddysm@gmail.com>
"""
import re

class ArtifactReference:
    """
    Represents the reference to the artifact.
    """

    # RegEx for matching the docker distribution reference
    __domain_regex_str = r"(?:[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]){1,63}(?:[.](?:[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]){1,63})+"
    __repo_regex_str = r"(?:[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])(?:/[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])*"
    __tag_regex_str = r"(?:[:])([\w][\w.-]{0,127})"
    __sha_regex_str = r"(?:[@])([A-Za-z][A-Za-z0-9]*(?:[-_+.][A-Za-z][A-Za-z0-9]*)*[:][0-9A-Fa-f]{32,})"

    def __init__(self, ref_str):
        """
        Initializes the artifact reference with a string. The string must follow
        the artifact reference spec.

        References:
        - https://github.com/distribution/distribution/blob/main/reference/regexp.go

        :param ref_str: The artifact reference 
        :type ref_str: string
        :raises ArtifactInitializationException: If the provided reference doesn't
            follow the specification
        """
        self.ref_str = ref_str

        # Build the regex for matching the reference components
        reference_regex_str = f"({self.__domain_regex_str})?/?({self.__repo_regex_str})(?:(?:{self.__tag_regex_str})|(?:{self.__sha_regex_str}))*"
        reference_regex = re.compile(reference_regex_str)

        try:
            # Match the components of the reference
            self.ref = reference_regex.match(ref_str).groups()
        except AttributeError:
            # If the above reference doesn't match each group
            raise ArtifactInitializationException("Provided string doesn't represent a valid artifact reference")
        except Exception:
            raise ArtifactInitializationException("Unknown error while initializing artifact reference class")
    
    def get_registry_endpoint(self):
        """
        Returns the registry endpoint from the artifact refererence.

        :returns: The registry endpoint
        :rtype: string
        """

        # The first item in the tuple is the registry endpoint
        return self.ref[0]
    
    def get_repository(self):
        """
        Returns the repository from the artifact refererence.

        :returns: The repository
        :rtype: string
        """

        # The second item in the tuple is the registry endpoint
        return self.ref[1]

    def get_tag(self):
        """
        Returns the tag from the artifact refererence.

        :returns: The tag
        :rtype: string
        """

        # The third item in the tuple is the registry endpoint
        return self.ref[2]

    def get_sha(self):
        """
        Returns the SHA from the artifact refererence.

        :returns: The SHA
        :rtype: string
        """

        # The fourth item in the tuple is the registry endpoint
        return self.ref[3]

class ArtifactInitializationException(Exception):
    """
    Defines exception thrown during initializationof artifact classes.
    """
    def __init__(self, message):
        """
        Initializes the exception.

        :param message: The exception message
        :type message: string
        """
        super(ArtifactInitializationException, self).__init__(message)