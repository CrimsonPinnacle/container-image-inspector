#!/usr/bin/env python3

"""
:mod: `test_artifact_reference.py` -- Tests the image reference
================================================================================

    module:: test_artifactreference
    :platform: Unix, Windows
    :synopsis: This module contains tests for the image reference.
    moduleauthor: Toddy Mladenov <toddysm@gmail.com>
"""
import os
import sys

from pathlib import Path

# Construct the root to add for import purposes
project_path = Path(os.path.dirname(__file__)).absolute().parent
sys.path.append(str(project_path))

import unittest
from libraries import artifact

class TestArtifactReference(unittest.TestCase):
    """
    Tests the regular expressions that parse the artifact's reference and ensures
    they can properly match the components of the reference.
    """
    __fqr_with_tag = 'my.registry.com/product/app/hello-world:v1.0'
    __fqr_with_sha = 'my.registry.com/product/app/hello-world@sha256:238f32f98492b75484d1f00f8cfb91deafd0d5b692ead87e2dadce9b718c1984'
    __sr_with_tag = 'product/app/hello-world:v1.0'
    __sr_with_sha = 'product/app/hello-world@sha256:238f32f98492b75484d1f00f8cfb91deafd0d5b692ead87e2dadce9b718c1984'
    __hierarchical_repo = 'product/app/hello-world'
    __flat_repo = 'hello-world'

    def setUp(self):
        """
        Sets up the artifact reference test by initializing the different
        references.
        """
        self.fqr_with_tag = artifact.ArtifactReference(self.__fqr_with_tag)
        self.fqr_with_sha = artifact.ArtifactReference(self.__fqr_with_sha)
        self.sr_with_tag = artifact.ArtifactReference(self.__sr_with_tag)
        self.sr_with_sha = artifact.ArtifactReference(self.__sr_with_sha)
        self.hierarchical_repo = artifact.ArtifactReference(self.__hierarchical_repo)
        self.flat_repo = artifact.ArtifactReference(self.__flat_repo)

    def test_registry_endpoint(self):
        """
        Tests the extraction of the registry endpoint from an artifact reference. 
        """
        self.assertEqual(self.fqr_with_tag.get_registry_endpoint(), 'my.registry.com')
        self.assertEqual(self.fqr_with_sha.get_registry_endpoint(), 'my.registry.com')
        self.assertIsNone(self.sr_with_tag.get_registry_endpoint())
        self.assertIsNone(self.sr_with_sha.get_registry_endpoint())
        self.assertIsNone(self.hierarchical_repo.get_registry_endpoint())
        self.assertIsNone(self.flat_repo.get_registry_endpoint())
    
    def test_repository_name(self):
        """
        Tests the extraction of the repository name from an artifact reference. 
        """
        self.assertEqual(self.fqr_with_tag.get_repository_name(), 'product/app/hello-world')
        self.assertEqual(self.fqr_with_sha.get_repository_name(), 'product/app/hello-world')
        self.assertEqual(self.sr_with_tag.get_repository_name(), 'product/app/hello-world')
        self.assertEqual(self.sr_with_sha.get_repository_name(), 'product/app/hello-world')
        self.assertEqual(self.hierarchical_repo.get_repository_name(), 'product/app/hello-world')
        self.assertEqual(self.flat_repo.get_repository_name(), 'hello-world')

    def test_image_tag(self):
        """
        Tests the extraction of the image tag from an artifact reference. 
        """
        self.assertEqual(self.fqr_with_tag.get_image_tag(), 'v1.0')
        self.assertIsNone(self.fqr_with_sha.get_image_tag())
        self.assertEqual(self.sr_with_tag.get_image_tag(), 'v1.0')
        self.assertIsNone(self.sr_with_sha.get_image_tag())
        self.assertIsNone(self.hierarchical_repo.get_image_tag())
        self.assertIsNone(self.flat_repo.get_image_tag())

    def test_image_sha(self):
        """
        Tests the extraction of the image tag from an artifact reference. 
        """
        self.assertIsNone(self.fqr_with_tag.get_image_sha())
        self.assertEqual(self.fqr_with_sha.get_image_sha(), 'sha256:238f32f98492b75484d1f00f8cfb91deafd0d5b692ead87e2dadce9b718c1984')
        self.assertIsNone(self.sr_with_tag.get_image_sha())
        self.assertEqual(self.sr_with_sha.get_image_sha(), 'sha256:238f32f98492b75484d1f00f8cfb91deafd0d5b692ead87e2dadce9b718c1984')
        self.assertIsNone(self.hierarchical_repo.get_image_sha())
        self.assertIsNone(self.flat_repo.get_image_sha())

if __name__ == '__main__':
    unittest.main()
