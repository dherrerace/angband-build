#!/usr/bin/bash

set -e

podman build -t angband-standalone ./standalone

podman unshare chown 0:0 -R $(pwd)/out
rm -rf $(pwd)/out
mkdir -p $(pwd)/out
podman unshare chown $UID:$UID -R $(pwd)/out

podman run -ti --rm \
    -v $(pwd)/out:/opt/angband:Z \
    -v $(pwd)/angband:/opt/orig/:Z \
    localhost/angband-standalone:latest

podman unshare chown 0:0 -R $(pwd)/out
