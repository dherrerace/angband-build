#!/usr/bin/bash

set -e

VERSION=$(git -C $(pwd)/angband describe)

podman build -t angband-rpm ./rpm

mkdir -p $(pwd)/rpm_out

podman unshare chown 0:0 -R $(pwd)/rpm_out
rm -rf $(pwd)/rpm_out
mkdir -p $(pwd)/rpm_out
podman unshare chown $UID:$UID -R $(pwd)/rpm_out

podman run -ti --rm \
    -v $(pwd)/rpm_out:/root/rpmbuild/:Z \
    -v $(pwd)/angband:/opt/orig/:Z,ro \
    -v $(pwd)/patch:/opt/patch/:Z,ro \
    -e VERSION=${VERSION} \
    localhost/angband-rpm:latest

podman unshare chown 0:0 -R $(pwd)/rpm_out
