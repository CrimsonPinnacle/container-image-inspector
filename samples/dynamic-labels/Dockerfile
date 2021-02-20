FROM python:slim
ARG IMAGE_COMMITTER
ARG IMAGE_DOCKERFILE
ARG IMAGE_COMMIT_SHA
LABEL "build.user"=${IMAGE_COMMITTER}
LABEL "build.sha"=${IMAGE_COMMIT_SHA}
LABEL "build.dockerfile"=${IMAGE_DOCKERFILE}
ADD ./samples/dynamic-labels/source /
CMD ["python", "/show_environment.py"]