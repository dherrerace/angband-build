#!/usr/bin/bash

set -e

cp -rT /opt/orig /opt/rpm/angband-${VERSION}

bash generate-tarball.sh ${VERSION}

rpmdev-setuptree

mv angband-${VERSION}-patched.tar.gz ~/rpmbuild/SOURCES/
mv angband.png ~/rpmbuild/SOURCES/
mv angband.desktop ~/rpmbuild/SOURCES/
cp /opt/patch/*.patch ~/rpmbuild/SOURCES/

rpmbuild -ba angband.spec