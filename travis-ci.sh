#!/bin/bash

image_name="xebialabsunsupported/xl-docker-demo-xlr-credentials-updater"

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build -t $image_name:latest .
docker push $image_name:$tag
