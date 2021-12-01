#!/bin/sh

VERSION=$1

rm -rf angband-${VERSION}/.git
rm -rf angband-${VERSION}/lib/tiles/shockbolt

sed -ie 's/shockbolt//' angband-${VERSION}/lib/tiles/Makefile
sed -ie '/name:5:Shockbolt/,$d' angband-${VERSION}/lib/tiles/list.txt

tar -czvf angband-${VERSION}-patched.tar.gz angband-${VERSION}
