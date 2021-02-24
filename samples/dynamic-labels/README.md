# Dynamic Docker Image Labels Sample

This sample demonstrates how to use dynamic Docker image labels to embed the Dockerfile and other origin information into the Docker image.

## How to Use This Sample?

You can build the sample locally by using the following command:

```
docker build -t test --build-arg IMAGE_COMMITTER=<username> --build-arg IMAGE_DOCKERFILE=<url> --build-arg IMAGE_COMMIT_SHA=<sha> -f .\samples\dynamic-labels\Dockerfile .
```

You can also build the command automatically using the following GitHub Actions:

- [GitHub Action for building and pushing image with dynamic labels to DockerHub](../../.github/workflows/gha-dynamic-docker-labels-dockerhub.yml)
- [GitHub Action for building and pushing image with dynamic labels to Azure Container Registry](../../.github/workflows/gha-dynamic-docker-labels-acr.yml)

The above two GitHub Actions are triggered on `push` or `pull_request` to the `development` branch in the GitHub repository.

## Help Improve This Sample

You can help improve this sample by sending feedback, filing an issue or asking a question. You are also welcome to submit a Pull Request.

[![Issues](https://img.shields.io/github/issues/crimsonpinnacle/container-image-inspector)](https://github.com/CrimsonPinnacle/container-image-inspector/issues/new) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/CrimsonPinnacle/container-image-inspector/pulls)
