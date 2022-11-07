#!/usr/bin/env sh

export AUTHORS="$(cat AUTHORS)"
export BUILD_DATETIME="$(date '+%FT%T.%N%:z')"
export BUILD_VERSION="$(cat VERSION)"

docker build \
    -t syntaxoru/syntaxbot:$BUILD_VERSION \
    --build-arg AUTHORS="$AUTHORS" \
    --build-arg BUILD_DATETIME="$BUILD_DATETIME" \
    --build-arg BUILD_VERSION="$BUILD_VERSION" \
    .