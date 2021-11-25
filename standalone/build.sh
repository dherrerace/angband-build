#!/usr/bin/bash

set -e

cp -rT /opt/orig /opt/angband

cd /opt/angband

# HACK to apply binary patches
rm -rf .git
git init -q
for i in /opt/patch/*.patch; do
   git apply $i
done

./autogen.sh

./configure \
    --with-no-install \
    --enable-curses \
    --enable-x11 \
    --enable-sdl2 \
    --enable-sdl2-mixer \
    --enable-tests

make
make tests