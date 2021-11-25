#!/usr/bin/bash

set -e

podman build -t angband-standalone ./standalone

mkdir -p $(pwd)/standalone_out

podman unshare chown 0:0 -R $(pwd)/standalone_out
rm -rf $(pwd)/standalone_out
mkdir -p $(pwd)/standalone_out
podman unshare chown $UID:$UID -R $(pwd)/standalone_out

podman run -ti --rm \
    -v $(pwd)/standalone_out:/opt/angband:Z \
    -v $(pwd)/angband:/opt/orig/:Z,ro \
    -v $(pwd)/patch:/opt/patch/:Z,ro \
    localhost/angband-standalone:latest

podman unshare chown 0:0 -R $(pwd)/standalone_out
